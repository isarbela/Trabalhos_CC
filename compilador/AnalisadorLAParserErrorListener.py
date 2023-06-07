from antlr4.error.ErrorListener import ErrorListener

# Implementacão da interface do antlr error listener.
class AnalisadorLAParserErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # A documentação https://www.antlr.org/api/Java/org/antlr/v4/runtime/ANTLRErrorListener.html
        # explica o que cada parâmetro significa.
        # offendingSymbol - The offending token in the input token stream, unless recognizer 
        # is a lexer (then it's null). 
        # If no viable alternative error, e has token at which we started production for the decision.
        l = offendingSymbol.line
        t = offendingSymbol.text # Similar ao getText() do exemplo em java.
        # Se o token for EOF alteramos para 'EOF'.
        if t == '<EOF>':
            t = 'EOF'
        # Utilizamos exception para escrever nossas mensagens de erro e parar a execução do programa.
        raise Exception(f'Linha {line}: erro sintatico proximo a {t}')
