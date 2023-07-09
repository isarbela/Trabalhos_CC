from AnalisadorLAParser import AnalisadorLAParser as LAParser
from TabelaDeSimbolos import TabelaDeSimbolos, Tipo
from Escopos import Escopos

class LASemanticoUtils:
    errosSemanticos: list[str] = []
    
    @staticmethod
    def adicionarErroSemantico(token, mensagem: str):
        linha: int = token.getLine()
        LASemanticoUtils.errosSemanticos.add(f"Erro {linha}: {mensagem}")
    
    @staticmethod
    def verificarTipoExpr(tabela: TabelaDeSimbolos, escopos: Escopos, ctx: LAParser.ExpressaoContext) -> Tipo:
        ret: Tipo = None
        for ta in ctx.termoAritmetico():
            aux: Tipo = LASemanticoUtils.verificarTipo(tabela, ta)
            if ret == None:
                ret = aux
            elif ret != aux and aux != Tipo.INVALIDO:
                LASemanticoUtils.adicionarErroSemantico(ctx.start, "Expressão " + ctx.getText() + " contém tipos incompatíveis")
                ret = Tipo.INVALIDO
        return ret

    @staticmethod
    def verificarTipoTerm(tabela: TabelaDeSimbolos, ctx: LAParser.TermoContext) -> Tipo:
        ret: Tipo = None
        for fa in ctx.fatorAritmetico():
            aux: Tipo = LASemanticoUtils.verificarTipo(tabela, fa)
            if ret == None:
                ret = aux
            elif ret != aux and aux != Tipo.INVALIDO:
                LASemanticoUtils.adicionarErroSemantico(ctx.start, "Termo " + ctx.getText() + " contém tipos incompatíveis")
                ret = Tipo.INVALIDO
        return ret

    @staticmethod
    def verificarTipoFat(tabela: TabelaDeSimbolos, ctx: LAParser.FatorContext) -> Tipo:
        if ctx.NUMINT() != None:
            return Tipo.INTEIRO
        if ctx.NUMREAL() != None:
            return Tipo.REAL
        if ctx.VARIAVEL() != None:
            nomeVar: str = ctx.VARIAVEL().getText()
            if not tabela.existe(nomeVar):
                LASemanticoUtils.adicionarErroSemantico(ctx.VARIAVEL().getSymbol(), "Variável " + nomeVar + " não foi declarada antes do uso")
                return Tipo.INVALIDO
            return LASemanticoUtils.verificarTipo(tabela, nomeVar)
        # se não for nenhum dos tipos acima, só pode ser uma expressão
        # entre parêntesis
        return LASemanticoUtils.verificarTipo(tabela, ctx.expressaoAritmetica())
    
    @staticmethod
    def verificarTipo(tabela: TabelaDeSimbolos, nomeVar: str) -> Tipo:
        return tabela.verificar(nomeVar)
    
