
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ATRIBUICAO BIT_AND BIT_NOT BIT_OR BOOL CHAVE_L CHAVE_R CLASS COMMENT DECREMENTO DIFERENTE DIV ELSE FALSE FOR FOREACH ID IF IGUAL IN INCREMENTO INT IS MAIOR MAIOR_IGUAL MENOR MENOR_IGUAL MUL NAMESPACE NEW NOT NULL OBJECT OR PARENTESE_L PARENTESE_R PONTO PONTO_VIRGULA PUBLIC RETURN SIZEOF SOMA STATIC STRING SUB THIS TRUE USING VIRGULA WHILE XOR newLineprograma : secaoUsing defClasse\n  | secaoUsing secaoNamespace\n  | defClasse\n  | secaoNamespacesecaoUsing : USING ID PONTO_VIRGULA\n  | USING ID PONTO_VIRGULA secaoUsingsecaoNamespace : NAMESPACE ID CHAVE_L defClasse CHAVE_R defClasse : PUBLIC CLASS ID CHAVE_L CHAVE_R\n  | CLASS ID CHAVE_L CHAVE_R\n  | PUBLIC CLASS ID CHAVE_L corpoClasse CHAVE_R\n  | CLASS ID CHAVE_L corpoClasse CHAVE_R\n  | PUBLIC CLASS ID CHAVE_L CHAVE_R defClasse\n  | CLASS ID CHAVE_L CHAVE_R defClasse\n  | CLASS ID CHAVE_L corpoClasse CHAVE_R defClasse\n  | PUBLIC CLASS ID CHAVE_L corpoClasse CHAVE_R defClasse corpoClasse : atributo\n  | atributo corpoClasse\n  | assinatura\n  | assinatura corpoClasseatributo : PUBLIC tipo atribuicao PONTO_VIRGULA\n  | tipo atribuicao PONTO_VIRGULA atribuicao : ID ATRIBUICAO ID\n  | ID ATRIBUICAO INT\n  | ID\n  | ID ATRIBUICAO chamadaMetodo assinatura : PUBLIC tipo ID PARENTESE_L parametrosFormais PARENTESE_R bloco\n  | tipo ID PARENTESE_L parametrosFormais PARENTESE_R blocoparametrosFormais : tipo ID\n  | tipo ID VIRGULA parametrosFormaiscorpoMetodo : comandos\n  | comandos corpoMetodotipo : INT \n  | STRING\n  | ID\n  | BOOLchamadaMetodo : ID PARENTESE_L parametrosReais PARENTESE_RparametrosReais : ID\n  | ID VIRGULA parametrosReais\n  | INT\n  | INT VIRGULA parametrosReais comandos : comandos1\n  | comandos2comandos1 : for1\n  | foreach1\n  | while1\n  | return\n  | atributo\n  | IF PARENTESE_L exp1 PARENTESE_R comandos1 ELSE comandos1\n  | IF PARENTESE_L exp1 PARENTESE_R bloco ELSE comandos1\n  | IF PARENTESE_L exp1 PARENTESE_R comandos1 ELSE bloco\n  | IF PARENTESE_L exp1 PARENTESE_R bloco ELSE blocobloco : CHAVE_L corpoComando CHAVE_R\n  | CHAVE_L CHAVE_Rcomandos2 : IF PARENTESE_L exp1 PARENTESE_R comandos\n  | IF PARENTESE_L exp1 PARENTESE_R comandos1 ELSE comandos2\n  | IF PARENTESE_L exp1 PARENTESE_R bloco\n  | IF PARENTESE_L exp1 PARENTESE_R bloco ELSE comandos2\n  | for2\n  | while2\n  | foreach2 corpoComando : comandos\n  | corpoComando comandosfor1 : FOR PARENTESE_L tipo atribuicao PONTO_VIRGULA exp1 PONTO_VIRGULA exp1 PARENTESE_R bloco \n  | FOR PARENTESE_L atribuicao PONTO_VIRGULA exp1 PONTO_VIRGULA exp1 PARENTESE_R bloco \n  | FOR PARENTESE_L tipo atribuicao PONTO_VIRGULA exp1 PONTO_VIRGULA exp1 PARENTESE_R comandos1\n  | FOR PARENTESE_L atribuicao PONTO_VIRGULA exp1 PONTO_VIRGULA exp1 PARENTESE_R comandos1for2 : FOR PARENTESE_L tipo atribuicao PONTO_VIRGULA exp1 PONTO_VIRGULA exp1 PARENTESE_R comandos2\n  | FOR PARENTESE_L atribuicao PONTO_VIRGULA exp1 PONTO_VIRGULA exp1 PARENTESE_R comandos2while1 : WHILE PARENTESE_L exp1 PARENTESE_R bloco\n  | WHILE PARENTESE_L exp1 PARENTESE_R comandos1while2 : WHILE PARENTESE_L exp1 PARENTESE_R comandos2foreach1 : FOREACH PARENTESE_L tipo ID IN ID PARENTESE_R bloco\n  | FOREACH PARENTESE_L  ID IN ID PARENTESE_R bloco\n  | FOREACH PARENTESE_L tipo ID IN ID PARENTESE_R  comandos1 \n  | FOREACH PARENTESE_L ID IN ID PARENTESE_R  comandos1foreach2 : FOREACH PARENTESE_L tipo ID IN ID PARENTESE_R  comandos2 \n  | FOREACH PARENTESE_L ID IN ID PARENTESE_R  comandos2return : RETURN ID PONTO_VIRGULA\n  | RETURN INT PONTO_VIRGULA\n  | RETURN PONTO_VIRGULAexp1 : exp1 ATRIBUICAO exp2\n  | exp2exp2 : exp2 OR exp3\n  | exp3exp3 : exp3 AND exp4\n  | exp4exp4 : exp4 BIT_OR exp5\n  | exp5exp5 : exp5 XOR exp6\n  | exp6exp6 : exp6 BIT_AND exp7\n  | exp7exp7 : exp7 IGUAL exp8\n  | exp7 DIFERENTE exp8\n  | exp8exp8 : exp8 MENOR exp9\n  | exp8 MENOR_IGUAL exp9\n  | exp8 MAIOR exp9\n  | exp8 MAIOR_IGUAL exp9\n  | exp9exp9 : exp9 SOMA exp10\n  | exp9 SUB exp10\n  | exp10exp10 : exp10 MUL exp11\n  | exp10 DIV exp11\n  | exp11exp11 : BIT_NOT exp12\n  | NOT exp12\n  | exp12exp12 : exp12 INCREMENTO\n  | exp12 DECREMENTO\n  | exp13exp13 : TRUE \n  | FALSE\n  | STRING\n  | ID\n  | chamadaMetodo\n  | INT\n  | PARENTESE_L exp1 PARENTESE_R'
    
