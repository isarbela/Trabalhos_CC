
from collections import deque
from TabelaDeSimbolos import TabelaDeSimbolos

class Escopos():
    def __init__ (self):
        self.pilhaDeTabelas: deque[TabelaDeSimbolos] = deque()
        self.criarNovoEscopo()

    def criarNovoEscopo(self):
        self.pilhaDeTabelas.append(TabelaDeSimbolos())

    def obterEscopoAtual(self) -> TabelaDeSimbolos:
        self.pilhaDeTabelas[-1]

    def abandonarEscopo(self):
        self.pilhaDeTabelas.pop()

    def percorrerEscoposAninhados(self) -> deque[TabelaDeSimbolos]:
        return self.pilhaDeTabelas
