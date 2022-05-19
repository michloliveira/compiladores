from analizador_lexico import AnalizadorLexico
from analizador_sintatico import AnalizadorSintatico
from gerador_codigo_intermediario import GeradorCodigoIntermediario

arq = open("code.txt","r")
texto = arq.readlines()
#print(texto)
arq.close()

lexer = AnalizadorLexico(texto)
lexer.tokenizar(texto)
lexer.imprimir_lista_tokens()
lexer.imprimir_tabela_simbolos()
parser = AnalizadorSintatico(lexer.tokens, lexer.tabela_simbolos)
tradutor = parser.start() #tradutor recebe uma array de instrucoes

for i in range(len(tradutor)):
    for j in range(len(tradutor[i])):
        print(tradutor[i][j].lexema, end=" ")
    print("")