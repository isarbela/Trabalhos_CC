grammar AnalisadorLA;


// Detecção de números reais e inteiros.
// A ordem importa.
NUM_INT	: /*('+'|'-')?*/('0'..'9')+
 	;
NUM_REAL : /*('+'|'-')?*/('0'..'9')+ ('.' ('0'..'9')+)?
 	;

// Variáveis
IDENT : ('a'..'z'|'A'..'Z' | '_') ('_' | 'a'..'z'|'A'..'Z'|'0'..'9')*
	;

// Cadeia de caracteres são identificadas através do operador de aspas
// duplas, diferentemente do exemplo de aula que era aspas simples.
CADEIA 	: '"' ( ESC_SEQ | ~('"'|'\\' | '\n') )* '"'
	;
fragment
ESC_SEQ	: '\\"';

// Comentários são identificados através de chaves e fecha chaves.
COMENTARIO
    :   ('{' ~('\n'|'\r' | '}')* '\r'?  '}') -> skip
    ;

// Espaços em branco são ignorados.
WS  :   ( ' '
        | '\t'
        | '\r'
        | '\n'
        ) -> skip
    ;

// Regras de produção da gramática LA.
// Basicamente retiramos do documento Gramatica_LA.pdf disponibilizado no Classroom
// Com algumas modificações para melhorar a leitura e evitar regras desnecessárias.
programa: declaracoes 'algoritmo' corpo 'fim_algoritmo' EOF;
declaracoes: (declaracao_local | declaracao_global)*;
declaracao_local: (declaracao_var | declaracao_const | declaracao_tipo);
declaracao_var: 'declare' variavel;
declaracao_const: 'constante' IDENT ':' tipo_basico '=' valor_constante;
declaracao_tipo: 'tipo' IDENT ':' tipo;
variavel: identificador (',' identificador)* ':' tipo;
identificador: IDENT ('.' IDENT)* dimensao;
dimensao: ('[' exp_aritmetica ']')*;
tipo: registro | tipo_estendido;
tipo_basico: 'literal' | 'inteiro' | 'real' | 'logico';
tipo_basico_ident: tipo_basico | IDENT;
tipo_estendido: '^'? tipo_basico_ident;
valor_constante: CADEIA | NUM_INT | NUM_REAL | 'verdadeiro' | 'falso';
registro: 'registro' variavel* 'fim_registro';
declaracao_global:
    'procedimento' IDENT '(' parametros? ')' corpo 'fim_procedimento'
    | 'funcao' IDENT '(' parametros? ')' ':' tipo_estendido corpo 'fim_funcao';
corpo: declaracao_local* cmd*;
parametro: 'var'? identificador (',' identificador)* ':' tipo_estendido;
parametros: parametro (',' parametro)*;
cmd: cmdLeia | cmdEscreva | cmdSe | cmdCaso | cmdPara | cmdEnquanto | cmdFaca
    | cmdAtribuicao | cmdChamada | cmdRetorne;
cmdLeia: 'leia' '(' '^'? identificador (',' '^'? identificador)* ')';
cmdEscreva: 'escreva' '(' expressao (',' expressao)* ')';
cmdSe: 'se' expressao 'entao' (cmd)* cmdSenao? 'fim_se';
cmdSenao: 'senao' (cmd)*;
cmdCaso: 'caso' exp_aritmetica 'seja' selecao ('senao' cmd*)? 'fim_caso';
cmdPara: 'para' IDENT '<-' exp_aritmetica 'ate' exp_aritmetica 'faca' cmd* 'fim_para';
cmdEnquanto: 'enquanto' expressao 'faca' cmd* 'fim_enquanto';
cmdFaca: 'faca' cmd* 'ate' expressao;
cmdAtribuicao: '^'? identificador '<-' expressao;
cmdChamada: IDENT '(' expressao (',' expressao)* ')';
cmdRetorne: 'retorne' expressao;
selecao: item_selecao*;
item_selecao: constantes ':' cmd*;
constantes: numero_intervalo (',' numero_intervalo)*;
numero_intervalo: op_unario? NUM_INT ( '..' op_unario? NUM_INT)?;
op_unario: '-';
exp_aritmetica: termo (op1 termo)*;
termo: fator (op2 fator)*;
fator: parcela (op3 parcela)*;
op1: '+' | '-';
op2: '*' | '/';
op3: '%';
parcela: op_unario? parcela_unario | parcela_nao_unario;
parcela_unario: '^'? identificador
    | IDENT '(' expressao (',' expressao)* ')'
    | NUM_INT
    | NUM_REAL
    | '(' expressao ')';
parcela_nao_unario: '&' identificador | CADEIA;
exp_relacional: exp_aritmetica (op_relacional exp_aritmetica)?;
op_relacional: '=' | '<>' | '>=' | '<=' | '>' | '<';
expressao: termo_logico (op_logico_1 termo_logico)*;
termo_logico: fator_logico (op_logico_2 fator_logico)*;
fator_logico: 'nao'? parcela_logica;
parcela_logica: 'verdadeiro' | 'falso' | exp_relacional;
op_logico_1: 'ou';
op_logico_2: 'e';
