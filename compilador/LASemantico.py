from AnalisadorLAVisitor import AnalisadorLAVisitor
from Escopos import Escopos
from TabelaDeSimbolos import TabelaDeSimbolos, Tipo, Estrutura
from LASemanticoUtils import LASemanticoUtils, debug
from AnalisadorLAParser import AnalisadorLAParser

# Análise semântica do compilador
# implementamos algumas funções da classe visitor gerada pelo antlr.
class LASemantico(AnalisadorLAVisitor) :

    escoposAninhados : Escopos = Escopos(Tipo.VOID)

    # Começo da árvore gerada pela análise sintática
    def visitPrograma(self, ctx:AnalisadorLAParser.ProgramaContext):
        return super().visitPrograma(ctx)

    # Os algoritmos da linguagem LA apresentam declaração global e local
    def visitDeclaracao_global(self, ctx:AnalisadorLAParser.Declaracao_globalContext):
        escopoAtual = self.escoposAninhados.obterEscopoAtual()
        possibilidades = None

        if escopoAtual.existe(ctx.IDENT().getText()):
            LASemanticoUtils.adicionarErroSemantico(ctx.start, f'{ctx.IDENT().getText()} ja declarado anteriormente')
            possibilidades = super().visitDeclaracao_global(ctx)
        else:
            tipoRetornoFuncao = Tipo.VOID
            if ctx.getText().startswith("funcao"):
                tipoRetornoFuncao = LASemanticoUtils.getTipo(ctx.tipo_estendido().getText())
                escopoAtual.adicionar(ctx.IDENT().getText(), tipoRetornoFuncao, Estrutura.FUNCAO)
            else:
                tipoRetornoFuncao = Tipo.VOID
                escopoAtual.adicionar(ctx.IDENT().getText(), tipoRetornoFuncao, Estrutura.PROCEDIMENTO)
            self.escoposAninhados.criarNovoEscopo(tipoRetornoFuncao)
            escopoAntigo = escopoAtual
            escopoAtual = self.escoposAninhados.obterEscopoAtual()
            if ctx.parametros() is not None:
                for param in ctx.parametros().parametro():
                    for id in param.identificador():
                        nomeId = ''
                        i = 0
                        for ident in id.IDENT():
                            if i > 0:
                                nomeId += '.'
                            i += 1
                            nomeId += ident.getText()
                        if escopoAtual.existe(nomeId):
                            LASemanticoUtils.adicionarErroSemantico(id.start, f'identificador {nomeId} ja declarado anteriormente')
                        else:
                            tipo = LASemanticoUtils.getTipo(param.tipo_estendido().getText())
                            if tipo is not None:
                                entrada = TabelaDeSimbolos.EntradaTabelaSimbolos(nomeId, tipo, Estrutura.VAR)
                                escopoAtual.adicionar(nomeId, tipo, Estrutura.VAR)
                                escopoAntigo.adicionarTipo(ctx.IDENT().getText(), entrada)
                            else:
                                identTipo = param.tipo_estendido().tipo_basico_ident().IDENT() if param.tipo_estendido().tipo_basico_ident() is not None and param.tipo_estendido().tipo_basico_ident().IDENT() is not None else None
                                if identTipo is not None:
                                    regVars = None
                                    for tabela in self.escoposAninhados.percorrerEscoposAninhados():
                                        if tabela.existe(identTipo.getText()):
                                            regVars = tabela.verificarTipo(identTipo.getText())
                                    if escopoAtual.existe(nomeId):
                                        LASemanticoUtils.adicionarErroSemantico(id.start, f"identificador {nomeId} ja declarado anteriormente")
                                    else:
                                        entrada = TabelaDeSimbolos.EntradaTabelaSimbolos(nomeId, Tipo.REGISTRO, Estrutura.VAR)
                                        escopoAtual.adicionar(nomeId, Tipo.REGISTRO, Estrutura.VAR)
                                        escopoAntigo.adicionarTipo(ctx.IDENT().getText(), entrada)

                                        for s in regVars:
                                            escopoAtual.adicionar(f"{nomeId}.{s.nome}", s.tipo, Estrutura.VAR)
            possibilidades = super().visitDeclaracao_global(ctx)
            self.escoposAninhados.abandonarEscopo()
        return possibilidades

    # A declaração local nos dividimos em outras regras na gramática para ficar mais organizado e fácil de implementar
    # Temos as declarações constantes.
    def visitDeclaracao_const(self, ctx: AnalisadorLAParser.Declaracao_constContext):
        print("declaracao const")
        
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
                escopoAtual.adicionar(ctx.IDENT().getText(), tipo, Estrutura.CONST)

        return super().visitDeclaracao_const(ctx)

    # Os tipos, temos constante (implementada na visitDeclaracao_const), 
    # variável (implementada na visitDeclaracao_var) e tipo (tipo estendido e registro que são implementados nessa função).
    def visitDeclaracao_tipo(self, ctx: AnalisadorLAParser.Declaracao_tipoContext):
        # escopoAtual = self.escoposAninhados.obterEscopoAtual()
        escopoAtual = self.escoposAninhados.obterEscopoAtual()
        if escopoAtual.existe(ctx.IDENT().getText()):
            LASemanticoUtils.adicionarErroSemantico(token=ctx.start,
                mensagem=f'tipo {ctx.IDENT().getText()} declarado duas vezes num mesmo escopo')
        else:
            tipo = LASemanticoUtils.getTipo(ctx.IDENT().getText())
            if tipo:
                escopoAtual.adicionar(ctx.IDENT().getText(), Tipo.TIPO, Estrutura.TIPO)
            elif ctx.tipo().registro():
                varRegistros: list[TabelaDeSimbolos.EntradaTabelaSimbolos] = []
                for variavel in ctx.tipo().registro().variavel():
                    tipoRegistrador = LASemanticoUtils.getTipo(variavel.tipo().getText())
                    for identificador in variavel.identificador():
                        varRegistros.append(TabelaDeSimbolos.EntradaTabelaSimbolos(identificador.getText(), tipoRegistrador, Estrutura.TIPO))
                        escopoAtual.adicionar(identificador.getText(), tipoRegistrador, Tipo.TIPO)
                if escopoAtual.existe(ctx.IDENT().getText()):
                    LASemanticoUtils.adicionarErroSemantico(token=ctx.start(),
                                                            mensagem=f'identificador {ctx.IDENT().getText()} ja declarado anteriormente')
                else:
                    escopoAtual.adicionar(ctx.IDENT().getText(), Tipo.REGISTRO, Estrutura.TIPO)
                    print("adicao", ctx.IDENT().getText(), Tipo.REGISTRO, Estrutura.TIPO, escopoAtual.tabela)
                # Vamos verificar se não há variáveis com mesmo nome dentro do registro
                for registro in varRegistros:
                    nomeVar = f"{ctx.IDENT().getText()}.{registro.nome}"
                    if escopoAtual.existe(nomeVar):
                        LASemanticoUtils.adicionarErroSemantico(token=ctx.start,
                                                                mensagem=f'identificador {nomeVar} ja declarado anteriormente')
                    else:
                        escopoAtual.adicionar(registro.nome, registro.tipo, registro.estrutura)
                        escopoAtual.adicionarTipo(ctx.IDENT().getText(), registro)
                print('mim add', registro.nome, registro.tipo, registro.estrutura, escopoAtual.tabela)

        # tipo = LASemanticoUtils.getTipo(ctx.tipo().getText())
        # escopoAtual.adicionar(ctx.IDENT().getText(), tipo, Estrutura.TIPO)
        return super().visitDeclaracao_tipo(ctx)
    
    # As variáveis. 
    def visitDeclaracao_var(self, ctx: AnalisadorLAParser.Declaracao_varContext):
        escopoAtual = self.escoposAninhados.obterEscopoAtual()
        
        for identificador in ctx.variavel().identificador():
            nomeId = ''
            i = 0
            for ident in identificador.IDENT():
                if i > 0:
                    nomeId += '.'
                nomeId += ident.getText()
            print(nomeId, escopoAtual.existe(nomeId), escopoAtual.tabela)
            if escopoAtual.existe(nomeId):
                LASemanticoUtils.adicionarErroSemantico(identificador.start,
                    f'identificador {identificador.getText()} ja declarado anteriormente')
            else:
                try:
                    identTipo = ctx.variavel().tipo().tipo_estendido().tipo_basico_ident().IDENT()
                except AttributeError:
                    identTipo = None
                if identTipo:
                    registros: list[TabelaDeSimbolos.EntradaTabelaSimbolos] = None
                    for tabela in self.escoposAninhados.percorrerEscoposAninhados():
                        if tabela.existe(identTipo.getText()):
                            registros = tabela.verificarTipo(identTipo.getText())
                    if escopoAtual.existe(nomeId):
                        LASemanticoUtils.adicionarErroSemantico(identificador.start, f"identificador {nomeId} ja declarado anteriormente")
                    else:
                        escopoAtual.adicionar(nomeId, Tipo.REGISTRO, Estrutura.VAR)
                        if registros:
                            for registro in registros:
                                escopoAtual.adicionar(f"{nomeId}.{registro.nome}", registro.tipo, Estrutura.VAR)
                # adicionar variáveis na tabela de dentro do registro (os registros são registrados na tabela)
                elif ctx.variavel().tipo().registro():
                    registros: list[TabelaDeSimbolos.EntradaTabelaSimbolos] = []
                    for variavel in ctx.variavel().tipo().registro().variavel():
                        tipoRegistros = LASemanticoUtils.getTipo(variavel.tipo().getText())
                        for identificador in variavel.identificador():
                            entrada = TabelaDeSimbolos.EntradaTabelaSimbolos(identificador.getText(), tipoRegistros, Estrutura.VAR)
                            escopoAtual.adicionar(entrada.nome, entrada.tipo, entrada.estrutura)
                            registros.append(entrada)
                    escopoAtual.adicionar(nomeId, Tipo.REGISTRO, Estrutura.VAR)
                    for registro in registros:
                        nomeVar = nomeId + '.' + registro.nome
                        if escopoAtual.existe(nomeVar):
                            LASemanticoUtils.adicionarErroSemantico(identificador.start, f"identificador {nomeVar} ja declarado anteriormente")
                        else:
                            escopoAtual.adicionar(registro.nome, registro.tipo, registro.estrutura)
                            escopoAtual.adicionar(nomeVar, registro.tipo, Estrutura.VAR)
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
                    escopoAtual.adicionar(identificador.getText(), tipo, Estrutura.VAR)
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
                nomeVar = ''
            i = 0
            for ident in ctx.IDENT():
                if i > 0:
                    nomeVar += '.'
                nomeVar += ident.getText()
                i += 1
            erro = True
            for escopo in self.escoposAninhados.percorrerEscoposAninhados():
                if escopo.existe(nomeVar):
                    erro = False
                if erro:
                    LASemanticoUtils.adicionarErroSemantico(ctx.start, f'identificador {nomeVar} nao declarado')
                    break
        return super().visitIdentificador(ctx)

    # Visitamos a atribuição para acusar erros de tipos incompatíveis
    def visitCmdAtribuicao(self, ctx: AnalisadorLAParser.CmdAtribuicaoContext):
        escopos = self.escoposAninhados.percorrerEscoposAninhados()
        tipoExpressao = Tipo.NUM_INT
        for escopo in escopos:
            if escopo != None:
                tipoExpressao = LASemanticoUtils.verificarTipoExpr(escopo, ctx=ctx.expressao())
        print("cmd atribuicao")
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
    
    def visitCmdRetorne(self, ctx: AnalisadorLAParser.CmdRetorneContext):
        escopo_atual = self.escoposAninhados.obterEscopoAtual()
        if escopo_atual is None:
            LASemanticoUtils.adicionarErroSemantico(ctx.start, f"comando retorne nao permitido nesse escopo")
        return super().visitCmdRetorne(ctx)