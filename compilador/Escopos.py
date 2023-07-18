
from collections import deque
from TabelaDeSimbolos import TabelaDeSimbolos, Tipo

class Escopos():
    def __init__ (self, tipo: Tipo):
        self.pilhaDeTabelas: deque[TabelaDeSimbolos] = deque()
        self.criarNovoEscopo(tipo)

    def criarNovoEscopo(self, tipo: Tipo):
        self.pilhaDeTabelas.append(TabelaDeSimbolos(tipo))

    def obterEscopoAtual(self) -> TabelaDeSimbolos:
        return self.pilhaDeTabelas[-1]

    def abandonarEscopo(self):
        self.pilhaDeTabelas.pop()

    def percorrerEscoposAninhados(self) -> deque[TabelaDeSimbolos]:
        return self.pilhaDeTabelas
