# Generated from T1_CC/compilador/AnalisadorLA.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .AnalisadorLAParser import AnalisadorLAParser
else:
    from AnalisadorLAParser import AnalisadorLAParser

# This class defines a complete listener for a parse tree produced by AnalisadorLAParser.
class AnalisadorLAListener(ParseTreeListener):

    # Enter a parse tree produced by AnalisadorLAParser#programa.
    def enterPrograma(self, ctx:AnalisadorLAParser.ProgramaContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#programa.
    def exitPrograma(self, ctx:AnalisadorLAParser.ProgramaContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#declaracoes.
    def enterDeclaracoes(self, ctx:AnalisadorLAParser.DeclaracoesContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#declaracoes.
    def exitDeclaracoes(self, ctx:AnalisadorLAParser.DeclaracoesContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#declaracao_local.
    def enterDeclaracao_local(self, ctx:AnalisadorLAParser.Declaracao_localContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#declaracao_local.
    def exitDeclaracao_local(self, ctx:AnalisadorLAParser.Declaracao_localContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#declaracao_var.
    def enterDeclaracao_var(self, ctx:AnalisadorLAParser.Declaracao_varContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#declaracao_var.
    def exitDeclaracao_var(self, ctx:AnalisadorLAParser.Declaracao_varContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#declaracao_const.
    def enterDeclaracao_const(self, ctx:AnalisadorLAParser.Declaracao_constContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#declaracao_const.
    def exitDeclaracao_const(self, ctx:AnalisadorLAParser.Declaracao_constContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#declaracao_tipo.
    def enterDeclaracao_tipo(self, ctx:AnalisadorLAParser.Declaracao_tipoContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#declaracao_tipo.
    def exitDeclaracao_tipo(self, ctx:AnalisadorLAParser.Declaracao_tipoContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#variavel.
    def enterVariavel(self, ctx:AnalisadorLAParser.VariavelContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#variavel.
    def exitVariavel(self, ctx:AnalisadorLAParser.VariavelContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#identificador.
    def enterIdentificador(self, ctx:AnalisadorLAParser.IdentificadorContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#identificador.
    def exitIdentificador(self, ctx:AnalisadorLAParser.IdentificadorContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#dimensao.
    def enterDimensao(self, ctx:AnalisadorLAParser.DimensaoContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#dimensao.
    def exitDimensao(self, ctx:AnalisadorLAParser.DimensaoContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#tipo.
    def enterTipo(self, ctx:AnalisadorLAParser.TipoContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#tipo.
    def exitTipo(self, ctx:AnalisadorLAParser.TipoContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#tipo_basico.
    def enterTipo_basico(self, ctx:AnalisadorLAParser.Tipo_basicoContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#tipo_basico.
    def exitTipo_basico(self, ctx:AnalisadorLAParser.Tipo_basicoContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#tipo_basico_ident.
    def enterTipo_basico_ident(self, ctx:AnalisadorLAParser.Tipo_basico_identContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#tipo_basico_ident.
    def exitTipo_basico_ident(self, ctx:AnalisadorLAParser.Tipo_basico_identContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#tipo_estendido.
    def enterTipo_estendido(self, ctx:AnalisadorLAParser.Tipo_estendidoContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#tipo_estendido.
    def exitTipo_estendido(self, ctx:AnalisadorLAParser.Tipo_estendidoContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#valor_constante.
    def enterValor_constante(self, ctx:AnalisadorLAParser.Valor_constanteContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#valor_constante.
    def exitValor_constante(self, ctx:AnalisadorLAParser.Valor_constanteContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#registro.
    def enterRegistro(self, ctx:AnalisadorLAParser.RegistroContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#registro.
    def exitRegistro(self, ctx:AnalisadorLAParser.RegistroContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#declaracao_global.
    def enterDeclaracao_global(self, ctx:AnalisadorLAParser.Declaracao_globalContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#declaracao_global.
    def exitDeclaracao_global(self, ctx:AnalisadorLAParser.Declaracao_globalContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#corpo.
    def enterCorpo(self, ctx:AnalisadorLAParser.CorpoContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#corpo.
    def exitCorpo(self, ctx:AnalisadorLAParser.CorpoContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#parametro.
    def enterParametro(self, ctx:AnalisadorLAParser.ParametroContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#parametro.
    def exitParametro(self, ctx:AnalisadorLAParser.ParametroContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#parametros.
    def enterParametros(self, ctx:AnalisadorLAParser.ParametrosContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#parametros.
    def exitParametros(self, ctx:AnalisadorLAParser.ParametrosContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#cmd.
    def enterCmd(self, ctx:AnalisadorLAParser.CmdContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#cmd.
    def exitCmd(self, ctx:AnalisadorLAParser.CmdContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#cmdLeia.
    def enterCmdLeia(self, ctx:AnalisadorLAParser.CmdLeiaContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#cmdLeia.
    def exitCmdLeia(self, ctx:AnalisadorLAParser.CmdLeiaContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#cmdEscreva.
    def enterCmdEscreva(self, ctx:AnalisadorLAParser.CmdEscrevaContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#cmdEscreva.
    def exitCmdEscreva(self, ctx:AnalisadorLAParser.CmdEscrevaContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#cmdSe.
    def enterCmdSe(self, ctx:AnalisadorLAParser.CmdSeContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#cmdSe.
    def exitCmdSe(self, ctx:AnalisadorLAParser.CmdSeContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#cmdSenao.
    def enterCmdSenao(self, ctx:AnalisadorLAParser.CmdSenaoContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#cmdSenao.
    def exitCmdSenao(self, ctx:AnalisadorLAParser.CmdSenaoContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#cmdCaso.
    def enterCmdCaso(self, ctx:AnalisadorLAParser.CmdCasoContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#cmdCaso.
    def exitCmdCaso(self, ctx:AnalisadorLAParser.CmdCasoContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#cmdPara.
    def enterCmdPara(self, ctx:AnalisadorLAParser.CmdParaContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#cmdPara.
    def exitCmdPara(self, ctx:AnalisadorLAParser.CmdParaContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#cmdEnquanto.
    def enterCmdEnquanto(self, ctx:AnalisadorLAParser.CmdEnquantoContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#cmdEnquanto.
    def exitCmdEnquanto(self, ctx:AnalisadorLAParser.CmdEnquantoContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#cmdFaca.
    def enterCmdFaca(self, ctx:AnalisadorLAParser.CmdFacaContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#cmdFaca.
    def exitCmdFaca(self, ctx:AnalisadorLAParser.CmdFacaContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#cmdAtribuicao.
    def enterCmdAtribuicao(self, ctx:AnalisadorLAParser.CmdAtribuicaoContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#cmdAtribuicao.
    def exitCmdAtribuicao(self, ctx:AnalisadorLAParser.CmdAtribuicaoContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#cmdChamada.
    def enterCmdChamada(self, ctx:AnalisadorLAParser.CmdChamadaContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#cmdChamada.
    def exitCmdChamada(self, ctx:AnalisadorLAParser.CmdChamadaContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#cmdRetorne.
    def enterCmdRetorne(self, ctx:AnalisadorLAParser.CmdRetorneContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#cmdRetorne.
    def exitCmdRetorne(self, ctx:AnalisadorLAParser.CmdRetorneContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#selecao.
    def enterSelecao(self, ctx:AnalisadorLAParser.SelecaoContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#selecao.
    def exitSelecao(self, ctx:AnalisadorLAParser.SelecaoContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#item_selecao.
    def enterItem_selecao(self, ctx:AnalisadorLAParser.Item_selecaoContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#item_selecao.
    def exitItem_selecao(self, ctx:AnalisadorLAParser.Item_selecaoContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#constantes.
    def enterConstantes(self, ctx:AnalisadorLAParser.ConstantesContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#constantes.
    def exitConstantes(self, ctx:AnalisadorLAParser.ConstantesContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#numero_intervalo.
    def enterNumero_intervalo(self, ctx:AnalisadorLAParser.Numero_intervaloContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#numero_intervalo.
    def exitNumero_intervalo(self, ctx:AnalisadorLAParser.Numero_intervaloContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#op_unario.
    def enterOp_unario(self, ctx:AnalisadorLAParser.Op_unarioContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#op_unario.
    def exitOp_unario(self, ctx:AnalisadorLAParser.Op_unarioContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#exp_aritmetica.
    def enterExp_aritmetica(self, ctx:AnalisadorLAParser.Exp_aritmeticaContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#exp_aritmetica.
    def exitExp_aritmetica(self, ctx:AnalisadorLAParser.Exp_aritmeticaContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#termo.
    def enterTermo(self, ctx:AnalisadorLAParser.TermoContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#termo.
    def exitTermo(self, ctx:AnalisadorLAParser.TermoContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#fator.
    def enterFator(self, ctx:AnalisadorLAParser.FatorContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#fator.
    def exitFator(self, ctx:AnalisadorLAParser.FatorContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#op1.
    def enterOp1(self, ctx:AnalisadorLAParser.Op1Context):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#op1.
    def exitOp1(self, ctx:AnalisadorLAParser.Op1Context):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#op2.
    def enterOp2(self, ctx:AnalisadorLAParser.Op2Context):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#op2.
    def exitOp2(self, ctx:AnalisadorLAParser.Op2Context):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#op3.
    def enterOp3(self, ctx:AnalisadorLAParser.Op3Context):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#op3.
    def exitOp3(self, ctx:AnalisadorLAParser.Op3Context):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#parcela.
    def enterParcela(self, ctx:AnalisadorLAParser.ParcelaContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#parcela.
    def exitParcela(self, ctx:AnalisadorLAParser.ParcelaContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#parcela_unario.
    def enterParcela_unario(self, ctx:AnalisadorLAParser.Parcela_unarioContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#parcela_unario.
    def exitParcela_unario(self, ctx:AnalisadorLAParser.Parcela_unarioContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#parcela_nao_unario.
    def enterParcela_nao_unario(self, ctx:AnalisadorLAParser.Parcela_nao_unarioContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#parcela_nao_unario.
    def exitParcela_nao_unario(self, ctx:AnalisadorLAParser.Parcela_nao_unarioContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#exp_relacional.
    def enterExp_relacional(self, ctx:AnalisadorLAParser.Exp_relacionalContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#exp_relacional.
    def exitExp_relacional(self, ctx:AnalisadorLAParser.Exp_relacionalContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#op_relacional.
    def enterOp_relacional(self, ctx:AnalisadorLAParser.Op_relacionalContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#op_relacional.
    def exitOp_relacional(self, ctx:AnalisadorLAParser.Op_relacionalContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#expressao.
    def enterExpressao(self, ctx:AnalisadorLAParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#expressao.
    def exitExpressao(self, ctx:AnalisadorLAParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#termo_logico.
    def enterTermo_logico(self, ctx:AnalisadorLAParser.Termo_logicoContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#termo_logico.
    def exitTermo_logico(self, ctx:AnalisadorLAParser.Termo_logicoContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#fator_logico.
    def enterFator_logico(self, ctx:AnalisadorLAParser.Fator_logicoContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#fator_logico.
    def exitFator_logico(self, ctx:AnalisadorLAParser.Fator_logicoContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#parcela_logica.
    def enterParcela_logica(self, ctx:AnalisadorLAParser.Parcela_logicaContext):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#parcela_logica.
    def exitParcela_logica(self, ctx:AnalisadorLAParser.Parcela_logicaContext):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#op_logico_1.
    def enterOp_logico_1(self, ctx:AnalisadorLAParser.Op_logico_1Context):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#op_logico_1.
    def exitOp_logico_1(self, ctx:AnalisadorLAParser.Op_logico_1Context):
        pass


    # Enter a parse tree produced by AnalisadorLAParser#op_logico_2.
    def enterOp_logico_2(self, ctx:AnalisadorLAParser.Op_logico_2Context):
        pass

    # Exit a parse tree produced by AnalisadorLAParser#op_logico_2.
    def exitOp_logico_2(self, ctx:AnalisadorLAParser.Op_logico_2Context):
        pass



del AnalisadorLAParser