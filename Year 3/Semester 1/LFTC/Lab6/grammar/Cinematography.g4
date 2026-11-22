
grammar Cinematography;

// --------------------
// PROGRAM
// --------------------

program
    : statement* EOF
    ;

statement
    : inputStatement
    | outputStatement
    | declarationStatement
    | assignmentStatement
    | ifStatement
    | forStatement
    | whileStatement
    | userDatatypeStatement
    | vectorStatement
    | functionStatement
    | returnStatement
    ;

// --------------------
// BASIC STATEMENTS
// --------------------

inputStatement
    : FILM LPAREN identifier RPAREN SEMI
    ;

outputStatement
    : ONSCREEN LPAREN expression RPAREN SEMI
    ;

declarationStatement
    : declaredType identifier (COMMA identifier)* SEMI
    ;

declaredType
    : type
    | identifier
    | REEL LPAREN declaredType RPAREN
    ;

assignmentStatement
    : identifier ASSIGN expression SEMI
    ;

// --------------------
// EXPRESSIONS
// --------------------

expression
    : logicalOrExpression
    ;

logicalOrExpression
    : logicalAndExpression (OR logicalAndExpression)*
    ;

logicalAndExpression
    : comparisonExpression (AND comparisonExpression)*
    ;

comparisonExpression
    : additiveExpression (relationalOperator additiveExpression)?
    ;

additiveExpression
    : multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*
    ;

multiplicativeExpression
    : operand ((MULTIPLY | DIVIDE | MODULO) operand)*
    ;

operand
    : identifier (DOT GET LPAREN index RPAREN)?
    | value
    | NEW constructorCall
    | functionCall
    | LPAREN expression RPAREN
    ;

constructorCall
    : identifier LPAREN argumentList RPAREN
    ;

functionCall
    : identifier LPAREN argumentList RPAREN
    ;

argumentList
    : (expression (COMMA expression)*)?
    ;

index
    : NUMBER
    | identifier
    ;

// --------------------
// CONDITIONS
// --------------------

ifStatement
    : CHECK LPAREN condition RPAREN DO
      LBRACE statement* RBRACE
      (ELSE LBRACE statement* RBRACE)?
    ;

condition
    : logicalOrCondition
    ;

logicalOrCondition
    : logicalAndCondition (OR logicalAndCondition)*
    ;

logicalAndCondition
    : conditionAtom (AND conditionAtom)*
    ;

conditionAtom
    : comparisonExpression
    | booleanValue
    | LPAREN condition RPAREN
    ;

// --------------------
// LOOPS
// --------------------

forStatement
    : FOR LPAREN forInitialization SEMI condition SEMI
      forAssignment RPAREN DO
      LBRACE statement* RBRACE
    ;

forInitialization
    : declaredType identifier
    | forAssignment
    ;

forAssignment
    : identifier ASSIGN expression
    ;

whileStatement
    : WHILE LPAREN condition RPAREN DO
      LBRACE statement* RBRACE
    ;

// --------------------
// USER-DEFINED TYPES
// --------------------

userDatatypeStatement
    : RECORD identifier LBRACE field* RBRACE SEMI
    ;

field
    : declaredType identifier SEMI
    ;

// --------------------
// VECTORS
// --------------------

vectorStatement
    : vectorCreation
    | vectorAssignment
    | vectorAdd
    | vectorRemoveAtIndex
    | vectorSetAtIndex
    ;

vectorCreation
    : REEL LPAREN declaredType RPAREN identifier SEMI
    ;

vectorAssignment
    : identifier ASSIGN vector SEMI
    ;

vector
    : LBRACE (expression (COMMA expression)*)? RBRACE
    ;

vectorAdd
    : identifier DOT ADD LPAREN expression RPAREN SEMI
    ;

vectorRemoveAtIndex
    : identifier DOT CUT LPAREN index RPAREN SEMI
    ;

vectorSetAtIndex
    : identifier DOT OVERWRITE LPAREN index COMMA expression RPAREN SEMI
    ;

// --------------------
// FUNCTIONS AND RETURN
// --------------------

functionStatement
    : declaredType identifier LPAREN parameters RPAREN
      LBRACE statement* returnStatement RBRACE
    | NOMEMORY identifier LPAREN parameters RPAREN
      LBRACE statement* RBRACE
    ;

parameters
    : (parameter (COMMA parameter)*)?
    ;

parameter
    : declaredType identifier
    ;

returnStatement
    : RETURN expression SEMI
    ;

// --------------------
// TYPES AND VALUES
// --------------------

type
    : INT
    | CHAR
    | SCRIPT
    | BOOL
    ;

value
    : NUMBER
    | STRING
    | CHARACTER
    | booleanValue
    ;

booleanValue
    : TRUE
    | FALSE
    ;

relationalOperator
    : LESS
    | LESS_EQUAL
    | GREATER
    | GREATER_EQUAL
    | EQUAL
    | NOT_EQUAL
    ;

identifier
    : IDENTIFIER
    ;

// --------------------
// LEXER RULES
// --------------------

INT       : 'int';
CHAR      : 'char';
SCRIPT    : 'script';
BOOL      : 'bool';
NEW       : 'new';
FILM      : 'film';
ONSCREEN  : 'onScreen';
TRUE      : 'true';
FALSE     : 'false';
CHECK     : 'check';
ELSE      : 'else';
FOR       : 'for';
DO        : 'do';
WHILE     : 'while';
RECORD    : 'record';
REEL      : 'reel';
RETURN    : 'return';
ADD       : 'add';
CUT       : 'cut';
GET       : 'get';
OVERWRITE : 'overwrite';
NOMEMORY  : 'nomemory';

PLUS       : '+';
MINUS      : '-';
MULTIPLY   : '*';
DIVIDE     : '/';
MODULO     : '%';
LESS       : '<';
LESS_EQUAL : '<=';
GREATER    : '>';
GREATER_EQUAL : '>=';
EQUAL      : '==';
NOT_EQUAL  : '!=';
ASSIGN     : '=';
AND        : '&&';
OR         : '||';

LPAREN : '(';
RPAREN : ')';
LBRACE : '{';
RBRACE : '}';
COLON  : ':';
SEMI   : ';';
COMMA  : ',';
DOT    : '.';

IDENTIFIER
    : [a-zA-Z_] [a-zA-Z_0-9]*
    ;

NUMBER
    : '0'
    | [1-9] [0-9]*
    ;

STRING
    : '"' ~["\r\n]* '"'
    ;

CHARACTER
    : '\'' ~['\r\n] '\''
    ;

COMMENT
    : '//' ~[\r\n]* -> skip
    ;

WHITESPACE
    : [ \t\r\n]+ -> skip
    ;
