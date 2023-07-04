
from collections import deque

class Escopos():
    def __init__ (self, pilhaDeTabelas: deque):
        self.pilhaDeTabelas = pilhaDeTabelas
        criarNovoEscopo()

    def criarNovoEscopo(self):
        self.pilhaDeTabelas.append(TabelaDeSimbolos())

    def obterEscopoAtual(self) -> TabelaDeSimbolos:
        self.pilhaDeTabelas[-1]

    def abandonarEscopo(self) :
        self.pilhaDeTabelas.pop()
