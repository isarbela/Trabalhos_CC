from AnalisadorLAVisitor import AnalisadorLAVisitor
from Escopos import Escopos
from TabelaDeSimbolos import TabelaDeSimbolos, Tipo, Estrutura
from LASemanticoUtils import LASemanticoUtils
from AnalisadorLAParser import AnalisadorLAParser

# Geração de código C após realizar as análises sintática, léxica e semântica
class GeradorCodigoC(AnalisadorLAVisitor) :

    def __init__(self):
        self.tabela = TabelaDeSimbolos(None)
        self.codigo = []

    # Começo da árvore gerada pela análise sintática
    def visitPrograma(self, ctx:AnalisadorLAParser.ProgramaContext):
        self.codigo.append("#include <stdio.h>")
        self.codigo.append("#include <stdlib.h>")
        self.codigo.append("#include <string.h>")
        self.codigo.append("#include <stdbool.h>")

        print("visit programa")
        # Visitar todas as declarações de funções e procedimentos
        for declaracao in ctx.declaracoes().declaracao_global():
            self.visitDeclaracao_global(declaracao)
        # Visitar todas as declarações de tipos, variáveis e constantes
        for declaracao in ctx.declaracoes().declaracao_local():
            self.visitDeclaracao_local(declaracao)

        self.codigo.append("int main() {")
        print("visit p")
        self.visitCorpo(ctx.corpo())
        self.codigo.append("return 0;")
        self.codigo.append("}")
        
        return None

    def visitCorpo(self, ctx: AnalisadorLAParser.CorpoContext):
        # Devemos visitar as declarações de variaveis, tipos e constantes
        for declaracao_local in ctx.declaracao_local():
            self.visitDeclaracao_local(declaracao_local)
        # Visitar os comandos se/senao, leia, imprima, enquanto, etc.
        for cmd in ctx.cmd():
            self.visitCmd(cmd)
            
        return None

    def visitCmd(self, ctx: AnalisadorLAParser.CmdContext):
        if ctx.cmdLeia():
            self.visitCmd_leia(ctx.cmdLeia())
        if ctx.cmdEscreva():
            self.visitCmd_escreva(ctx.cmdEscreva())
        if ctx.cmdAtribuicao():
            self.visitCmd_atribuicao(ctx.cmdAtribuicao())
        if ctx.cmdSe():
            self.visitCmd_se(ctx.cmdSe())
        if ctx.cmdCaso():
            self.visitCmd_caso(ctx.cmdCaso())
        if ctx.cmdPara():
            self.visitCmd_para(ctx.cmdPara())
        if ctx.cmdEnquanto():
            self.visitCmd_enquanto(ctx.cmdEnquanto())
        if ctx.cmdFaca():
            self.visitCmd_faca(ctx.cmdFaca())
        if ctx.cmdChamada():
            self.visitCmd_chamada(ctx.cmdChamada())
        if ctx.cmdRetorne():
            self.visitCmd_retorne(ctx.cmdRetorne())
        return None

    def visitCmd_leia(self, ctx: AnalisadorLAParser.CmdLeiaContext):
        for ident in ctx.identificador():
            tipo_ident = self.tabela.verificar(ident.getText())
            
            if tipo_ident == Tipo.CADEIA:
                self.codigo.append('gets(')
                self.visitIdentificador(ident)
                self.codigo.append(');')
            else:
                self.codigo.append(f'scanf("%{LASemanticoUtils.getMascaraIO(tipo_ident)}", &{ident.getText()});')
        return None

    def visitCmd_escreva(self, ctx: AnalisadorLAParser.CmdEscrevaContext):
        for expressao in ctx.expressao():
            mascaraTipo = LASemanticoUtils.getMascaraIO(LASemanticoUtils.verificarTipoExpr(self.tabela, expressao))
            if self.tabela.existe(expressao.getText()):
                tipo = self.tabela.verificar(expressao.getText())
                mascaraTipo = LASemanticoUtils.getMascaraIO(tipo)
            
            self.codigo.append(f'printf("%{mascaraTipo}", {expressao.getText()});')
        return None

    def visitCmd_atribuicao(self, ctx: AnalisadorLAParser.CmdAtribuicaoContext):
        if ctx.getText().find('^') != -1:
            self.codigo.append('*')
        tipo = self.tabela.verificar(ctx.identificador().getText())
        if tipo == Tipo.CADEIA:
            self.codigo.append('strcpy(')
            self.visitIdentificador(ctx.identificador())
            self.codigo.append(f', {ctx.expressao().getText()});')
        else:
            self.visitIdentificador(ctx.identificador())
            self.codigo.append(f' = {ctx.expressao().getText()};')
        return None

    def visitCmd_se(self, ctx: AnalisadorLAParser.CmdSeContext):
        # Caso primário
        self.codigo.append('if (')
        self.visitExpressao(ctx.expressao())
        self.codigo.append(') {')
        for cmd in ctx.cmd():
            self.visitCmd(cmd)
        self.codigo.append('}')
        # Caso secundário
        if ctx.cmdSenao():
            self.codigo.append('else {')
            for cmd in ctx.cmdSenao().cmd():
                self.visitCmd(cmd)
            self.codigo.append('}')
        return None

    def visitCmd_caso(self, ctx: AnalisadorLAParser.CmdCasoContext):
        self.codigo.append('switch (')
        self.visitExp_aritmetica(ctx.exp_aritmetica())
        self.codigo.append(') {')
        self.visitSelecao(ctx.selecao())
        
        if ctx.cmd():
            self.codigo.append("default:")
            for cmd in ctx.cmd():
                self.visitCmd(cmd)
            self.codigo.append('break;')
        
        self.codigo.append('}')
        return None
    
    def visitSelecao(self, ctx: AnalisadorLAParser.SelecaoContext):
        for item in ctx.item_selecao():
            self.visitItem(item)
        return None
    
    def visitItem(self, ctx: AnalisadorLAParser.Item_selecaoContext):
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
                self.visitCmd(cmd)
            self.codigo.append('break;')
        return None
        
    def visitCmd_para(self, ctx: AnalisadorLAParser.CmdParaContext):
        ident = ctx.IDENT().getText()
        # Cabeçalho do for
        self.codigo.append(f"for ({ident} = ")
        self.visitExp_aritmetica(ctx.exp_aritmetica(0))
        self.codigo.append(f'; {ident} <= ')
        self.visitExp_aritmetica(ctx.exp_aritmetica(1))
        self.codigo.append(f'; {ident}++) ' + '{')
        # Corpo do for
        for cmd in ctx.cmd():
            self.visitCmd(cmd)
        self.codigo.append('}')
        return None

    def visitCmd_enquanto(self, ctx: AnalisadorLAParser.CmdEnquantoContext):
        self.codigo.append("while (")
        self.visitExpressao(ctx.expressao())
        self.codigo.append(") {")
        for cmd in ctx.cmd():
            self.visitCmd(cmd)
        self.codigo.append('}')
        return None

    def visitCmd_faca(self, ctx: AnalisadorLAParser.CmdFacaContext):
        self.codigo.append("do {")
        for cmd in ctx.cmd():
            self.visitCmd(cmd)
        self.codigo.append("} while (")
        self.visitExpressao(ctx.expressao())
        self.codigo.append(');')
        return None

    def visitCmd_retorne(self, ctx: AnalisadorLAParser.CmdRetorneContext):
        self.codigo.append('return ')
        self.visitExpressao(ctx.expressao())
        self.codigo.append(';')
        return None

    def visitCmd_chamada(self, ctx: AnalisadorLAParser.CmdChamadaContext):
        self.codigo.append(f'{ctx.IDENT().getText()} (')
        for expressao, i in zip(ctx.expressao(), range(len(ctx.expressao()))):
            if i > 0:
                self.codigo.append(', ')
            self.visitExpressao(expressao)
        self.codigo.append(');')
        return None

    # Os algoritmos da linguagem LA apresentam declaração global e local
    def visitDeclaracao_global(self, ctx:AnalisadorLAParser.Declaracao_globalContext):
        # Se a funcao for
        if ctx.getText().find("procedimento") != -1:
            self.codigo.append(f"void {ctx.IDENT().getText()} (")
        else:
            tipoC = LASemanticoUtils.getTipoC(ctx.tipo_estendido().getText().replace('^', ''))
            tipoLA = LASemanticoUtils.getTipo(ctx.tipo_estendido().getText())
            self.visitTipo_estendido(ctx.tipo_estendido())
            
            if tipoC == 'char':
                self.codigo.append('[50]')
            
            self.codigo.append(f' {ctx.IDENT().getText()} (')
            self.tabela.adicionar(ctx.IDENT().getText(), tipoLA, Estrutura.FUNCAO)
        
        for variavel in ctx.parametros().parametro():
            self.visitParametro(variavel)
        
        self.codigo.append(") {")
        
        for declaracao_local in ctx.declaracao_local():
            self.visitParametro(declaracao_local)
        
        for cmd in ctx.cmd():
            self.visitCmd(cmd) 
        
        self.codigo.append('}')
        return None
    
    def visitParametro(self, ctx: AnalisadorLAParser.ParametroContext):
        tipoC = LASemanticoUtils.getTipoC(ctx.tipo_estendido().getText().replace('^', ''))
        tipoLA = LASemanticoUtils.getTipo(ctx.tipo_estendido().getText())
        # Criando lista de parâmetros
        for ident, i in zip(ctx.identificador(), range(len(ctx.identificador()))):
            if i > 0:
                self.codigo.append(', ')
            self.visitTipo_estendido(ctx.tipo_estendido())
            self.visitIdentificador(ident)
            if tipoC == 'char':
                self.codigo.append('[50]')
            self.tabela.adicionar(ident.getText(), tipoLA, Estrutura.VAR)
        return None
    
    def visitIdentificador(self, ctx: AnalisadorLAParser.IdentificadorContext):
        self.codigo.append(' ')
        # Criando o identificador completo
        for ident, i in zip(ctx.IDENT(), range(len(ctx.IDENT()))):
            if i > 0:
                self.codigo.append('.')
            self.codigo.append(ident.getText())
        # Tratar a dimensionalidade
        self.visitDimensao(ctx.dimensao())
        return None
    
    def visitDimensao(self, ctx: AnalisadorLAParser.DimensaoContext):
        for exp_aritmetica in ctx.exp_aritmetica():
            self.codigo.append('[')
            # Realizar cálculos na dimensão (se necessário)
            self.visitExp_aritmetica(exp_aritmetica)
            self.codigo.append(']')
        return None
    
    def visitExp_aritmetica(self, ctx: AnalisadorLAParser.Exp_aritmeticaContext):
        self.visitTermo(ctx.termo(0))
        
        for i in range(len(ctx.termo())):
            termo = ctx.termo(i+1)
            self.codigo.append(ctx.op1(i).getText())
            self.visitTermo(termo)
        return None
    
    def visitTermo(self, ctx: AnalisadorLAParser.TermoContext):
        self.visitFator(ctx.fator(0))
        
        for i in range(len(ctx.fator())):
            fator = ctx.fator(i+1)
            self.codigo.append(ctx.op2(i).getText())
            self.visitFator(fator)
        return None
    
    def visitFator(self, ctx: AnalisadorLAParser.FatorContext):
        self.visitParcela(ctx.parcela(0))
        
        for i in range(len(ctx.parcela())):
            fator = ctx.parcela(i+1)
            self.codigo.append(ctx.op3(i).getText())
            self.visitParcela(fator)
        return None
    
    def visitParcela(self, ctx: AnalisadorLAParser.ParcelaContext):
        if ctx.parcela_unario():
            if ctx.op_unario():
                self.codigo.append(ctx.op_unario().getText())
            self.visitParcela_unario(ctx.parcela_unario())
        elif ctx.parcela_nao_unario():
            self.visitParcela_nao_unario(ctx.parcela_nao_unario())
        return None
    
    def visitParcela_nao_unario(self, ctx: AnalisadorLAParser.Parcela_nao_unarioContext):
        self.codigo.append(ctx.getText())
        return None
    
    def visitParcela_unario(self, ctx: AnalisadorLAParser.Parcela_unarioContext):
        if ctx.IDENT():
            self.codigo.append(f'{ctx.IDENT().getText()}(')
            
            for i in range(len(ctx.expressao())):
                self.visitExpressao(ctx.expressao(i))
                if i < len(ctx.expressao() - 1):
                    self.codigo.append(', ')
        else:
            self.codigo.append(ctx.getText())
        return None
    
    def visitExpressao(self, ctx: AnalisadorLAParser.ExpressaoContext):
        if ctx.termo_logico():
            self.visitTermo_logico(ctx.termo_logico(0))
            for i in range(len(ctx.termo_logico())):
                termo = ctx.termo_logico(i+1)
                self.codigo.append(' || ')
                self.visitTermo_logico(termo)
        return None
    
    def visitTermo_logico(self, ctx: AnalisadorLAParser.Termo_logicoContext):
        if ctx.fator_logico():
            self.visitFator_logico(ctx.fator_logico(0))
            for i in range(len(ctx.fator_logico())):
                fator = ctx.fator_logico(i+1)
                self.codigo.append(' && ')
                self.visitFator_logico(fator)
        return None
    
    def visitFator_logico(self, ctx: AnalisadorLAParser.Fator_logicoContext):
        if ctx.getText().startswith('nao'):
            self.codigo.append('!')
        self.visitParcela_logica(ctx.parcela_logica())
        return None
    
    def visitParcela_logica(self, ctx: AnalisadorLAParser.Parcela_logicaContext):
        if ctx.exp_relacional():
            self.visitExp_relacional(ctx.exp_relacional())
        else:
            if ctx.getText() == 'verdadeiro':
                self.codigo.append('true')
            elif ctx.getText() == 'falso':
                self.codigo.append('false')
        return None
    
    def visitExp_relacional(self, ctx: AnalisadorLAParser.Exp_relacionalContext):
        self.visitExp_aritmetica(ctx.exp_aritmetica(0))
        
        for i in range(len(ctx.exp_aritmetica())):
            termo = ctx.exp_aritmetica(i+1)
            # Tratando os casos em que os símbolos de operações diferem da linguagem C
            if ctx.op_relacional().getText() == '=':
                self.codigo.append(' == ')
            elif ctx.op_relacional().getText() == '<>':
                self.codigo.append(' != ')
            else:
                self.codigo.append(ctx.op_relacional().getText())
            
            self.visitExp_aritmetica(termo)
        return None
    
    def visitTipo_estendido(self, ctx: AnalisadorLAParser.Tipo_estendidoContext):
        self.visitTipo_basico_ident(ctx.tipo_basico_ident())
        # Tratando ponteiros
        if ctx.getText().find('^') != -1:
            self.codigo.append('*')
        return None

    def visitTipo_basico_ident(self, ctx: AnalisadorLAParser.Tipo_basico_identContext):
        if ctx.IDENT():
            self.codigo.append(ctx.IDENT().getText())
        else:
            self.codigo.append(LASemanticoUtils.getTipoC(ctx.getText().replace('^', '')))
        return None

    def visitDeclaracao_local(self, ctx: AnalisadorLAParser.Declaracao_localContext):
        print("visit local")
        if ctx.declaracao_var():
            print("visit var")
            self.visitDeclaracao_var(ctx.declaracao_var())
        if ctx.declaracao_const():
            print("visit const")
            self.visitDeclaracao_const(ctx.declaracao_const())
        if ctx.declaracao_tipo():
            print("visit tipo")
            self.visitDeclaracao_tipo(ctx.declaracao_tipo())
        return None

    def visitDeclaracao_var(self, ctx: AnalisadorLAParser.Declaracao_varContext):
        self.visitVariavel(ctx.variavel())
        return None

    def visitDeclaracao_const(self, ctx: AnalisadorLAParser.Declaracao_constContext):
        tipoC = LASemanticoUtils.getTipoC(ctx.tipo_basico().getText())
        tipoLA = LASemanticoUtils.getTipo(ctx.tipo_basico().getText())
        self.tabela.adicionar(ctx.IDENT().getText(), tipoLA, Estrutura.CONST)
        self.codigo.append(f"const {tipoC} {ctx.IDENT().getText()} = ")
        self.visitValor_constante(ctx.valor_constante())
        self.codigo.append(';')
        return None
    
    def visitValor_constante(self, ctx: AnalisadorLAParser.Valor_constanteContext):
        if ctx.getText() == 'falso':
            self.codigo.append('false')
        elif ctx.getText() == 'verdadeiro':
            self.codigo.append('true')
        else:
            self.codigo.append(ctx.getText())
        return None

    def visitDeclaracao_tipo(self, ctx: AnalisadorLAParser.Declaracao_tipoContext):
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
        self.visitTipo(ctx.tipo())
        self.codigo.append(f'{ctx.IDENT()};')
        return None
    
    def visitTipo(self, ctx: AnalisadorLAParser.TipoContext):
        tipoC = LASemanticoUtils.getTipoC(ctx.getText().replace("^", ''))
        ponteiro = ctx.getText().find("^") != -1
        
        if tipoC:
            self.codigo.append(tipoC)
        elif ctx.registro():
            self.visitRegistro(ctx.registro())
        else:
            self.visitTipo_estendido(ctx.tipo_estendido())
        if ponteiro:
            self.codigo.append("*")
        self.codigo.append(" ")
        return None
    
    def visitRegistro(self, ctx: AnalisadorLAParser.RegistroContext):
        self.codigo.append("struct {")
        for variavel in ctx.variavel():
            self.visitVariavel(variavel)
        self.codigo.append('}')
        return None
    
    def visitVariavel(self, ctx: AnalisadorLAParser.VariavelContext):
        tipoC = LASemanticoUtils.getTipoC(ctx.tipo().getText().replace("^", ''))
        tipoLA = LASemanticoUtils.getTipo(ctx.tipo().getText())
        print("variavel", tipoC, tipoLA)
        for ident in ctx.identificador():
            print("pront")
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
            print("oi")
            self.visitTipo(ctx.tipo())
            print('ok')
            self.visitIdentificador(ident)

            if tipoC == 'char':
                self.codigo.append("[50]")
            self.codigo.append(';')
        return None
