from AnalisadorLAParser import AnalisadorLAParser as LAParser
from TabelaDeSimbolos import TabelaDeSimbolos, Tipo
from Escopos import Escopos

def debug(string: str, msg_prefix):
    if string.find('&') != -1 and False:
        print(f'{msg_prefix}: {string}')

# Classe responsável por verificação de erros, avaliamos, recursivamente, os principais componentes da gramática LA.
class LASemanticoUtils:
    errosSemanticos: list[str] = []
    
    @staticmethod
    def adicionarErroSemantico(token, mensagem: str):
        linha: int = token.line
        LASemanticoUtils.errosSemanticos.append(f"Linha {linha}: {mensagem}")
    
    # Começamos analisando a componente de maior posição na hierarquia da estrutura, a expressão.
    @staticmethod
    def verificarTipoExpr(tabela: TabelaDeSimbolos, ctx: LAParser.ExpressaoContext) -> Tipo:
        ret: Tipo = None
        # Esta, é formada por termo lógico, então vamos analisar seus termos.
        
        for ta in ctx.termo_logico():
            aux: Tipo = LASemanticoUtils.verificarTipoTermoLogico(tabela, ta)
            auxCompativel = (aux == Tipo.NUM_INT or aux == Tipo.NUM_REAL) and (ret == Tipo.NUM_INT or ret == Tipo.NUM_REAL)
            if ret == None:
                ret = aux
            # O erro é acusado quando a flag inválido no tipo se mantém.
            elif (ret != aux and not auxCompativel) and aux != Tipo.INVALIDO:
                LASemanticoUtils.adicionarErroSemantico(ctx.start, "Expressao " + ctx.getText() + " contem tipos incompativeis")
                ret = Tipo.INVALIDO
        return ret

    # O termo lógico é composto por fatores lógicos.
    @staticmethod
    def verificarTipoTermoLogico(tabela: TabelaDeSimbolos, ctx: LAParser.Termo_logicoContext) -> Tipo:
        ret: Tipo = None
        for fa in ctx.fator_logico():
            aux: Tipo = LASemanticoUtils.verificarFatorLogico(tabela, fa)
            auxCompativel = (aux == Tipo.NUM_INT or aux == Tipo.NUM_REAL) and (ret == Tipo.NUM_INT or ret == Tipo.NUM_REAL)
            if ret == None:
                ret = aux
            # O erro é acusado quando a flag inválido no tipo se mantém.
            elif (ret != aux and not auxCompativel) and aux != Tipo.INVALIDO:
                LASemanticoUtils.adicionarErroSemantico(ctx.start, "Termo " + ctx.getText() + " contem tipos incompativeis")
                ret = Tipo.INVALIDO
        return ret
    
    # Por sua vez, os fatores lógicos são formados por parcelas lógicas
    @staticmethod
    def verificarFatorLogico(tabela: TabelaDeSimbolos, ctx: LAParser.Fator_logicoContext) -> Tipo:
        return LASemanticoUtils.verificarParcelaLogica(tabela, ctx.parcela_logica())
    
    @staticmethod
    def verificarParcelaLogica(tabela: TabelaDeSimbolos, ctx: LAParser.Parcela_logicaContext) -> Tipo:
        if ctx.exp_relacional() != None:
            ret = LASemanticoUtils.verificarExprRelacional(tabela, ctx.exp_relacional())
        else:
            ret = Tipo.LOGICO
        return ret
    
    @staticmethod
    def verificarExprRelacional(tabela: TabelaDeSimbolos, ctx: LAParser.Exp_relacionalContext) -> Tipo:
        ret: Tipo = None
        
        # Para cada parcela lógica, vamos verificar a expressão aritmética que a compõe.
        if ctx.op_relacional() != None:
            for fa in ctx.exp_aritmetica():
                aux: Tipo = LASemanticoUtils.verificarExprAritmetica(tabela, fa)
                auxCompativel = (aux == Tipo.NUM_INT or aux == Tipo.NUM_REAL) and (ret == Tipo.NUM_INT or ret == Tipo.NUM_REAL)
                if ret == None:
                    ret = aux
                elif (ret != aux and not auxCompativel) and aux != Tipo.INVALIDO:
                    LASemanticoUtils.adicionarErroSemantico(ctx.start, "Termo " + ctx.getText() + " contem tipos incompativeis")
                    ret = Tipo.INVALIDO
            if ret != Tipo.INVALIDO:
                ret = Tipo.LOGICO
        else:
            ret = LASemanticoUtils.verificarExprAritmetica(tabela, ctx.exp_aritmetica(0))
        return ret
    
    # Daí, seguimos a mesma linha de raciocínio para as relações aritméticas.
    @staticmethod
    def verificarExprAritmetica(tabela: TabelaDeSimbolos, ctx: LAParser.Exp_aritmeticaContext) -> Tipo:
        ret: Tipo = None
        for fa in ctx.termo():
            aux: Tipo = LASemanticoUtils.verificarTipoTerm(tabela, fa)
            auxCompativel = (aux == Tipo.NUM_INT or aux == Tipo.NUM_REAL) and (ret == Tipo.NUM_INT or ret == Tipo.NUM_REAL)
            if ret == None:
                ret = aux
            elif (ret != aux and not auxCompativel) and aux != Tipo.INVALIDO:
                ret = Tipo.INVALIDO
        return ret
    
    @staticmethod
    def verificarTipoTerm(tabela: TabelaDeSimbolos, ctx: LAParser.TermoContext) -> Tipo:
        ret: Tipo = None
        for fa in ctx.fator():
            aux: Tipo = LASemanticoUtils.verificarTipoFat(tabela, fa)
            auxCompativel = (aux == Tipo.NUM_INT or aux == Tipo.NUM_REAL) and (ret == Tipo.NUM_INT or ret == Tipo.NUM_REAL)
            if ret == None:
                ret = aux
            elif (ret != aux and not auxCompativel) and aux != Tipo.INVALIDO:
                LASemanticoUtils.adicionarErroSemantico(ctx.start, "Termo " + ctx.getText() + " contem tipos incompativeis")
                ret = Tipo.INVALIDO
        return ret

    @staticmethod
    def verificarTipoFat(tabela: TabelaDeSimbolos, ctx: LAParser.FatorContext) -> Tipo:
        ret: Tipo = None
        for fa in ctx.parcela():
            aux: Tipo = LASemanticoUtils.verificarTipoParcela(tabela, fa)
            auxCompativel = (aux == Tipo.NUM_INT or aux == Tipo.NUM_REAL) and (ret == Tipo.NUM_INT or ret == Tipo.NUM_REAL)
            if ret == None:
                ret = aux
            elif (ret != aux and not auxCompativel) and aux != Tipo.INVALIDO:
                LASemanticoUtils.adicionarErroSemantico(ctx.start, "Termo " + ctx.getText() + " contem tipos incompativeis")
                ret = Tipo.INVALIDO
        return ret
    
    @staticmethod
    def verificarTipoParcela(tabela: TabelaDeSimbolos, ctx: LAParser.ParcelaContext) -> Tipo:
        ret = Tipo.INVALIDO
        
        # As parcelas aritméticas podem ser unárias ou não unárias, portanto precisamos verificá-las.
        if ctx.parcela_nao_unario() != None:
            debug(ctx.getText(), "parcela nao unaria")
            ret = LASemanticoUtils.verificarTipoParcelaNaoUnario(tabela, ctx.parcela_nao_unario())
        else:
            debug(ctx.getText(), "parcela unaria")
            ret = LASemanticoUtils.verificarTipoParcelaUnario(tabela, ctx.parcela_unario())
        return ret
    
    # Seguindo a gramática, devemos analisar o identificador desta parcela unária.
    @staticmethod
    def verificarTipoParcelaNaoUnario(tabela: TabelaDeSimbolos, ctx: LAParser.Parcela_nao_unarioContext) -> Tipo:
        if ctx.identificador() != None:
            debug(ctx.getText(), "ident")
            return LASemanticoUtils.verificarTipoIdentificador(tabela, ctx.identificador())
        return Tipo.CADEIA
    
    # 
    @staticmethod
    def verificarTipoIdentificador(tabela: TabelaDeSimbolos, ctx: LAParser.IdentificadorContext) -> Tipo:
        nomeVar = ""
        ret = Tipo.INVALIDO
        for i in range(len(ctx.IDENT())):
            nomeVar += ctx.IDENT(i).getText()
            # if necessário por conta do funcionamento do identificador na gramática
            # é colocado . antes de outros ident com excessão da última posição, que deve ser a dimensão.
            if i != len(ctx.IDENT()) - 1:
                nomeVar += "."
        if tabela.existe(nomeVar):
            ret = LASemanticoUtils.verificarTipo(tabela, nomeVar)
        return ret
    
    # Verificamos o tipo da parcela unária
    @staticmethod
    def verificarTipoParcelaUnario(tabela: TabelaDeSimbolos, ctx: LAParser.Parcela_unarioContext) -> Tipo:
        if tabela.existe(ctx.getText()):
            return LASemanticoUtils.verificarTipo(tabela, ctx.getText())
        if ctx.NUM_INT():
            return Tipo.NUM_INT
        if ctx.NUM_REAL():
            return Tipo.NUM_REAL
        if ctx.identificador():
            return LASemanticoUtils.verificarTipoIdentificador(tabela, ctx.identificador())
        if ctx.IDENT():
            return LASemanticoUtils.verificarTipo(tabela, ctx.IDENT().getText())
        ret = None
        for expressaoContext in ctx.expressao():
            aux = LASemanticoUtils.verificarTipoExpr(tabela, expressaoContext)
            if ret == None:
                ret = aux
            elif ret != aux and aux != Tipo.INVALIDO:
                ret = Tipo.INVALIDO
        return ret
    
    # Verifica se o tipo existe na tabela de símbolos
    @staticmethod
    def verificarTipo(tabela: TabelaDeSimbolos, nomeVar: str) -> Tipo:
        return tabela.verificar(nomeVar)
    
    @staticmethod
    def getTipo(valor: str):
        tipo = None
        if valor == 'literal':
            tipo = Tipo.CADEIA
        elif valor == 'inteiro':
            tipo = Tipo.NUM_INT
        elif valor == 'real':
            tipo = Tipo.NUM_REAL
        elif valor == 'logico':
            tipo = Tipo.LOGICO
        return tipo
    
    @staticmethod
    def getTipoC(valor: str):
        tipo = None
        if valor == 'literal':
            tipo = 'char'
        elif valor == 'inteiro':
            tipo = 'int'
        elif valor == 'real':
            tipo = 'float'
        elif valor == 'logico':
            tipo = 'bool'
        return tipo
    
    @staticmethod
    def getMascaraIO(valor: Tipo):
        tipo = None
        
        if valor == Tipo.CADEIA:
            tipo = 's'
        elif valor == Tipo.NUM_INT:
            tipo = 'd'
        elif valor == Tipo.NUM_REAL:
            tipo = 'f'
        
        return tipo