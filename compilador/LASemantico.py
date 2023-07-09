from AnalisadorLAVisitor import AnalisadorLAVisitor
from Escopos import Escopos
from TabelaDeSimbolos import TabelaDeSimbolos, Tipo
from LASemanticoUtils import LASemanticoUtils
from AnalisadorLAParser import AnalisadorLAParser


class LASemantico(AnalisadorLAVisitor) :

    escoposAninhados : Escopos = Escopos()

    def visitPrograma(self, ctx:AnalisadorLAParser.ProgramaContext):
        return super().visitPrograma(ctx)

    def visitDeclaracao_global(self, ctx:AnalisadorLAParser.Declaracao_globalContext):
        nomeVar = ctx.IDENT().getText()
        strTipoVar = ctx.tipo().getText()
        escopoAtual = self.escoposAninhados.obterEscopoAtual()

        if escopoAtual.existe(nomeVar):
            LASemanticoUtils.adicionarErroSemantico(ctx.start, nomeVar + "ja declarado anteriormente")
        else:
            escopoAtual.adicionar(nomeVar, strTipoVar)

        return super().visitDeclaracao_global(ctx)

    def visitDeclaracao_const(self, ctx: AnalisadorLAParser.Declaracao_constContext):
        for escopoAtual in self.escoposAninhados.percorrerEscoposAninhados():
            if escopoAtual.existe(ctx.IDENT().getText()):
                LASemanticoUtils.adicionarErroSemantico(token=ctx.start,
                    mensagem=f'constante {ctx.IDENT().getText()} ja declarado anteriormente')
            else:
                tipo = Tipo.INTEIRO
                tipo_basico = ctx.tipo_basico().getText()
                if tipo_basico == 'literal':
                    tipo = Tipo.LITERAL
                elif tipo_basico == 'real':
                    tipo = Tipo.REAL
                elif tipo == 'logico':
                    tipo = Tipo.LOGICO
                elif tipo_basico == 'inteiro':
                    tipo = Tipo.INTEIRO
                escopoAtual.adicionar(ctx.IDENT().getText(), tipo)

        return super().visitDeclaracao_const(ctx)

    def visitDeclaracao_tipo(self, ctx: AnalisadorLAParser.Declaracao_tipoContext):
        escopoAtual = self.escoposAninhados.obterEscopoAtual()
        
        if escopoAtual.existe(ctx.IDENT().getText()):
            LASemanticoUtils.adicionarErroSemantico(token=ctx.start,
                mensagem=f'tipo {ctx.IDENT().getText()} declarado duas vezes num mesmo escopo')
        else:
            escopoAtual.adicionar(ctx.IDENT().getText(), Tipo.TIPO)
        return super().visitDeclaracao_tipo(ctx)
    
    def visitDeclaracao_var(self, ctx: AnalisadorLAParser.Declaracao_varContext):
        escopos = self.escoposAninhados.percorrerEscoposAninhados()

        for escopoAtual in escopos:
            for identificador in ctx.variavel().identificador():
                print('\n\n\n\n\n\n\n\n', escopoAtual)
                if escopoAtual.existe(identificador.getText()):
                    LASemanticoUtils.adicionarErroSemantico(identificador.start,
                        f'identificador {identificador.getText()} ja declarado anteriormente')
                else:
                    tipo = Tipo.INTEIRO
                    tipo_basico = ctx.tipo_basico().getText()
                    if tipo_basico == 'literal':
                        tipo = Tipo.LITERAL
                    elif tipo_basico == 'real':
                        tipo = Tipo.REAL
                    elif tipo == 'logico':
                        tipo = Tipo.LOGICO
                    elif tipo_basico == 'inteiro':
                        tipo = Tipo.INTEIRO
                    escopoAtual.adicionar(identificador.getText(), tipo)
        return super().visitDeclaracao_var(ctx)
    
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
                if not escopo.existe(ctx.IDENT().getText()):
                    LASemanticoUtils.adicionarErroSemantico(ctx.start, f'identificador {ctx.IDENT().getText()} não declarado')
                break
        return super().visitIdentificador(ctx)

    def visitCmdAtribuicao(self, ctx: AnalisadorLAParser.CmdAtribuicaoContext):
        tipoExpressao = LASemanticoUtils.verificarTipoExpr(ctx=ctx.expressao())
        error = False
        nomeVar = ctx.identificador().getText()
        if tipoExpressao != TabelaDeSimbolos.TipoLA.INVALIDO:
            for escopo in LASemantico.escopos.obterPilha():
                if escopo.existe(nomeVar):
                    tipoVar = LASemanticoUtils.verificarTipoNomeVar(escopos=LASemantico.escopos, nomeVar=nomeVar)
                    varNumeric = tipoVar == TabelaDeSimbolos.TipoLA.INTEIRO or tipoVar == TabelaDeSimbolos.TipoLA.REAL
                    expNumeric = tipoExpressao == TabelaDeSimbolos.TipoLA.INTEIRO or tipoExpressao == TabelaDeSimbolos.TipoLA.REAL
                    if not (varNumeric and expNumeric) and tipoVar != tipoExpressao and tipoExpressao != TabelaDeSimbolos.TipoLA.INVALIDO:
                        error = True
        else:
            error = True

        if error:
            LASemanticoUtils.adicionarErroSemantico(ctx.identificador().start, f'atribuicao nao compativel para {nomeVar}')
            
        return super().visitCmdAtribuicao(ctx)
    