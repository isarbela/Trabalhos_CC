import sys
from antlr4 import *
from AnalisadorLALexer import AnalisadorLALexer
from AnalisadorLAParser import AnalisadorLAParser
from AnalisadorLALexerErrorListener import AnalisadorLALexerErrorListener
from AnalisadorLAParserErrorListener import AnalisadorLAParserErrorListener

# Código responsável por ler os tokens gerados pela analisador léxico e salvar em um arquivo
def main(argv):

    # Recebendo o arquivo de entrada
    input_stream = FileStream(argv[1], encoding='utf-8')
    # Arquivo de saida
    output_stream = open(argv[2], 'w')
    # Gerando os tokens
    lexer = AnalisadorLALexer(input_stream)
    # Gerando o parser (Analisador sintático)
    tokens = CommonTokenStream(lexer)
    parser = AnalisadorLAParser(tokens)

    # Tratamento de erros em python
    # Alterando os tratadores padrões de erro para os que criamos
    lexer.removeErrorListeners()
    lexer.addErrorListener(AnalisadorLALexerErrorListener())

    parser.removeErrorListeners()
    parser.addErrorListener(AnalisadorLAParserErrorListener())

    

    try:
        parser.programa()
    except Exception as e:
        output_stream.write(str(e))
        output_stream.write("\nFim da compilacao\n")
        # t = lexer.nextToken()
        # if t.type == Token.EOF:
        #     return
        # elif AnalisadorLexer.symbolicNames[t.type] == "ERRO":
        #     output_stream.write(f"Linha {t.line}: {t.text} - simbolo nao identificado\n")
        #     return
        # elif AnalisadorLexer.symbolicNames[t.type] == "COMENTARIO_NAO_FECHADO":
        #     output_stream.write(f"Linha {t.line}: comentario nao fechado\n")
        #     return
        # elif AnalisadorLexer.symbolicNames[t.type] == "CADEIA_NAO_FECHADA":
        #     output_stream.write(f"Linha {t.line}: cadeia literal nao fechada\n")
        #     return
        # elif AnalisadorLexer.symbolicNames[t.type] == "SELF":
        #     output_stream.write(f"<'{t.text}','{t.text}'>\n")
        # else:
        #     output_stream.write(f"<'{t.text}',{AnalisadorLexer.symbolicNames[t.type]}>\n")
    output_stream.close()
    
 
if __name__ == '__main__':
    main(sys.argv)