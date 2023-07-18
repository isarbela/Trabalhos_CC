from enum import Enum


class Tipo(Enum):
    NUM_INT = "inteiro"
    NUM_REAL = "real"
    CADEIA  = "cadeia"
    INVALIDO = "invalido"
    TIPO = "tipo"
    LOGICO = "logico"
    PONTEIRO = "ponteiro"
    REGISTRO = "registro"
    VOID = "void"

class Estrutura(Enum):
    VAR = "var"
    CONST = "const"
    PROCEDIMENTO = "procedimento"
    FUNCAO = "funcao"
    TIPO = "tipo"

class TabelaDeSimbolos():
    def __init__(self, tipo: Tipo):
        self.tabela: dict[str, Tipo] = {}
        self.tabelaTipo: dict[str, list] = {}
        self.tipo = tipo

    class EntradaTabelaSimbolos():
        def __init__(self, nome, tipo, estrutura):
            self.nome = nome
            self.tipo =  tipo
            self.estrutura = estrutura

    def adicionar(self, nome : str, tipo: Tipo, estrutura: Estrutura):
        entrada = TabelaDeSimbolos.EntradaTabelaSimbolos(nome, tipo, estrutura)
        self.tabela[entrada.nome] = entrada.tipo
    
    def adicionarTipo(self, nomeTipo: str, entradaTabelaSimbolos: EntradaTabelaSimbolos):
        if nomeTipo in self.tabelaTipo:
            self.tabelaTipo.get(nomeTipo).append(entradaTabelaSimbolos)
        else:
            self.tabelaTipo[nomeTipo] = [ entradaTabelaSimbolos ]
    
    def existe(self, nome: str) -> bool:
        return self.tabela.get(nome) != None
    
    def verificar(self, nome : str):
        return self.tabela.get(nome)

    def verificarTipo(self, nome: str):
        return self.tabelaTipo.get(nome)