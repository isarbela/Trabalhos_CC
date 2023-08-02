// Generated from compilador/AnalisadorLA.g4 by ANTLR 4.13.0
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link AnalisadorLAParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface AnalisadorLAVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#programa}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrograma(AnalisadorLAParser.ProgramaContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#declaracoes}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclaracoes(AnalisadorLAParser.DeclaracoesContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#declaracao_local}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclaracao_local(AnalisadorLAParser.Declaracao_localContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#declaracao_var}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclaracao_var(AnalisadorLAParser.Declaracao_varContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#declaracao_const}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclaracao_const(AnalisadorLAParser.Declaracao_constContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#declaracao_tipo}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclaracao_tipo(AnalisadorLAParser.Declaracao_tipoContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#variavel}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVariavel(AnalisadorLAParser.VariavelContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#identificador}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIdentificador(AnalisadorLAParser.IdentificadorContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#dimensao}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDimensao(AnalisadorLAParser.DimensaoContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#tipo}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTipo(AnalisadorLAParser.TipoContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#tipo_basico}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTipo_basico(AnalisadorLAParser.Tipo_basicoContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#tipo_basico_ident}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTipo_basico_ident(AnalisadorLAParser.Tipo_basico_identContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#tipo_estendido}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTipo_estendido(AnalisadorLAParser.Tipo_estendidoContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#valor_constante}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitValor_constante(AnalisadorLAParser.Valor_constanteContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#registro}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRegistro(AnalisadorLAParser.RegistroContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#declaracao_global}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclaracao_global(AnalisadorLAParser.Declaracao_globalContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#corpo}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCorpo(AnalisadorLAParser.CorpoContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#parametro}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParametro(AnalisadorLAParser.ParametroContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#parametros}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParametros(AnalisadorLAParser.ParametrosContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#cmd}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCmd(AnalisadorLAParser.CmdContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#cmdLeia}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCmdLeia(AnalisadorLAParser.CmdLeiaContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#cmdEscreva}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCmdEscreva(AnalisadorLAParser.CmdEscrevaContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#cmdSe}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCmdSe(AnalisadorLAParser.CmdSeContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#cmdSenao}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCmdSenao(AnalisadorLAParser.CmdSenaoContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#cmdCaso}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCmdCaso(AnalisadorLAParser.CmdCasoContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#cmdPara}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCmdPara(AnalisadorLAParser.CmdParaContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#cmdEnquanto}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCmdEnquanto(AnalisadorLAParser.CmdEnquantoContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#cmdFaca}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCmdFaca(AnalisadorLAParser.CmdFacaContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#cmdAtribuicao}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCmdAtribuicao(AnalisadorLAParser.CmdAtribuicaoContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#cmdChamada}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCmdChamada(AnalisadorLAParser.CmdChamadaContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#cmdRetorne}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCmdRetorne(AnalisadorLAParser.CmdRetorneContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#selecao}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSelecao(AnalisadorLAParser.SelecaoContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#item_selecao}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitItem_selecao(AnalisadorLAParser.Item_selecaoContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#constantes}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConstantes(AnalisadorLAParser.ConstantesContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#numero_intervalo}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNumero_intervalo(AnalisadorLAParser.Numero_intervaloContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#op_unario}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOp_unario(AnalisadorLAParser.Op_unarioContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#exp_aritmetica}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp_aritmetica(AnalisadorLAParser.Exp_aritmeticaContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#termo}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTermo(AnalisadorLAParser.TermoContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#fator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFator(AnalisadorLAParser.FatorContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#op1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOp1(AnalisadorLAParser.Op1Context ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#op2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOp2(AnalisadorLAParser.Op2Context ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#op3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOp3(AnalisadorLAParser.Op3Context ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#parcela}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParcela(AnalisadorLAParser.ParcelaContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#parcela_unario}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParcela_unario(AnalisadorLAParser.Parcela_unarioContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#expressao_parenteses}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpressao_parenteses(AnalisadorLAParser.Expressao_parentesesContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#parcela_nao_unario}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParcela_nao_unario(AnalisadorLAParser.Parcela_nao_unarioContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#exp_relacional}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp_relacional(AnalisadorLAParser.Exp_relacionalContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#op_relacional}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOp_relacional(AnalisadorLAParser.Op_relacionalContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#expressao}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpressao(AnalisadorLAParser.ExpressaoContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#termo_logico}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTermo_logico(AnalisadorLAParser.Termo_logicoContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#fator_logico}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFator_logico(AnalisadorLAParser.Fator_logicoContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#parcela_logica}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParcela_logica(AnalisadorLAParser.Parcela_logicaContext ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#op_logico_1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOp_logico_1(AnalisadorLAParser.Op_logico_1Context ctx);
	/**
	 * Visit a parse tree produced by {@link AnalisadorLAParser#op_logico_2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOp_logico_2(AnalisadorLAParser.Op_logico_2Context ctx);
}