from analiseLexica import *
from analiseSintatica import *
lexer = lex.lex()

teste1 = '''using System;
            using std;
            namespace reinan{
              public class classe{

              }

            }'''
teste2 = '''using System;
            using std;
            namespace reinan{
              public class classe1{

              }
              public class classe2{

              }
              class classe3{

              }
              class classe4{

              }

            }'''
teste3 = '''using System;
            using std;
            namespace reinan{
              public class classe1{
                public int numero1 = 2;
                public int numero2 = 10;
                public int numero3 = 1;
                public int numero4 = 2;
              }
            }'''
teste4 = '''using System;
            using std;
            public class classe1{
              int numero1 = 2;
              public int numero2 = 10;
              int numero3;
              public int numero4;
            }
            '''
teste5 = '''using System;
            using std;
            public class classe1{
              int numero1 = 2;
              public int numero2 = 10;
              int numero3;
              public int numero4;
              int metodo1(int a, int b){
                int a = funcao(a,b);
                while(!false){
                  return 1;
                }
                while(a++)
                  return 2;
                
                foreach (int listaNum in elementoLista){
                  int a = elementoLista;
                  public int b = elementoLista; 
                  return elementoLista;
                }
              }
              public int metodo2(int a){
                for(int i = 8 ; i >= 10 ; i++){
                return 1;
                }
                while(a > 2){
                return 1;
                }
                while(a < 2){
                return 2;
                }
                for(int a = 1 ; a < 10 ; a--){
                  while(true){
                    for(int z = 1 ; z < 2 ; z++){
                      return 0;
                    }
                    return ;
                  }
                }
              }
            }
            '''
teste6 = '''using System;
            using std;
            public class classe1{
              
              int metodo1(int a, int b){
                int a = a;
                for(a = 2 ; a < 1 ; a++) return 1;
                foreach (int listaNum in elementoLista){
                  int a = elementoLista;
                  if(a>2){
                    return;
                  }else{
                    while(a>2)return;
                    while(false){
                      int a;
                    }
                    int a = 2;
                    return elementoLista;
                  }
                }
              }
            }
            '''


lexer.input(teste5)
parser = yacc.yacc()
result = parser.parse(debug=False)
print ("realiza a analise semantica")