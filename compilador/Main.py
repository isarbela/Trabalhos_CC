import sys
from antlr4 import *
from AnalisadorLALexer import AnalisadorLALexer
from AnalisadorLAParser import AnalisadorLAParser
from AnalisadorLALexerErrorListener import AnalisadorLALexerErrorListener
from AnalisadorLAParserErrorListener import AnalisadorLAParserErrorListener
from LASemantico import LASemantico
from LASemanticoUtils import LASemanticoUtils
from GeradorDeCodigoC import GeradorCodigoC

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

    arvore = parser.programa()
    # Tratamento de erros em python
    # Alterando os tratadores padrões de erro para os que criamos
    lexer.removeErrorListeners()
    lexer.addErrorListener(AnalisadorLALexerErrorListener())

    parser.removeErrorListeners()
    parser.addErrorListener(AnalisadorLAParserErrorListener())

    try:
        # Executa o parser para análise sintática
        laSemantico = LASemantico()

        laSemantico.visitPrograma(arvore)
        for erro in LASemanticoUtils.errosSemanticos:
            output_stream.write(erro + "\n")
        
        print(len(LASemanticoUtils.errosSemanticos))
        if len(LASemanticoUtils.errosSemanticos) == 0:
            codigo_c = GeradorCodigoC()
            print('abc')
            codigo_c.visitPrograma(arvore)
            print('def')
            print(codigo_c.codigo)
            for instrucoes in codigo_c.codigo:
                output_stream.write(f"{instrucoes}\n")
        else:
            output_stream.write("Fim da compilacao\n")
    except Exception as e:
        # Deteccao de erro sintatico e lexico
        # gracas aos listeners que implementamos
        output_stream.write(str(e))
        output_stream.write("\nFim da compilacao\n")
    output_stream.close()
 
if __name__ == '__main__':
    main(sys.argv)