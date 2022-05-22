import ply.yacc as yacc
from analiseLexica import *

def p_programa(p):
  '''programa : secaoUsing defClasse
  | secaoUsing secaoNamespace
  | defClasse
  | secaoNamespace'''
def p_secaoUsing(p):
  '''secaoUsing : USING ID PONTO_VIRGULA
  | USING ID PONTO_VIRGULA secaoUsing'''
def p_secaoNamespace(p):
  '''secaoNamespace : NAMESPACE ID CHAVE_L defClasse CHAVE_R'''
def p_defClasse(p):
  ''' defClasse : PUBLIC CLASS ID CHAVE_L CHAVE_R
  | CLASS ID CHAVE_L CHAVE_R
  | PUBLIC CLASS ID CHAVE_L corpoClasse CHAVE_R
  | CLASS ID CHAVE_L corpoClasse CHAVE_R
  | PUBLIC CLASS ID CHAVE_L CHAVE_R defClasse
  | CLASS ID CHAVE_L CHAVE_R defClasse
  | CLASS ID CHAVE_L corpoClasse CHAVE_R defClasse
  | PUBLIC CLASS ID CHAVE_L corpoClasse CHAVE_R defClasse'''
def p_corpoClasse(p):
  ''' corpoClasse : atributo
  | atributo corpoClasse
  | assinatura
  | assinatura corpoClasse''' 
def p_atributo(p):
  '''atributo : PUBLIC tipo atribuicao PONTO_VIRGULA
  | tipo atribuicao PONTO_VIRGULA '''
def p_atribuicao(p):
  '''atribuicao : ID ATRIBUICAO ID
  | ID ATRIBUICAO INT
  | ID
  | ID ATRIBUICAO chamadaMetodo '''
  
def p_assinatura(p):
  '''assinatura : PUBLIC tipo ID PARENTESE_L parametrosFormais PARENTESE_R bloco
  | tipo ID PARENTESE_L parametrosFormais PARENTESE_R bloco'''
def p_parametrosFormais(p):
  '''parametrosFormais : tipo ID
  | tipo ID VIRGULA parametrosFormais'''
def p_corpoMetodo(p):
  '''corpoMetodo : comandos
  | comandos corpoMetodo''' 
def p_tipo(p):
  '''tipo : INT 
  | STRING
  | ID
  | BOOL'''
def p_chamadaMetodo(p):
  '''chamadaMetodo : ID PARENTESE_L parametrosReais PARENTESE_R'''
def p_parametrosReais(p):
  '''parametrosReais : ID
  | ID VIRGULA parametrosReais
  | INT
  | INT VIRGULA parametrosReais'''  
def p_comandos(p):
  ''' comandos : comandos1
  | comandos2'''

def p_comandos1(p):
  '''comandos1 : for1
  | foreach1
  | while1
  | return
  | atributo
  | IF PARENTESE_L exp1 PARENTESE_R comandos1 ELSE comandos1
  | IF PARENTESE_L exp1 PARENTESE_R bloco ELSE comandos1
  | IF PARENTESE_L exp1 PARENTESE_R comandos1 ELSE bloco
  | IF PARENTESE_L exp1 PARENTESE_R bloco ELSE bloco'''

def p_bloco(p):
  '''bloco : CHAVE_L corpoComando CHAVE_R
  | CHAVE_L CHAVE_R'''
def p_comandos2(p):
  '''comandos2 : IF PARENTESE_L exp1 PARENTESE_R comandos
  | IF PARENTESE_L exp1 PARENTESE_R comandos1 ELSE comandos2
  | IF PARENTESE_L exp1 PARENTESE_R bloco
  | IF PARENTESE_L exp1 PARENTESE_R bloco ELSE comandos2
  | for2
  | while2
  | foreach2'''
def p_corpoComando(p):
  ''' corpoComando : comandos
  | corpoComando comandos'''
