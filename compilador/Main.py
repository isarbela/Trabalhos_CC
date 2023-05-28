import sys
from antlr4 import *
from AnalisadorLexer import AnalisadorLexer

# Código responsável por ler os tokens gerados pela analisador léxico e salvar em um arquivo
def main(argv):

    # Recebendo o arquivo de entrada
    input_stream = FileStream(argv[1], encoding='utf-8')
    # Arquivo de saida
    output_stream = open(argv[2], 'w')
    # Gerando os tokens
    lexer = AnalisadorLexer(input_stream)

    # Leitura dos tokens e salvamento em arquivo
    while True:
    # Se for um erro léxico, imprime o lexema e a linha do erro, indicando 
    # o erro encontrado, podendo ser comentário não fechado, cadeia literal 
    # não fechada ou símbolo não identificado.
    # Se for um SELF (Palavra-chave) imprime o lexema nos dois campos do token
    # Se for outro token, imprime o lexema e o tipo do token.
    # A condição de parada é o fim do arquivo (EOF).
        
        t = lexer.nextToken()
        if t.type == Token.EOF:
            break
        elif AnalisadorLexer.symbolicNames[t.type] == "ERRO":
            output_stream.write(f"Linha {t.line}: {t.text} - simbolo nao identificado\n")
            break
        elif AnalisadorLexer.symbolicNames[t.type] == "COMENTARIO_NAO_FECHADO":
            output_stream.write(f"Linha {t.line}: comentario nao fechado\n")
            break
        elif AnalisadorLexer.symbolicNames[t.type] == "CADEIA_NAO_FECHADA":
            output_stream.write(f"Linha {t.line}: cadeia literal nao fechada\n")
            break
        elif AnalisadorLexer.symbolicNames[t.type] == "SELF":
            output_stream.write(f"<'{t.text}','{t.text}'>\n")
        else:
            output_stream.write(f"<'{t.text}',{AnalisadorLexer.symbolicNames[t.type]}>\n")
        
    output_stream.close()
    
 
if __name__ == '__main__':
    main(sys.argv)