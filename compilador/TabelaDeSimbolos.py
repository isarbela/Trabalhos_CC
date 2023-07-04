from enum import Enum

class TabelaDeSimbolos():

    def __init(self):
        self.tabela = Dict[str, Tipo]

    class EntradaTabelaSimbolos() :

        def __init__(self, nome, tipo) :
            self.nome = nome
            self.tipo =  tipo
    
    def adicionar(self, nome : str, tipo: Tipo) :
        self.tabela[nome] = tipo
    
    
    def existe(self, nome: str) -> bool :
        return self.tabela.get(nome) != None
    
    
    def verificar(self, nome : str) :
        return self.tabela.get(nome)
    
    
class Tipo (Enum) :
    NUM_INT = "inteiro"
    NUM_REAL = "real"
    CADEIA  = "cadeia"