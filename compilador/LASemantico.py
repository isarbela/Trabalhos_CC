from AnalisadorLAVisitor import AnalisadorLAVisitor
from Escopos import Escopos
from TabelaDeSimbolos import TabelaDeSimbolos, Tipo
from LASemanticoUtils import LASemanticoUtils, debug
from AnalisadorLAParser import AnalisadorLAParser

# Análise semântica do compilador
# implementamos algumas funções da classe visitor gerada pelo antlr.
class LASemantico(AnalisadorLAVisitor) :

    escoposAninhados : Escopos = Escopos()

    # Começo da árvore gerada pela análise sintática
    def visitPrograma(self, ctx:AnalisadorLAParser.ProgramaContext):
        return super().visitPrograma(ctx)

    # Os algoritmos da linguagem LA apresentam declaração global e local
    def visitDeclaracao_global(self, ctx:AnalisadorLAParser.Declaracao_globalContext):
        nomeVar = ctx.IDENT().getText()
        strTipoVar = ctx.tipo().getText()
        escopoAtual = self.escoposAninhados.obterEscopoAtual()

        if escopoAtual.existe(nomeVar):
            LASemanticoUtils.adicionarErroSemantico(ctx.start, nomeVar + "ja declarado anteriormente")
        else:
            escopoAtual.adicionar(nomeVar, strTipoVar)

        return super().visitDeclaracao_global(ctx)

    # A declaração local nos dividimos em outras regras na gramática para ficar mais organizado e fácil de implementar
    # Temos as declarações constantes.
    def visitDeclaracao_const(self, ctx: AnalisadorLAParser.Declaracao_constContext):
        for escopoAtual in self.escoposAninhados.percorrerEscoposAninhados():
            if escopoAtual.existe(ctx.IDENT().getText()):
                LASemanticoUtils.adicionarErroSemantico(token=ctx.start,
                    mensagem=f'constante {ctx.IDENT().getText()} ja declarado anteriormente')
            else:
                tipo = Tipo.NUM_INT
                tipo_const = escopoAtual.verificar(ctx.valor_constante.getText())
                if tipo_const == 'literal':
                    tipo = Tipo.CADEIA
                elif tipo_const == 'real':
                    tipo = Tipo.NUM_REAL
                elif tipo_const == 'logico':
                    tipo = Tipo.LOGICO
                elif tipo_const == 'inteiro':
                    tipo = Tipo.NUM_INT
                escopoAtual.adicionar(ctx.IDENT().getText(), tipo)

        return super().visitDeclaracao_const(ctx)

    # Os tipos.
    def visitDeclaracao_tipo(self, ctx: AnalisadorLAParser.Declaracao_tipoContext):
        escopoAtual = self.escoposAninhados.obterEscopoAtual()
        
        if escopoAtual.existe(ctx.IDENT().getText()):
            LASemanticoUtils.adicionarErroSemantico(token=ctx.start,
                mensagem=f'tipo {ctx.IDENT().getText()} declarado duas vezes num mesmo escopo')
        else:
            escopoAtual.adicionar(ctx.IDENT().getText(), Tipo.TIPO)
        return super().visitDeclaracao_tipo(ctx)
    
    # As variáveis. 
    def visitDeclaracao_var(self, ctx: AnalisadorLAParser.Declaracao_varContext):
        escopos = self.escoposAninhados.percorrerEscoposAninhados()

        for escopoAtual in escopos:
            for identificador in ctx.variavel().identificador():
                if escopoAtual.existe(identificador.getText()):
                    LASemanticoUtils.adicionarErroSemantico(identificador.start,
                        f'identificador {identificador.getText()} ja declarado anteriormente')
                else:
                    tipo = Tipo.INVALIDO
                    tipo_variavel = ctx.variavel().tipo().getText()
                    if tipo_variavel == 'literal' or tipo_variavel == '^literal':
                        tipo = Tipo.CADEIA
                    elif tipo_variavel == 'real' or tipo_variavel == '^real':
                        tipo = Tipo.NUM_REAL
                    elif tipo_variavel == 'logico' or tipo_variavel == '^logico':
                        tipo = Tipo.LOGICO
                    elif tipo_variavel == 'inteiro' or tipo_variavel == '^inteiro':
                        tipo = Tipo.NUM_INT
                    escopoAtual.adicionar(identificador.getText(), tipo)
        return super().visitDeclaracao_var(ctx)
    
    # Para analisar a tipagem, visitamos as regras de tipo básico dos identificadores (variáveis da linguagem)
    def visitTipo_basico_ident(self, ctx: AnalisadorLAParser.Tipo_basico_identContext):
        # Verifica se a variável existe em cada escopo
        # Devolve erro para o primeiro escopo que não existir.
        if ctx.IDENT() != None:
            for escopo in self.escoposAninhados.percorrerEscoposAninhados():
                if not escopo.existe(ctx.IDENT().getText()):
                    LASemanticoUtils.adicionarErroSemantico(ctx.start, f'tipo {ctx.IDENT().getText()} nao declarado')
                    break

        return super().visitTipo_basico_ident(ctx)
    
    def visitIdentificador(self, ctx: AnalisadorLAParser.IdentificadorContext):
        if ctx.IDENT() != None:
            for escopo in self.escoposAninhados.percorrerEscoposAninhados():
                if not escopo.existe(ctx.IDENT(0).getText()):
                    LASemanticoUtils.adicionarErroSemantico(ctx.start, f'identificador {ctx.IDENT(0).getText()} nao declarado')
                break
        return super().visitIdentificador(ctx)

    # Visitamos a atribuição para acusar erros de tipos incompatíveis
    def visitCmdAtribuicao(self, ctx: AnalisadorLAParser.CmdAtribuicaoContext):
        escopos = self.escoposAninhados.percorrerEscoposAninhados()
        tipoExpressao = Tipo.NUM_INT
        for escopo in escopos:
            if escopo != None:
                tipoExpressao = LASemanticoUtils.verificarTipoExpr(escopo, ctx=ctx.expressao())
        
        error = False
        pointer_prefix = "^" if ctx.getText()[0] == "^" else ""
        nomeVar = ctx.identificador().getText()
        debug(ctx.getText(), tipoExpressao)
        if tipoExpressao != Tipo.INVALIDO:
            for escopo in self.escoposAninhados.percorrerEscoposAninhados():
                if escopo.existe(nomeVar):
                    tipoVar = LASemanticoUtils.verificarTipo(escopo, nomeVar)
                    print(ctx.getText(), f"{tipoVar}")
                    
                    varNumeric = tipoVar == Tipo.NUM_INT or tipoVar == Tipo.NUM_REAL
                    expNumeric = tipoExpressao == Tipo.NUM_INT or tipoExpressao == Tipo.NUM_REAL
                    if not (varNumeric and expNumeric) and tipoVar != tipoExpressao and tipoExpressao != Tipo.INVALIDO:
                        error = True
        else:
            error = True

        if error:
            LASemanticoUtils.adicionarErroSemantico(ctx.identificador().start, f'atribuicao nao compativel para {pointer_prefix}{nomeVar}')
            
        return super().visitCmdAtribuicao(ctx)
    