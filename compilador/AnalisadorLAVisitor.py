# Generated from T1_CC/compilador/AnalisadorLA.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .AnalisadorLAParser import AnalisadorLAParser
else:
    from AnalisadorLAParser import AnalisadorLAParser

# This class defines a complete generic visitor for a parse tree produced by AnalisadorLAParser.

class AnalisadorLAVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AnalisadorLAParser#programa.
    def visitPrograma(self, ctx:AnalisadorLAParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#declaracoes.
    def visitDeclaracoes(self, ctx:AnalisadorLAParser.DeclaracoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#declaracao_local.
    def visitDeclaracao_local(self, ctx:AnalisadorLAParser.Declaracao_localContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#declaracao_var.
    def visitDeclaracao_var(self, ctx:AnalisadorLAParser.Declaracao_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#declaracao_const.
    def visitDeclaracao_const(self, ctx:AnalisadorLAParser.Declaracao_constContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#declaracao_tipo.
    def visitDeclaracao_tipo(self, ctx:AnalisadorLAParser.Declaracao_tipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#variavel.
    def visitVariavel(self, ctx:AnalisadorLAParser.VariavelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#identificador.
    def visitIdentificador(self, ctx:AnalisadorLAParser.IdentificadorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#dimensao.
    def visitDimensao(self, ctx:AnalisadorLAParser.DimensaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#tipo.
    def visitTipo(self, ctx:AnalisadorLAParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#tipo_basico.
    def visitTipo_basico(self, ctx:AnalisadorLAParser.Tipo_basicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#tipo_basico_ident.
    def visitTipo_basico_ident(self, ctx:AnalisadorLAParser.Tipo_basico_identContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#tipo_estendido.
    def visitTipo_estendido(self, ctx:AnalisadorLAParser.Tipo_estendidoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#valor_constante.
    def visitValor_constante(self, ctx:AnalisadorLAParser.Valor_constanteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#registro.
    def visitRegistro(self, ctx:AnalisadorLAParser.RegistroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#declaracao_global.
    def visitDeclaracao_global(self, ctx:AnalisadorLAParser.Declaracao_globalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#corpo.
    def visitCorpo(self, ctx:AnalisadorLAParser.CorpoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#parametro.
    def visitParametro(self, ctx:AnalisadorLAParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#parametros.
    def visitParametros(self, ctx:AnalisadorLAParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#cmd.
    def visitCmd(self, ctx:AnalisadorLAParser.CmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#cmdLeia.
    def visitCmdLeia(self, ctx:AnalisadorLAParser.CmdLeiaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#cmdEscreva.
    def visitCmdEscreva(self, ctx:AnalisadorLAParser.CmdEscrevaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#cmdSe.
    def visitCmdSe(self, ctx:AnalisadorLAParser.CmdSeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#cmdSenao.
    def visitCmdSenao(self, ctx:AnalisadorLAParser.CmdSenaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#cmdCaso.
    def visitCmdCaso(self, ctx:AnalisadorLAParser.CmdCasoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#cmdPara.
    def visitCmdPara(self, ctx:AnalisadorLAParser.CmdParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#cmdEnquanto.
    def visitCmdEnquanto(self, ctx:AnalisadorLAParser.CmdEnquantoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#cmdFaca.
    def visitCmdFaca(self, ctx:AnalisadorLAParser.CmdFacaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#cmdAtribuicao.
    def visitCmdAtribuicao(self, ctx:AnalisadorLAParser.CmdAtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#cmdChamada.
    def visitCmdChamada(self, ctx:AnalisadorLAParser.CmdChamadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#cmdRetorne.
    def visitCmdRetorne(self, ctx:AnalisadorLAParser.CmdRetorneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#selecao.
    def visitSelecao(self, ctx:AnalisadorLAParser.SelecaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#item_selecao.
    def visitItem_selecao(self, ctx:AnalisadorLAParser.Item_selecaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#constantes.
    def visitConstantes(self, ctx:AnalisadorLAParser.ConstantesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#numero_intervalo.
    def visitNumero_intervalo(self, ctx:AnalisadorLAParser.Numero_intervaloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#op_unario.
    def visitOp_unario(self, ctx:AnalisadorLAParser.Op_unarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#exp_aritmetica.
    def visitExp_aritmetica(self, ctx:AnalisadorLAParser.Exp_aritmeticaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#termo.
    def visitTermo(self, ctx:AnalisadorLAParser.TermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#fator.
    def visitFator(self, ctx:AnalisadorLAParser.FatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#op1.
    def visitOp1(self, ctx:AnalisadorLAParser.Op1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#op2.
    def visitOp2(self, ctx:AnalisadorLAParser.Op2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#op3.
    def visitOp3(self, ctx:AnalisadorLAParser.Op3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#parcela.
    def visitParcela(self, ctx:AnalisadorLAParser.ParcelaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#parcela_unario.
    def visitParcela_unario(self, ctx:AnalisadorLAParser.Parcela_unarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#parcela_nao_unario.
    def visitParcela_nao_unario(self, ctx:AnalisadorLAParser.Parcela_nao_unarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#exp_relacional.
    def visitExp_relacional(self, ctx:AnalisadorLAParser.Exp_relacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#op_relacional.
    def visitOp_relacional(self, ctx:AnalisadorLAParser.Op_relacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#expressao.
    def visitExpressao(self, ctx:AnalisadorLAParser.ExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#termo_logico.
    def visitTermo_logico(self, ctx:AnalisadorLAParser.Termo_logicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#fator_logico.
    def visitFator_logico(self, ctx:AnalisadorLAParser.Fator_logicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#parcela_logica.
    def visitParcela_logica(self, ctx:AnalisadorLAParser.Parcela_logicaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#op_logico_1.
    def visitOp_logico_1(self, ctx:AnalisadorLAParser.Op_logico_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnalisadorLAParser#op_logico_2.
    def visitOp_logico_2(self, ctx:AnalisadorLAParser.Op_logico_2Context):
        return self.visitChildren(ctx)



del AnalisadorLAParser