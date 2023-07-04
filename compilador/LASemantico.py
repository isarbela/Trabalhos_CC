class LASemantico(AnalisadorLAVisitor) :

    escoposAninhados : Escopos = Escopos()
    tabela : TabelaDeSimbolos()

    def visitPrograma(self, ctx:AnalisadorLAParser.ProgramaContext):
        tabela = TabelaDeSimbolos()
        return super().visitPrograma(ctx)

    def visitDeclaracao_global(self, ctx:AnalisadorLAParser.Declaracao_globalContext):
        nomeVar = ctx.IDENT().getText()
        strTipoVar = ctx.tipo().getText()