_lr_action_items = {'USING':([0,15,],[5,5,]),'PUBLIC':([0,2,15,17,18,19,20,22,24,25,32,35,43,47,51,64,65,69,71,72,73,74,75,76,77,78,79,80,82,83,84,94,95,102,135,136,138,163,165,166,167,188,189,190,191,192,196,197,198,199,200,201,202,205,206,207,208,210,211,212,213,214,215,216,217,218,219,220,],[6,6,-5,26,6,-6,26,6,26,26,6,6,6,-21,-20,-27,90,-26,90,-53,-61,-41,-42,-43,-44,-45,-46,-47,-58,-59,-60,-52,-62,-80,-78,-79,90,90,-41,-56,-54,-69,-70,-71,90,90,90,-48,-50,-55,-51,-49,-57,90,-73,-75,-77,90,-72,-74,-76,90,-64,-66,-68,-63,-65,-67,]),'CLASS':([0,2,6,15,18,19,22,32,35,43,],[7,7,12,-5,7,-6,7,7,7,7,]),'NAMESPACE':([0,2,15,19,],[8,8,-5,-6,]),'$end':([1,3,4,9,10,22,32,34,35,41,42,43,44,50,],[0,-3,-4,-1,-2,-9,-8,-13,-11,-7,-12,-10,-14,-15,]),'ID':([5,7,8,12,17,20,21,24,25,26,27,28,29,30,38,47,48,49,51,52,53,61,63,64,65,69,71,72,73,74,75,76,77,78,79,80,82,83,84,86,89,90,91,93,94,95,96,97,99,100,102,104,107,119,121,129,131,132,133,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,160,162,163,165,166,167,184,186,188,189,190,191,192,194,196,197,198,199,200,201,202,203,205,206,207,208,210,211,212,213,214,215,216,217,218,219,220,],[11,13,14,16,21,21,-34,21,21,21,40,-32,-33,-35,46,-21,21,55,-20,21,59,66,21,-27,21,-26,21,-53,-61,-41,-42,-43,-44,-45,-46,-47,-58,-59,-60,98,101,21,66,66,-52,-62,126,131,133,126,-80,98,126,126,126,98,-34,161,-34,-78,-79,21,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,187,21,-41,-56,-54,126,195,-69,-70,-71,21,21,126,21,-48,-50,-55,-51,-49,-57,126,21,-73,-75,-77,21,-72,-74,-76,21,-64,-66,-68,-63,-65,-67,]),'PONTO_VIRGULA':([11,39,40,45,46,55,56,57,89,92,98,101,103,109,110,111,112,113,114,115,116,117,118,120,122,123,124,125,126,127,128,130,131,155,156,157,158,159,164,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,185,193,],[15,47,-24,51,-24,-22,-23,-25,102,-36,-24,135,136,-82,-84,-86,-88,-90,-92,-95,-100,-103,-106,-109,-112,-113,-114,-115,-116,-117,-118,160,-24,-107,-110,-111,-108,184,-119,-81,-83,-85,-87,-89,-91,-93,-94,-96,-97,-98,-99,-101,-102,-104,-105,194,203,]),'CHAVE_L':([13,14,16,60,62,138,163,191,192,196,205,210,214,],[17,18,20,65,65,65,65,65,65,65,65,65,65,]),'CHAVE_R':([17,20,22,23,24,25,31,32,33,34,35,36,37,42,43,44,47,50,51,64,65,69,71,72,73,74,75,76,77,78,79,80,82,83,84,94,95,102,135,136,165,166,167,188,189,190,197,198,199,200,201,202,206,207,208,211,212,213,215,216,217,218,219,220,],[22,32,-9,35,-16,-18,41,-8,43,-13,-11,-17,-19,-12,-10,-14,-21,-15,-20,-27,72,-26,94,-53,-61,-41,-42,-43,-44,-45,-46,-47,-58,-59,-60,-52,-62,-80,-78,-79,-41,-56,-54,-69,-70,-71,-48,-50,-55,-51,-49,-57,-73,-75,-77,-72,-74,-76,-64,-66,-68,-63,-65,-67,]),'INT':([17,20,24,25,26,47,48,49,51,52,61,63,64,65,69,71,72,73,74,75,76,77,78,79,80,82,83,84,89,90,91,93,94,95,96,97,99,100,102,107,119,121,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,160,163,165,166,167,184,188,189,190,191,192,194,196,197,198,199,200,201,202,203,205,206,207,208,210,211,212,213,214,215,216,217,218,219,220,],[28,28,28,28,28,-21,28,56,-20,28,68,28,-27,28,-26,28,-53,-61,-41,-42,-43,-44,-45,-46,-47,-58,-59,-60,103,28,68,68,-52,-62,128,28,28,128,-80,128,128,128,-78,-79,28,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,28,-41,-56,-54,128,-69,-70,-71,28,28,128,28,-48,-50,-55,-51,-49,-57,128,28,-73,-75,-77,28,-72,-74,-76,28,-64,-66,-68,-63,-65,-67,]),'STRING':([17,20,24,25,26,47,48,51,52,63,64,65,69,71,72,73,74,75,76,77,78,79,80,82,83,84,90,94,95,96,97,99,100,102,107,119,121,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,160,163,165,166,167,184,188,189,190,191,192,194,196,197,198,199,200,201,202,203,205,206,207,208,210,211,212,213,214,215,216,217,218,219,220,],[29,29,29,29,29,-21,29,-20,29,29,-27,29,-26,29,-53,-61,-41,-42,-43,-44,-45,-46,-47,-58,-59,-60,29,-52,-62,125,29,29,125,-80,125,125,125,-78,-79,29,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,29,-41,-56,-54,125,-69,-70,-71,29,29,125,29,-48,-50,-55,-51,-49,-57,125,29,-73,-75,-77,29,-72,-74,-76,29,-64,-66,-68,-63,-65,-67,]),'BOOL':([17,20,24,25,26,47,48,51,52,63,64,65,69,71,72,73,74,75,76,77,78,79,80,82,83,84,90,94,95,97,99,102,135,136,138,163,165,166,167,188,189,190,191,192,196,197,198,199,200,201,202,205,206,207,208,210,211,212,213,214,215,216,217,218,219,220,],[30,30,30,30,30,-21,30,-20,30,30,-27,30,-26,30,-53,-61,-41,-42,-43,-44,-45,-46,-47,-58,-59,-60,30,-52,-62,30,30,-80,-78,-79,30,30,-41,-56,-54,-69,-70,-71,30,30,30,-48,-50,-55,-51,-49,-57,30,-73,-75,-77,30,-72,-74,-76,30,-64,-66,-68,-63,-65,-67,]),'PARENTESE_L':([40,46,55,81,85,87,88,96,100,107,119,121,126,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,160,184,194,203,],[48,52,61,96,97,99,100,107,107,107,107,107,61,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,]),'ATRIBUICAO':([40,46,92,98,108,109,110,111,112,113,114,115,116,117,118,120,122,123,124,125,126,127,128,131,134,137,155,156,157,158,164,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,185,193,204,209,],[49,49,-36,49,139,-82,-84,-86,-88,-90,-92,-95,-100,-103,-106,-109,-112,-113,-114,-115,-116,-117,-118,49,139,139,-107,-110,-111,-108,-119,-81,-83,-85,-87,-89,-91,-93,-94,-96,-97,-98,-99,-101,-102,-104,-105,139,139,139,139,]),'IF':([47,51,65,71,72,73,74,75,76,77,78,79,80,82,83,84,94,95,102,135,136,138,163,165,166,167,188,189,190,191,192,196,197,198,199,200,201,202,205,206,207,208,210,211,212,213,214,215,216,217,218,219,220,],[-21,-20,81,81,-53,-61,-41,-42,-43,-44,-45,-46,-47,-58,-59,-60,-52,-62,-80,-78,-79,81,81,-41,-56,-54,-69,-70,-71,81,81,81,-48,-50,-55,-51,-49,-57,81,-73,-75,-77,81,-72,-74,-76,81,-64,-66,-68,-63,-65,-67,]),'FOR':([47,51,65,71,72,73,74,75,76,77,78,79,80,82,83,84,94,95,102,135,136,138,163,165,166,167,188,189,190,191,192,196,197,198,199,200,201,202,205,206,207,208,210,211,212,213,214,215,216,217,218,219,220,],[-21,-20,85,85,-53,-61,-41,-42,-43,-44,-45,-46,-47,-58,-59,-60,-52,-62,-80,-78,-79,85,85,-41,-56,-54,-69,-70,-71,85,85,85,-48,-50,-55,-51,-49,-57,85,-73,-75,-77,85,-72,-74,-76,85,-64,-66,-68,-63,-65,-67,]),'FOREACH':([47,51,65,71,72,73,74,75,76,77,78,79,80,82,83,84,94,95,102,135,136,138,163,165,166,167,188,189,190,191,192,196,197,198,199,200,201,202,205,206,207,208,210,211,212,213,214,215,216,217,218,219,220,],[-21,-20,87,87,-53,-61,-41,-42,-43,-44,-45,-46,-47,-58,-59,-60,-52,-62,-80,-78,-79,87,87,-41,-56,-54,-69,-70,-71,87,87,87,-48,-50,-55,-51,-49,-57,87,-73,-75,-77,87,-72,-74,-76,87,-64,-66,-68,-63,-65,-67,]),'WHILE':([47,51,65,71,72,73,74,75,76,77,78,79,80,82,83,84,94,95,102,135,136,138,163,165,166,167,188,189,190,191,192,196,197,198,199,200,201,202,205,206,207,208,210,211,212,213,214,215,216,217,218,219,220,],[-21,-20,88,88,-53,-61,-41,-42,-43,-44,-45,-46,-47,-58,-59,-60,-52,-62,-80,-78,-79,88,88,-41,-56,-54,-69,-70,-71,88,88,88,-48,-50,-55,-51,-49,-57,88,-73,-75,-77,88,-72,-74,-76,88,-64,-66,-68,-63,-65,-67,]),'RETURN':([47,51,65,71,72,73,74,75,76,77,78,79,80,82,83,84,94,95,102,135,136,138,163,165,166,167,188,189,190,191,192,196,197,198,199,200,201,202,205,206,207,208,210,211,212,213,214,215,216,217,218,219,220,],[-21,-20,89,89,-53,-61,-41,-42,-43,-44,-45,-46,-47,-58,-59,-60,-52,-62,-80,-78,-79,89,89,-41,-56,-54,-69,-70,-71,89,89,89,-48,-50,-55,-51,-49,-57,89,-73,-75,-77,89,-72,-74,-76,89,-64,-66,-68,-63,-65,-67,]),'ELSE':([47,51,72,76,77,78,79,80,94,102,135,136,165,166,188,189,197,198,200,201,206,207,211,212,215,216,218,219,],[-21,-20,-53,-43,-44,-45,-46,-47,-52,-80,-78,-79,191,192,-69,-70,-48,-50,-51,-49,-73,-75,-72,-74,-64,-66,-63,-65,]),'PARENTESE_R':([54,58,59,66,67,68,70,92,105,106,108,109,110,111,112,113,114,115,116,117,118,120,122,123,124,125,126,127,128,134,137,155,156,157,158,164,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,187,195,204,209,],[60,62,-28,-37,92,-39,-29,-36,-38,-40,138,-82,-84,-86,-88,-90,-92,-95,-100,-103,-106,-109,-112,-113,-114,-115,-116,-117,-118,163,164,-107,-110,-111,-108,-119,-81,-83,-85,-87,-89,-91,-93,-94,-96,-97,-98,-99,-101,-102,-104,-105,196,205,210,214,]),'VIRGULA':([59,66,68,],[63,91,93,]),'INCREMENTO':([92,120,122,123,124,125,126,127,128,155,156,157,158,164,],[-36,156,-112,-113,-114,-115,-116,-117,-118,156,-110,-111,156,-119,]),'DECREMENTO':([92,120,122,123,124,125,126,127,128,155,156,157,158,164,],[-36,157,-112,-113,-114,-115,-116,-117,-118,157,-110,-111,157,-119,]),'MUL':([92,117,118,120,122,123,124,125,126,127,128,155,156,157,158,164,180,181,182,183,],[-36,153,-106,-109,-112,-113,-114,-115,-116,-117,-118,-107,-110,-111,-108,-119,153,153,-104,-105,]),'DIV':([92,117,118,120,122,123,124,125,126,127,128,155,156,157,158,164,180,181,182,183,],[-36,154,-106,-109,-112,-113,-114,-115,-116,-117,-118,-107,-110,-111,-108,-119,154,154,-104,-105,]),'SOMA':([92,116,117,118,120,122,123,124,125,126,127,128,155,156,157,158,164,176,177,178,179,180,181,182,183,],[-36,151,-103,-106,-109,-112,-113,-114,-115,-116,-117,-118,-107,-110,-111,-108,-119,151,151,151,151,-101,-102,-104,-105,]),'SUB':([92,116,117,118,120,122,123,124,125,126,127,128,155,156,157,158,164,176,177,178,179,180,181,182,183,],[-36,152,-103,-106,-109,-112,-113,-114,-115,-116,-117,-118,-107,-110,-111,-108,-119,152,152,152,152,-101,-102,-104,-105,]),'MENOR':([92,115,116,117,118,120,122,123,124,125,126,127,128,155,156,157,158,164,174,175,176,177,178,179,180,181,182,183,],[-36,147,-100,-103,-106,-109,-112,-113,-114,-115,-116,-117,-118,-107,-110,-111,-108,-119,147,147,-96,-97,-98,-99,-101,-102,-104,-105,]),'MENOR_IGUAL':([92,115,116,117,118,120,122,123,124,125,126,127,128,155,156,157,158,164,174,175,176,177,178,179,180,181,182,183,],[-36,148,-100,-103,-106,-109,-112,-113,-114,-115,-116,-117,-118,-107,-110,-111,-108,-119,148,148,-96,-97,-98,-99,-101,-102,-104,-105,]),'MAIOR':([92,115,116,117,118,120,122,123,124,125,126,127,128,155,156,157,158,164,174,175,176,177,178,179,180,181,182,183,],[-36,149,-100,-103,-106,-109,-112,-113,-114,-115,-116,-117,-118,-107,-110,-111,-108,-119,149,149,-96,-97,-98,-99,-101,-102,-104,-105,]),'MAIOR_IGUAL':([92,115,116,117,118,120,122,123,124,125,126,127,128,155,156,157,158,164,174,175,176,177,178,179,180,181,182,183,],[-36,150,-100,-103,-106,-109,-112,-113,-114,-115,-116,-117,-118,-107,-110,-111,-108,-119,150,150,-96,-97,-98,-99,-101,-102,-104,-105,]),'IGUAL':([92,114,115,116,117,118,120,122,123,124,125,126,127,128,155,156,157,158,164,173,174,175,176,177,178,179,180,181,182,183,],[-36,145,-95,-100,-103,-106,-109,-112,-113,-114,-115,-116,-117,-118,-107,-110,-111,-108,-119,145,-93,-94,-96,-97,-98,-99,-101,-102,-104,-105,]),'DIFERENTE':([92,114,115,116,117,118,120,122,123,124,125,126,127,128,155,156,157,158,164,173,174,175,176,177,178,179,180,181,182,183,],[-36,146,-95,-100,-103,-106,-109,-112,-113,-114,-115,-116,-117,-118,-107,-110,-111,-108,-119,146,-93,-94,-96,-97,-98,-99,-101,-102,-104,-105,]),'BIT_AND':([92,113,114,115,116,117,118,120,122,123,124,125,126,127,128,155,156,157,158,164,172,173,174,175,176,177,178,179,180,181,182,183,],[-36,144,-92,-95,-100,-103,-106,-109,-112,-113,-114,-115,-116,-117,-118,-107,-110,-111,-108,-119,144,-91,-93,-94,-96,-97,-98,-99,-101,-102,-104,-105,]),'XOR':([92,112,113,114,115,116,117,118,120,122,123,124,125,126,127,128,155,156,157,158,164,171,172,173,174,175,176,177,178,179,180,181,182,183,],[-36,143,-90,-92,-95,-100,-103,-106,-109,-112,-113,-114,-115,-116,-117,-118,-107,-110,-111,-108,-119,143,-89,-91,-93,-94,-96,-97,-98,-99,-101,-102,-104,-105,]),'BIT_OR':([92,111,112,113,114,115,116,117,118,120,122,123,124,125,126,127,128,155,156,157,158,164,170,171,172,173,174,175,176,177,178,179,180,181,182,183,],[-36,142,-88,-90,-92,-95,-100,-103,-106,-109,-112,-113,-114,-115,-116,-117,-118,-107,-110,-111,-108,-119,142,-87,-89,-91,-93,-94,-96,-97,-98,-99,-101,-102,-104,-105,]),'AND':([92,110,111,112,113,114,115,116,117,118,120,122,123,124,125,126,127,128,155,156,157,158,164,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,],[-36,141,-86,-88,-90,-92,-95,-100,-103,-106,-109,-112,-113,-114,-115,-116,-117,-118,-107,-110,-111,-108,-119,141,-85,-87,-89,-91,-93,-94,-96,-97,-98,-99,-101,-102,-104,-105,]),'OR':([92,109,110,111,112,113,114,115,116,117,118,120,122,123,124,125,126,127,128,155,156,157,158,164,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,],[-36,140,-84,-86,-88,-90,-92,-95,-100,-103,-106,-109,-112,-113,-114,-115,-116,-117,-118,-107,-110,-111,-108,-119,140,-83,-85,-87,-89,-91,-93,-94,-96,-97,-98,-99,-101,-102,-104,-105,]),'BIT_NOT':([96,100,107,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,160,184,194,203,],[119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,]),'NOT':([96,100,107,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,160,184,194,203,],[121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,]),'TRUE':([96,100,107,119,121,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,160,184,194,203,],[123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,]),'FALSE':([96,100,107,119,121,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,160,184,194,203,],[124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,]),'IN':([133,161,],[162,186,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'secaoUsing':([0,15,],[2,19,]),'defClasse':([0,2,18,22,32,35,43,],[3,9,31,34,42,44,50,]),'secaoNamespace':([0,2,],[4,10,]),'corpoClasse':([17,20,24,25,],[23,33,36,37,]),'atributo':([17,20,24,25,65,71,138,163,191,192,196,205,210,214,],[24,24,24,24,80,80,80,80,80,80,80,80,80,80,]),'assinatura':([17,20,24,25,],[25,25,25,25,]),'tipo':([17,20,24,25,26,48,52,63,65,71,90,97,99,138,163,191,192,196,205,210,214,],[27,27,27,27,38,53,53,53,86,86,104,129,132,86,86,86,86,86,86,86,86,]),'atribuicao':([27,38,86,97,104,129,],[39,45,39,130,45,159,]),'parametrosFormais':([48,52,63,],[54,58,70,]),'chamadaMetodo':([49,96,100,107,119,121,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,160,184,194,203,],[57,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,]),'bloco':([60,62,138,163,191,192,196,205,210,214,],[64,69,166,188,198,200,206,211,215,218,]),'parametrosReais':([61,91,93,],[67,105,106,]),'corpoComando':([65,],[71,]),'comandos':([65,71,138,],[73,95,167,]),'comandos1':([65,71,138,163,191,192,196,205,210,214,],[74,74,165,189,197,201,207,212,216,219,]),'comandos2':([65,71,138,163,191,192,196,205,210,214,],[75,75,75,190,199,202,208,213,217,220,]),'for1':([65,71,138,163,191,192,196,205,210,214,],[76,76,76,76,76,76,76,76,76,76,]),'foreach1':([65,71,138,163,191,192,196,205,210,214,],[77,77,77,77,77,77,77,77,77,77,]),'while1':([65,71,138,163,191,192,196,205,210,214,],[78,78,78,78,78,78,78,78,78,78,]),'return':([65,71,138,163,191,192,196,205,210,214,],[79,79,79,79,79,79,79,79,79,79,]),'for2':([65,71,138,163,191,192,196,205,210,214,],[82,82,82,82,82,82,82,82,82,82,]),'while2':([65,71,138,163,191,192,196,205,210,214,],[83,83,83,83,83,83,83,83,83,83,]),'foreach2':([65,71,138,163,191,192,196,205,210,214,],[84,84,84,84,84,84,84,84,84,84,]),'exp1':([96,100,107,160,184,194,203,],[108,134,137,185,193,204,209,]),'exp2':([96,100,107,139,160,184,194,203,],[109,109,109,168,109,109,109,109,]),'exp3':([96,100,107,139,140,160,184,194,203,],[110,110,110,110,169,110,110,110,110,]),'exp4':([96,100,107,139,140,141,160,184,194,203,],[111,111,111,111,111,170,111,111,111,111,]),'exp5':([96,100,107,139,140,141,142,160,184,194,203,],[112,112,112,112,112,112,171,112,112,112,112,]),'exp6':([96,100,107,139,140,141,142,143,160,184,194,203,],[113,113,113,113,113,113,113,172,113,113,113,113,]),'exp7':([96,100,107,139,140,141,142,143,144,160,184,194,203,],[114,114,114,114,114,114,114,114,173,114,114,114,114,]),'exp8':([96,100,107,139,140,141,142,143,144,145,146,160,184,194,203,],[115,115,115,115,115,115,115,115,115,174,175,115,115,115,115,]),'exp9':([96,100,107,139,140,141,142,143,144,145,146,147,148,149,150,160,184,194,203,],[116,116,116,116,116,116,116,116,116,116,116,176,177,178,179,116,116,116,116,]),'exp10':([96,100,107,139,140,141,142,143,144,145,146,147,148,149,150,151,152,160,184,194,203,],[117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,180,181,117,117,117,117,]),'exp11':([96,100,107,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,160,184,194,203,],[118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,182,183,118,118,118,118,]),'exp12':([96,100,107,119,121,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,160,184,194,203,],[120,120,120,155,158,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,]),'exp13':([96,100,107,119,121,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,160,184,194,203,],[122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> secaoUsing defClasse','programa',2,'p_programa','analiseSintatica.py',5),
  ('programa -> secaoUsing secaoNamespace','programa',2,'p_programa','analiseSintatica.py',6),
  ('programa -> defClasse','programa',1,'p_programa','analiseSintatica.py',7),
  ('programa -> secaoNamespace','programa',1,'p_programa','analiseSintatica.py',8),
  ('secaoUsing -> USING ID PONTO_VIRGULA','secaoUsing',3,'p_secaoUsing','analiseSintatica.py',10),
  ('secaoUsing -> USING ID PONTO_VIRGULA secaoUsing','secaoUsing',4,'p_secaoUsing','analiseSintatica.py',11),
  ('secaoNamespace -> NAMESPACE ID CHAVE_L defClasse CHAVE_R','secaoNamespace',5,'p_secaoNamespace','analiseSintatica.py',13),
  ('defClasse -> PUBLIC CLASS ID CHAVE_L CHAVE_R','defClasse',5,'p_defClasse','analiseSintatica.py',15),
  ('defClasse -> CLASS ID CHAVE_L CHAVE_R','defClasse',4,'p_defClasse','analiseSintatica.py',16),
  ('defClasse -> PUBLIC CLASS ID CHAVE_L corpoClasse CHAVE_R','defClasse',6,'p_defClasse','analiseSintatica.py',17),
  ('defClasse -> CLASS ID CHAVE_L corpoClasse CHAVE_R','defClasse',5,'p_defClasse','analiseSintatica.py',18),
  ('defClasse -> PUBLIC CLASS ID CHAVE_L CHAVE_R defClasse','defClasse',6,'p_defClasse','analiseSintatica.py',19),
  ('defClasse -> CLASS ID CHAVE_L CHAVE_R defClasse','defClasse',5,'p_defClasse','analiseSintatica.py',20),
  ('defClasse -> CLASS ID CHAVE_L corpoClasse CHAVE_R defClasse','defClasse',6,'p_defClasse','analiseSintatica.py',21),
  ('defClasse -> PUBLIC CLASS ID CHAVE_L corpoClasse CHAVE_R defClasse','defClasse',7,'p_defClasse','analiseSintatica.py',22),
  ('corpoClasse -> atributo','corpoClasse',1,'p_corpoClasse','analiseSintatica.py',24),
  ('corpoClasse -> atributo corpoClasse','corpoClasse',2,'p_corpoClasse','analiseSintatica.py',25),
  ('corpoClasse -> assinatura','corpoClasse',1,'p_corpoClasse','analiseSintatica.py',26),
  ('corpoClasse -> assinatura corpoClasse','corpoClasse',2,'p_corpoClasse','analiseSintatica.py',27),
  ('atributo -> PUBLIC tipo atribuicao PONTO_VIRGULA','atributo',4,'p_atributo','analiseSintatica.py',29),
  ('atributo -> tipo atribuicao PONTO_VIRGULA','atributo',3,'p_atributo','analiseSintatica.py',30),
  ('atribuicao -> ID ATRIBUICAO ID','atribuicao',3,'p_atribuicao','analiseSintatica.py',32),
  ('atribuicao -> ID ATRIBUICAO INT','atribuicao',3,'p_atribuicao','analiseSintatica.py',33),
  ('atribuicao -> ID','atribuicao',1,'p_atribuicao','analiseSintatica.py',34),
  ('atribuicao -> ID ATRIBUICAO chamadaMetodo','atribuicao',3,'p_atribuicao','analiseSintatica.py',35),
  ('assinatura -> PUBLIC tipo ID PARENTESE_L parametrosFormais PARENTESE_R bloco','assinatura',7,'p_assinatura','analiseSintatica.py',38),
  ('assinatura -> tipo ID PARENTESE_L parametrosFormais PARENTESE_R bloco','assinatura',6,'p_assinatura','analiseSintatica.py',39),
  ('parametrosFormais -> tipo ID','parametrosFormais',2,'p_parametrosFormais','analiseSintatica.py',41),
  ('parametrosFormais -> tipo ID VIRGULA parametrosFormais','parametrosFormais',4,'p_parametrosFormais','analiseSintatica.py',42),
  ('corpoMetodo -> comandos','corpoMetodo',1,'p_corpoMetodo','analiseSintatica.py',44),
  ('corpoMetodo -> comandos corpoMetodo','corpoMetodo',2,'p_corpoMetodo','analiseSintatica.py',45),
  ('tipo -> INT','tipo',1,'p_tipo','analiseSintatica.py',47),
  ('tipo -> STRING','tipo',1,'p_tipo','analiseSintatica.py',48),
  ('tipo -> ID','tipo',1,'p_tipo','analiseSintatica.py',49),
  ('tipo -> BOOL','tipo',1,'p_tipo','analiseSintatica.py',50),
  ('chamadaMetodo -> ID PARENTESE_L parametrosReais PARENTESE_R','chamadaMetodo',4,'p_chamadaMetodo','analiseSintatica.py',52),
  ('parametrosReais -> ID','parametrosReais',1,'p_parametrosReais','analiseSintatica.py',54),
  ('parametrosReais -> ID VIRGULA parametrosReais','parametrosReais',3,'p_parametrosReais','analiseSintatica.py',55),
  ('parametrosReais -> INT','parametrosReais',1,'p_parametrosReais','analiseSintatica.py',56),
  ('parametrosReais -> INT VIRGULA parametrosReais','parametrosReais',3,'p_parametrosReais','analiseSintatica.py',57),
  ('comandos -> comandos1','comandos',1,'p_comandos','analiseSintatica.py',59),
  ('comandos -> comandos2','comandos',1,'p_comandos','analiseSintatica.py',60),
  ('comandos1 -> for1','comandos1',1,'p_comandos1','analiseSintatica.py',63),
  ('comandos1 -> foreach1','comandos1',1,'p_comandos1','analiseSintatica.py',64),
  ('comandos1 -> while1','comandos1',1,'p_comandos1','analiseSintatica.py',65),
  ('comandos1 -> return','comandos1',1,'p_comandos1','analiseSintatica.py',66),
  ('comandos1 -> atributo','comandos1',1,'p_comandos1','analiseSintatica.py',67),
  ('comandos1 -> IF PARENTESE_L exp1 PARENTESE_R comandos1 ELSE comandos1','comandos1',7,'p_comandos1','analiseSintatica.py',68),
  ('comandos1 -> IF PARENTESE_L exp1 PARENTESE_R bloco ELSE comandos1','comandos1',7,'p_comandos1','analiseSintatica.py',69),
  ('comandos1 -> IF PARENTESE_L exp1 PARENTESE_R comandos1 ELSE bloco','comandos1',7,'p_comandos1','analiseSintatica.py',70),
  ('comandos1 -> IF PARENTESE_L exp1 PARENTESE_R bloco ELSE bloco','comandos1',7,'p_comandos1','analiseSintatica.py',71),
  ('bloco -> CHAVE_L corpoComando CHAVE_R','bloco',3,'p_bloco','analiseSintatica.py',74),
  ('bloco -> CHAVE_L CHAVE_R','bloco',2,'p_bloco','analiseSintatica.py',75),
  ('comandos2 -> IF PARENTESE_L exp1 PARENTESE_R comandos','comandos2',5,'p_comandos2','analiseSintatica.py',77),
  ('comandos2 -> IF PARENTESE_L exp1 PARENTESE_R comandos1 ELSE comandos2','comandos2',7,'p_comandos2','analiseSintatica.py',78),
  ('comandos2 -> IF PARENTESE_L exp1 PARENTESE_R bloco','comandos2',5,'p_comandos2','analiseSintatica.py',79),
  ('comandos2 -> IF PARENTESE_L exp1 PARENTESE_R bloco ELSE comandos2','comandos2',7,'p_comandos2','analiseSintatica.py',80),
  ('comandos2 -> for2','comandos2',1,'p_comandos2','analiseSintatica.py',81),
  ('comandos2 -> while2','comandos2',1,'p_comandos2','analiseSintatica.py',82),
  ('comandos2 -> foreach2','comandos2',1,'p_comandos2','analiseSintatica.py',83),
  ('corpoComando -> comandos','corpoComando',1,'p_corpoComando','analiseSintatica.py',85),
  ('corpoComando -> corpoComando comandos','corpoComando',2,'p_corpoComando','analiseSintatica.py',86),
  ('for1 -> FOR PARENTESE_L tipo atribuicao PONTO_VIRGULA exp1 PONTO_VIRGULA exp1 PARENTESE_R bloco','for1',10,'p_for1','analiseSintatica.py',88),
  ('for1 -> FOR PARENTESE_L atribuicao PONTO_VIRGULA exp1 PONTO_VIRGULA exp1 PARENTESE_R bloco','for1',9,'p_for1','analiseSintatica.py',89),
  ('for1 -> FOR PARENTESE_L tipo atribuicao PONTO_VIRGULA exp1 PONTO_VIRGULA exp1 PARENTESE_R comandos1','for1',10,'p_for1','analiseSintatica.py',90),
  ('for1 -> FOR PARENTESE_L atribuicao PONTO_VIRGULA exp1 PONTO_VIRGULA exp1 PARENTESE_R comandos1','for1',9,'p_for1','analiseSintatica.py',91),
  ('for2 -> FOR PARENTESE_L tipo atribuicao PONTO_VIRGULA exp1 PONTO_VIRGULA exp1 PARENTESE_R comandos2','for2',10,'p_for2','analiseSintatica.py',93),
  ('for2 -> FOR PARENTESE_L atribuicao PONTO_VIRGULA exp1 PONTO_VIRGULA exp1 PARENTESE_R comandos2','for2',9,'p_for2','analiseSintatica.py',94),
  ('while1 -> WHILE PARENTESE_L exp1 PARENTESE_R bloco','while1',5,'p_while1','analiseSintatica.py',96),
  ('while1 -> WHILE PARENTESE_L exp1 PARENTESE_R comandos1','while1',5,'p_while1','analiseSintatica.py',97),
  ('while2 -> WHILE PARENTESE_L exp1 PARENTESE_R comandos2','while2',5,'p_while2','analiseSintatica.py',99),
  ('foreach1 -> FOREACH PARENTESE_L tipo ID IN ID PARENTESE_R bloco','foreach1',8,'p_foreach1','analiseSintatica.py',101),
  ('foreach1 -> FOREACH PARENTESE_L ID IN ID PARENTESE_R bloco','foreach1',7,'p_foreach1','analiseSintatica.py',102),
  ('foreach1 -> FOREACH PARENTESE_L tipo ID IN ID PARENTESE_R comandos1','foreach1',8,'p_foreach1','analiseSintatica.py',103),
  ('foreach1 -> FOREACH PARENTESE_L ID IN ID PARENTESE_R comandos1','foreach1',7,'p_foreach1','analiseSintatica.py',104),
  ('foreach2 -> FOREACH PARENTESE_L tipo ID IN ID PARENTESE_R comandos2','foreach2',8,'p_foreach2','analiseSintatica.py',106),
  ('foreach2 -> FOREACH PARENTESE_L ID IN ID PARENTESE_R comandos2','foreach2',7,'p_foreach2','analiseSintatica.py',107),
  ('return -> RETURN ID PONTO_VIRGULA','return',3,'p_return','analiseSintatica.py',109),
  ('return -> RETURN INT PONTO_VIRGULA','return',3,'p_return','analiseSintatica.py',110),
  ('return -> RETURN PONTO_VIRGULA','return',2,'p_return','analiseSintatica.py',111),
  ('exp1 -> exp1 ATRIBUICAO exp2','exp1',3,'p_exp1','analiseSintatica.py',113),
  ('exp1 -> exp2','exp1',1,'p_exp1','analiseSintatica.py',114),
  ('exp2 -> exp2 OR exp3','exp2',3,'p_exp2','analiseSintatica.py',116),
  ('exp2 -> exp3','exp2',1,'p_exp2','analiseSintatica.py',117),
  ('exp3 -> exp3 AND exp4','exp3',3,'p_exp3','analiseSintatica.py',119),
  ('exp3 -> exp4','exp3',1,'p_exp3','analiseSintatica.py',120),
  ('exp4 -> exp4 BIT_OR exp5','exp4',3,'p_exp4','analiseSintatica.py',122),
  ('exp4 -> exp5','exp4',1,'p_exp4','analiseSintatica.py',123),
  ('exp5 -> exp5 XOR exp6','exp5',3,'p_exp5','analiseSintatica.py',125),
  ('exp5 -> exp6','exp5',1,'p_exp5','analiseSintatica.py',126),
  ('exp6 -> exp6 BIT_AND exp7','exp6',3,'p_exp6','analiseSintatica.py',128),
  ('exp6 -> exp7','exp6',1,'p_exp6','analiseSintatica.py',129),
  ('exp7 -> exp7 IGUAL exp8','exp7',3,'p_exp7','analiseSintatica.py',131),
  ('exp7 -> exp7 DIFERENTE exp8','exp7',3,'p_exp7','analiseSintatica.py',132),
  ('exp7 -> exp8','exp7',1,'p_exp7','analiseSintatica.py',133),
  ('exp8 -> exp8 MENOR exp9','exp8',3,'p_exp8','analiseSintatica.py',135),
  ('exp8 -> exp8 MENOR_IGUAL exp9','exp8',3,'p_exp8','analiseSintatica.py',136),
  ('exp8 -> exp8 MAIOR exp9','exp8',3,'p_exp8','analiseSintatica.py',137),
  ('exp8 -> exp8 MAIOR_IGUAL exp9','exp8',3,'p_exp8','analiseSintatica.py',138),
  ('exp8 -> exp9','exp8',1,'p_exp8','analiseSintatica.py',139),
  ('exp9 -> exp9 SOMA exp10','exp9',3,'p_exp9','analiseSintatica.py',141),
  ('exp9 -> exp9 SUB exp10','exp9',3,'p_exp9','analiseSintatica.py',142),
  ('exp9 -> exp10','exp9',1,'p_exp9','analiseSintatica.py',143),
  ('exp10 -> exp10 MUL exp11','exp10',3,'p_exp10','analiseSintatica.py',145),
  ('exp10 -> exp10 DIV exp11','exp10',3,'p_exp10','analiseSintatica.py',146),
  ('exp10 -> exp11','exp10',1,'p_exp10','analiseSintatica.py',147),
  ('exp11 -> BIT_NOT exp12','exp11',2,'p_exp11','analiseSintatica.py',149),
  ('exp11 -> NOT exp12','exp11',2,'p_exp11','analiseSintatica.py',150),
  ('exp11 -> exp12','exp11',1,'p_exp11','analiseSintatica.py',151),
  ('exp12 -> exp12 INCREMENTO','exp12',2,'p_exp12','analiseSintatica.py',153),
  ('exp12 -> exp12 DECREMENTO','exp12',2,'p_exp12','analiseSintatica.py',154),
  ('exp12 -> exp13','exp12',1,'p_exp12','analiseSintatica.py',155),
  ('exp13 -> TRUE','exp13',1,'p_exp13','analiseSintatica.py',157),
  ('exp13 -> FALSE','exp13',1,'p_exp13','analiseSintatica.py',158),
  ('exp13 -> STRING','exp13',1,'p_exp13','analiseSintatica.py',159),
  ('exp13 -> ID','exp13',1,'p_exp13','analiseSintatica.py',160),
  ('exp13 -> chamadaMetodo','exp13',1,'p_exp13','analiseSintatica.py',161),
  ('exp13 -> INT','exp13',1,'p_exp13','analiseSintatica.py',162),
  ('exp13 -> PARENTESE_L exp1 PARENTESE_R','exp13',3,'p_exp13','analiseSintatica.py',163),
]
