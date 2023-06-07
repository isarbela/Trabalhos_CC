from antlr4.error.ErrorListener import ErrorListener

# Implementamos a interface ErrorListener para tratamento de erros léxicos
# https://github.com/antlr/antlr4/blob/master/runtime/Python3/src/antlr4/error/ErrorListener.py
# https://www.antlr.org/api/Java/org/antlr/v4/runtime/BaseErrorListener.html#syntaxError(org.antlr.v4.runtime.Recognizer,java.lang.Object,int,int,java.lang.String,org.antlr.v4.runtime.RecognitionException)
class AnalisadorLALexerErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Analisa o tipo de erro e lança para LexorError.
        # Através da variável "e" conseguimos recuperar o simbolo de entrada para analisar o erro (N SEI).
        # https://www.antlr.org/api/Java/org/antlr/v4/runtime/RecognitionException.html
        # https://www.antlr3.org/api/Python/classantlr3_1_1_recognition_exception.html
        # https://www.antlr3.org/api/Python/antlr3_8py-source.html#l00224
        # print("e = ", e)
        # print("recognizer = ", recognizer)
        # print("offendingSymbol = ", offendingSymbol)
        # print("msg = ", msg)
        # print("------------------  FIM  ------------------")
        # N SEI FAZER
        # talvez fazer um parse na variavel e para pegar o caractere e fazer uma comparacao
        pass