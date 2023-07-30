from AnalisadorLAVisitor import AnalisadorLAVisitor
from Escopos import Escopos
from TabelaDeSimbolos import TabelaDeSimbolos, Tipo, Estrutura
from LASemanticoUtils import LASemanticoUtils
from AnalisadorLAParser import AnalisadorLAParser
# from compilador.AnalisadorLAParser import AnalisadorLAParser
from Escopos import Escopos
from TabelaDeSimbolos import TabelaDeSimbolos, Tipo, Estrutura
from LASemanticoUtils import LASemanticoUtils, debug
from AnalisadorLAParser import AnalisadorLAParser
# from compilador.AnalisadorLAParser import AnalisadorLAParser

# Geração de código C após realizar as análises sintática, léxica e semântica
class GeradorCodigoC(AnalisadorLAVisitor) :

    def __init__(self):
        self.tabela = TabelaDeSimbolos(None)
        self.codigo = []

    # Começo da árvore gerada pela análise sintática
    def visit_programa(self, ctx:AnalisadorLAParser.ProgramaContext):
        self.codigo.append("#include <stdio.h>")
        self.codigo.append("#include <stdlib.h>")
        self.codigo.append("#include <string.h>")
        self.codigo.append("#include <stdbool.h>")

        # Visitar todas as declarações de funções e procedimentos
        for declaracao in ctx.declaracoes().declaracao_global():
            self.visit_declaracao_global(declaracao)
        # Visitar todas as declarações de tipos, variáveis e constantes
        for declaracao in ctx.declaracoes().declaracao_local():
            self.visit_declaracao_local(declaracao)

        self.codigo.append("int main() {")
        self.visit_corpo(ctx.corpo())
        self.codigo.append("return 0;")
        self.codigo.append("}")

    def visit_corpo(self, ctx: AnalisadorLAParser.CorpoContext):
        # Devemos visitar as declarações de variaveis, tipos e constantes
        for declaracao_local in ctx.declaracao_local():
            self.visit_declaracao_local(declaracao_local)
        # Visitar os comandos se/senao, leia, imprima, enquanto, etc.
        for cmd in ctx.cmd():
            self.visit_cmd(cmd)

    def visit_cmd(self, ctx: AnalisadorLAParser.CmdContext):
        if ctx.cmdLeia():
            self.visit_cmd_leia(ctx.cmdLeia())
        if ctx.cmdEscreva():
            self.visit_cmd_escreva(ctx.cmdEscreva())
        if ctx.cmdAtribuicao():
            self.visit_cmd_atribuicao(ctx.cmdAtribuicao())
        if ctx.cmdSe():
            self.visit_cmd_se(ctx.cmdSe())
        if ctx.cmdCaso():
            self.visit_cmd_caso(ctx.cmdCaso())
        if ctx.cmdPara():
            self.visit_cmd_para(ctx.cmdPara())
        if ctx.cmdEnquanto():
            self.visit_cmd_enquanto(ctx.cmdEnquanto())
        if ctx.cmdFaca():
            self.visit_cmd_faca(ctx.cmdFaca())
        if ctx.cmdChamada():
            self.visit_cmd_chamada(ctx.cmdChamada())
        if ctx.cmdRetorne():
            self.visit_cmd_retorne(ctx.cmdRetorne())

    def visit_cmd_caso(self, ctx: AnalisadorLAParser.CmdCasoContext):
        self.codigo.append('switch (')
        self.visit_exp_aritmetica(ctx.exp_aritmetica())
        self.codigo.append(') {')
        self.visit_selecao(ctx.selecao())
        
        if ctx.cmd():
            self.codigo.append("default:")
            for cmd in ctx.cmd():
                self.visit_cmd(cmd)
            self.codigo.append('break;')
        
        self.codigo.append('}')
    
    def visit_selecao(self, ctx: AnalisadorLAParser.SelecaoContext):
        for item in ctx.item_selecao():
            self.visit_item(item)
    
    def visit_item(self, ctx: AnalisadorLAParser.Item_selecaoContext):
        intervalo = ctx.constantes().getText().split('..')
        if len(intervalo) > 0:
            first = intervalo[0]
        else:
            first = ctx.constantes().getText()
        if len(intervalo) > 1:
            last = intervalo[1]
        else:
            last = intervalo[0]
        
        for i in range(int(first), int(last) + 1):
            self.codigo.append(f"case {i} :")
            for cmd in ctx.cmd():
                self.visit_cmd(cmd)
            self.codigo.append('break;')
        
    def visit_cmd_para(self, ctx: AnalisadorLAParser.CmdParaContext):
        ident = ctx.IDENT().getText()
        # Cabeçalho do for
        self.codigo.append(f"for ({ident} = ")
        self.visit_exp_aritmetica(ctx.exp_aritmetica(0))
        self.codigo.append(f'; {ident} <= ')
        self.visit_exp_aritmetica(ctx.exp_aritmetica(1))
        self.codigo.append(f'; {ident}++) ' + '{')
        # Corpo do for
        for cmd in ctx.cmd():
            self.visit_cmd(cmd)
        self.codigo.append('}')

    def visit_cmd_enquanto(self, ctx: AnalisadorLAParser.CmdEnquantoContext):
        self.codigo.append("while (")
        self.visit_expressao(ctx.expressao())
        self.codigo.append(") {")
        for cmd in ctx.cmd():
            self.visit_cmd(cmd)
        self.codigo.append('}')

    def visit_cmd_faca(self, ctx: AnalisadorLAParser.CmdFacaContext):
        self.codigo.append("do {")
        for cmd in ctx.cmd():
            self.visit_cmd(cmd)
        self.codigo.append("} while (")
        self.visit_expressao(ctx.expressao())
        self.codigo.append(');')

    def visit_cmd_retorne(self, ctx: AnalisadorLAParser.CmdRetorneContext):
        self.codigo.append('return ')
        self.visit_expressao(ctx.expressao())
        self.codigo.append(';')

    def visit_cmd_chamada(self, ctx: AnalisadorLAParser.CmdChamadaContext):
        self.codigo.append(f'{ctx.IDENT().getText()} (')
        for expressao, i in zip(ctx.expressao(), range(len(ctx.expressao()))):
            if i > 0:
                self.codigo.append(', ')
            self.visit_expressao(expressao)
        self.codigo.append(');')

    # Os algoritmos da linguagem LA apresentam declaração global e local
    def visit_declaracao_global(self, ctx:AnalisadorLAParser.Declaracao_globalContext):
        # Se a funcao for
        if ctx.getText().find("procedimento") != -1:
            self.codigo.append(f"void {ctx.IDENT().getText()} (")
        else:
            tipoC = LASemanticoUtils.getTipoC(ctx.tipo_estendido().getText().replace('^', ''))
            tipoLA = LASemanticoUtils.getTipo(ctx.tipo_estendido().getText())
            self.visit_tipo_estendido(ctx.tipo_estendido())
            
            if tipoC == 'char':
                self.codigo.append('[50]')
            
            self.codigo.append(f' {ctx.IDENT().getText()} (')
            self.tabela.adicionar(ctx.IDENT().getText(), tipoLA, Estrutura.FUNCAO)
        
        for variavel in ctx.parametros().parametro():
            self.visit_parametro(variavel)
        
        self.codigo.append(") {")
        
        for declaracao_local in ctx.declaracao_local():
            self.visit_parametro(declaracao_local)
        
        for cmd in ctx.cmd():
            self.visit_cmd(cmd) 
        
        self.codigo.append('}')
        
    def visit_parametro(self, ctx: AnalisadorLAParser.ParametroContext):
        tipoC = LASemanticoUtils.getTipoC(ctx.tipo_estendido().getText().replace('^', ''))
        tipoLA = LASemanticoUtils.getTipo(ctx.tipo_estendido().getText())
        # Criando lista de parâmetros
        for ident, i in zip(ctx.identificador(), range(len(ctx.identificador()))):
            if i > 0:
                self.codigo.append(', ')
            self.visit_tipo_estendido(ctx.tipo_estendido())
            self.visit_identificador(ident)
            if tipoC == 'char':
                self.codigo.append('[50]')
            self.tabela.adicionar(ident.getText(), tipoLA, Estrutura.VAR)
    
    def visit_identificador(self, ctx: AnalisadorLAParser.IdentificadorContext):
        self.codigo.append(' ')
        # Criando o identificador completo
        for ident, i in zip(ctx.IDENT(), len(ctx.IDENT())):
            if i > 0:
                self.codigo.append('.')
            self.codigo.append(ident.getText())
        # Tratar a dimensionalidade
        self.visit_dimensao(ctx.dimensao())
    
    def visit_dimensao(self, ctx: AnalisadorLAParser.DimensaoContext):
        for exp_aritmetica in ctx.exp_aritmetica():
            self.codigo.append('[')
            # Realizar cálculos na dimensão (se necessário)
            self.visit_exp_aritmetica(exp_aritmetica)
            self.codigo.append(']')
    
    def visit_exp_aritmetica(self, ctx: AnalisadorLAParser.Exp_aritmeticaContext):
        self.visit_termo(ctx.termo(0))
        
        for i in range(len(ctx.termo())):
            termo = ctx.termo(i+1)
            self.codigo.append(ctx.op1(i).getText())
            self.visit_termo(termo)
    
    def visit_termo(self, ctx: AnalisadorLAParser.TermoContext):
        self.visit_fator(ctx.fator(0))
        
        for i in range(len(ctx.fator())):
            fator = ctx.fator(i+1)
            self.codigo.append(ctx.op2(i).getText())
            self.visit_fator(fator)
    
    def visit_fator(self, ctx: AnalisadorLAParser.FatorContext):
        self.visit_parcela(ctx.parcela(0))
        
        for i in range(len(ctx.parcela())):
            fator = ctx.parcela(i+1)
            self.codigo.append(ctx.op3(i).getText())
            self.visit_parcela(fator)
    
    def visit_parcela(self, ctx: AnalisadorLAParser.ParcelaContext):
        if ctx.parcela_unario():
            if ctx.op_unario():
                self.codigo.append(ctx.op_unario().getText())
            self.visit_parcela_unario(ctx.parcela_unario())
        elif ctx.parcela_nao_unario():
            self.visit_parcela_nao_unario(ctx.parcela_nao_unario())
    
    def visit_parcela_nao_unario(self, ctx: AnalisadorLAParser.Parcela_nao_unarioContext):
        self.codigo.append(ctx.getText())
    
    def visit_parcela_unario(self, ctx: AnalisadorLAParser.Parcela_unarioContext):
        if ctx.IDENT():
            self.codigo.append(f'{ctx.IDENT().getText()}(')
            
            for i in range(len(ctx.expressao())):
                self.visit_expressao(ctx.expressao(i))
                if i < len(ctx.expressao() - 1):
                    self.codigo.append(', ')
        else:
            self.codigo.append(ctx.getText())
    
    def visit_expressao(self, ctx: AnalisadorLAParser.ExpressaoContext):
        if ctx.termo_logico():
            self.visit_termo_logico(ctx.termo_logico(0))
            for i in range(len(ctx.termo_logico())):
                termo = ctx.termo_logico(i+1)
                self.codigo.append(' || ')
                self.visit_termo_logico(termo)
    
    def visit_termo_logico(self, ctx: AnalisadorLAParser.Termo_logicoContext):
        if ctx.fator_logico():
            self.visit_fator_logico(ctx.fator_logico(0))
            for i in range(len(ctx.fator_logico())):
                fator = ctx.fator_logico(i+1)
                self.codigo.append(' && ')
                self.visit_fator_logico(fator)
    
    def visit_fator_logico(self, ctx: AnalisadorLAParser.Fator_logicoContext):
        if ctx.getText().startswith('nao'):
            self.codigo.append('!')
        self.visit_parcela_logica(ctx.parcela_logica())
    
    def visit_parcela_logica(self, ctx: AnalisadorLAParser.Parcela_logicaContext):
        if ctx.exp_relacional():
            self.visit_exp_relacional(ctx.exp_relacional())
        else:
            if ctx.getText() == 'verdadeiro':
                self.codigo.append('true')
            elif ctx.getText() == 'falso':
                self.codigo.append('false')
    
    def visit_exp_relacional(self, ctx: AnalisadorLAParser.Exp_relacionalContext):
        self.visit_exp_aritmetica(ctx.exp_aritmetica(0))
        
        for i in range(len(ctx.exp_aritmetica())):
            termo = ctx.exp_aritmetica(i+1)
            # Tratando os casos em que os símbolos de operações diferem da linguagem C
            if ctx.op_relacional().getText() == '=':
                self.codigo.append(' == ')
            elif ctx.op_relacional().getText() == '<>':
                self.codigo.append(' != ')
            else:
                self.codigo.append(ctx.op_relacional().getText())
            
            self.visit_exp_aritmetica(termo)
    
    def visit_tipo_estendido(self, ctx: AnalisadorLAParser.Tipo_estendidoContext):
        self.visit_tipo_basico_ident(ctx.tipo_basico_ident())
        # Tratando ponteiros
        if ctx.getText().find('^') != -1:
            self.codigo.append('*')

    def visit_tipo_basico_ident(self, ctx: AnalisadorLAParser.Tipo_basico_identContext):
        if ctx.IDENT():
            self.codigo.append(ctx.IDENT().getText())
        else:
            self.codigo.append(LASemanticoUtils.getTipoC(ctx.getText().replace('^', '')))

    def visit_declaracao_local(self, ctx: AnalisadorLAParser.Declaracao_localContext):
        if ctx.declaracao_var():
            self.visit_declaracao_var(ctx.declaracao_var())
        if ctx.declaracao_const():
            self.visit_declaracao_const(ctx.declaracao_const())
        if ctx.declaracao_tipo():
            self.visit_declaracao_tipo(ctx.declaracao_tipo())

    def visit_declaracao_var(self, ctx: AnalisadorLAParser.Declaracao_varContext):
        self.visit_variavel(ctx.variavel())

    def visit_declaracao_const(self, ctx: AnalisadorLAParser.Declaracao_constContext):
        tipoC = LASemanticoUtils.getTipoC(ctx.tipo_basico().getText())
        tipoLA = LASemanticoUtils.getTipo(ctx.tipo_basico().getText())
        self.tabela.adicionar(ctx.IDENT().getText(), tipoLA, Estrutura.CONST)
        self.codigo.append(f"const {tipoC} {ctx.IDENT().getText()} = ")
        self.visit_valor_constante(ctx.valor_constante())
        self.codigo.append(';')
    
    def visit_valor_constante(self, ctx: AnalisadorLAParser.Valor_constanteContext):
        if ctx.getText() == 'falso':
            self.codigo.append('false')
        elif ctx.getText() == 'verdadeiro':
            self.codigo.append('true')
        else:
            self.codigo.append(ctx.getText())

    def visit_declaracao_tipo(self, ctx: AnalisadorLAParser.Declaracao_tipoContext):
        self.codigo.append('typedef ')
        tipo = LASemanticoUtils.getTipo(ctx.tipo().getText())
        # Tratando o caso de declaração de structs
        if ctx.tipo.getText().find('registro') != -1:
            for variavel in ctx.tipo().registro().variavel():
                for ident in variavel.identificador():
                    tipo_var = LASemanticoUtils.getTipo(variavel.tipo().getText())
                    self.tabela.adicionar(f"{ctx.IDENT().getText()}.{ident.getText()}", tipo_var, Estrutura.VAR)
                    nova_entrada = TabelaDeSimbolos.EntradaTabelaSimbolos(ident.getText(), tipo_var, Estrutura.TIPO)
                    self.tabela.adicionarTipo(ctx.IDENT().getText(), nova_entrada)
        
        self.tabela.adicionar(ctx.IDENT().getText(), tipo, Estrutura.VAR)
        self.visit_tipo(ctx.tipo())
        self.codigo.append(f'{ctx.IDENT()};')
    
    def visit_tipo(self, ctx: AnalisadorLAParser.TipoContext):
        tipoC = LASemanticoUtils.getTipoC(ctx.getText().replace("^", ''))
        ponteiro = ctx.getText().find("^") != 1
        
        if tipoC:
            self.codigo.append(tipoC)
        elif ctx.registro():
            self.visit_registro(ctx.registro())
        else:
            self.visit_tipo_estendido(ctx.tipo_estendido())
        if ponteiro:
            self.codigo.append("*")
        self.codigo.append(" ")
    
    def visit_registro(self, ctx: AnalisadorLAParser.RegistroContext):
        self.codigo.append("struct {")
        for variavel in ctx.variavel():
            self.visit_variavel(variavel)
        self.codigo.append('}')
    
    def visit_variavel(self, ctx: AnalisadorLAParser.VariavelContext):
        tipoC = LASemanticoUtils.getTipoC(ctx.getText().replace("^", ''))
        tipoLA = LASemanticoUtils.getTipo(ctx.tipo().getText())
        
        for ident in ctx.identificador():
            if ctx.tipo().getText().find('registro') != -1:
                for variavel in ctx.tipo().registro().variavel():
                    for var_ident in variavel.identificador():
                        tipo_var = LASemanticoUtils.getTipo(variavel.tipo().getText())
                        self.tabela.adicionar(f"{ident.getText()}.{var_ident.getText()}", tipo_var, Estrutura.VAR)
            elif tipoC and tipoLA:
                entradas = self.tabela.verificarTipo(ctx.tipo().getText())
                if entradas:
                    for entrada in entradas:
                        self.tabela.adicionar(f"{ident.getText()}.{entrada.nome}", entrada.tipo, Estrutura.VAR)
            # Tratar o caso de vetores
            if ident.getText().find('[') != -1:
                inicio = ident.getText().index('[')
                fim = ident.getText().index(']')
                
                if fim - inicio == 2:
                    tamanho = str(ident.getText()[inicio + 1])
                else:
                    tamanho = ident.getText().substring(inicio + 1, fim - 1)
                
                nome = ident.IDENT()[0].getText()
                for i in range(int(tamanho)):
                    self.tabela.adicionar(f'{nome}[{i}]', tipoLA, Estrutura.VAR)
            else:
                self.tabela.adicionar(ident.getText(), tipoLA, Estrutura.VAR)
            
            self.visit_tipo(ctx.tipo())
            self.visit_identificador(ident)

            if tipoC == 'char':
                self.codigo.append("[50]")
            self.codigo.append(';')