def p_for1(p):
  '''for1 : FOR PARENTESE_L tipo atribuicao PONTO_VIRGULA exp1 PONTO_VIRGULA exp1 PARENTESE_R bloco 
  | FOR PARENTESE_L atribuicao PONTO_VIRGULA exp1 PONTO_VIRGULA exp1 PARENTESE_R bloco 
  | FOR PARENTESE_L tipo atribuicao PONTO_VIRGULA exp1 PONTO_VIRGULA exp1 PARENTESE_R comandos1
  | FOR PARENTESE_L atribuicao PONTO_VIRGULA exp1 PONTO_VIRGULA exp1 PARENTESE_R comandos1'''
def p_for2(p):
  '''for2 : FOR PARENTESE_L tipo atribuicao PONTO_VIRGULA exp1 PONTO_VIRGULA exp1 PARENTESE_R comandos2
  | FOR PARENTESE_L atribuicao PONTO_VIRGULA exp1 PONTO_VIRGULA exp1 PARENTESE_R comandos2'''
def p_while1(p):
  '''while1 : WHILE PARENTESE_L exp1 PARENTESE_R bloco
  | WHILE PARENTESE_L exp1 PARENTESE_R comandos1'''
def p_while2(p):
  '''while2 : WHILE PARENTESE_L exp1 PARENTESE_R comandos2'''
def p_foreach1(p):
  '''foreach1 : FOREACH PARENTESE_L tipo ID IN ID PARENTESE_R bloco
  | FOREACH PARENTESE_L  ID IN ID PARENTESE_R bloco
  | FOREACH PARENTESE_L tipo ID IN ID PARENTESE_R  comandos1 
  | FOREACH PARENTESE_L ID IN ID PARENTESE_R  comandos1'''   
def p_foreach2(p):
  '''foreach2 : FOREACH PARENTESE_L tipo ID IN ID PARENTESE_R  comandos2 
  | FOREACH PARENTESE_L ID IN ID PARENTESE_R  comandos2'''    
def p_return(p):
  '''return : RETURN ID PONTO_VIRGULA
  | RETURN INT PONTO_VIRGULA
  | RETURN PONTO_VIRGULA'''
def p_exp1(p):
  '''exp1 : exp1 ATRIBUICAO exp2
  | exp2'''
def p_exp2(p):
  '''exp2 : exp2 OR exp3
  | exp3'''
def p_exp3(p):
  '''exp3 : exp3 AND exp4
  | exp4'''
def p_exp4(p):
  '''exp4 : exp4 BIT_OR exp5
  | exp5'''
def p_exp5(p):
  '''exp5 : exp5 XOR exp6
  | exp6'''
def p_exp6(p):
  '''exp6 : exp6 BIT_AND exp7
  | exp7'''
def p_exp7(p):
  '''exp7 : exp7 IGUAL exp8
  | exp7 DIFERENTE exp8
  | exp8'''
def p_exp8(p):
  '''exp8 : exp8 MENOR exp9
  | exp8 MENOR_IGUAL exp9
  | exp8 MAIOR exp9
  | exp8 MAIOR_IGUAL exp9
  | exp9'''
def p_exp9(p):
  '''exp9 : exp9 SOMA exp10
  | exp9 SUB exp10
  | exp10'''
def p_exp10(p):
  '''exp10 : exp10 MUL exp11
  | exp10 DIV exp11
  | exp11'''
def p_exp11(p):
  '''exp11 : BIT_NOT exp12
  | NOT exp12
  | exp12'''
def p_exp12(p):
  '''exp12 : exp12 INCREMENTO
  | exp12 DECREMENTO
  | exp13'''
def p_exp13(p):
  '''exp13 : TRUE 
  | FALSE
  | STRING
  | ID
  | chamadaMetodo
  | INT
  | PARENTESE_L exp1 PARENTESE_R'''









def p_error(p):
  print("Erro Sintático")
