from abc import abstractmethod
from abc import ABCMeta
from visitor import visitor

class programa(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class programaConcrete(programa):
  def __init__(self, programa, decl):
    self.programa = programa
    self.decl = decl

####

class secaoUsing(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class secaoUsingConcrete(secaoUsing):
  def __init__(self, using, id, secaoUsing):
    self.using = using
    self.id = id
    self.secaoUsing = secaoUsing

###
class secaoNamespace(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class secaoNamespaceConcrete(secaoNamespace):
  def __init__(self, namespace, id, decl):
    self.namespace = namespace
    self.id = id  
    self.decl = decl

###
    
class defClass(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class defClassConcrete(defClass):
  def __init__(self, public, Class, id, corpoClass, defClass):
    self.public = public
    self.Classlass = Class
    self.id = id
    self.corpoClass = corpoClass
    self.defClass = defClass

###

class corpoClass(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class corpoClassConcrete(corpoClass):
  def __init__(self, atributo, assinatura, corpoClass):
    self.atributo = atributo
    self.assinatura = assinatura
    self.corpoClass = corpoClass

###

class atributo(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class atributoConcrete(atributo):
  def __init__(self, public, tipo, atribuicao):
    self.public = public
    self.tipo = tipo
    self.atribuicao = atribuicao

###

class atribuicao(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class atribuicaoConcrete(atribuicao):
  def __init__(self, id, atribuicao, int, chamadaMetodo):
    self.atribuicao = atribuicao
    self.id = id
    self.int = int
    self.chamadaMetodo = chamadaMetodo


###
class assinatura(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class assinaturaConcrete(assinatura):
  def __init__(self, public, tipo, id, parametrosFormais, bloco):
    self.public = public
    self.tipo = tipo
    self.id = id
    self.parametrosFormais = parametrosFormais
    self.bloco = bloco

###

class parametrosFormais(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class parametrosFormaisConcrete(parametrosFormais):
  def __init__(self, tipo, id, virgula, parametrosFormais):
    self.tipo = tipo
    self.id = id
    self.virgula = virgula
    self.parametrosFormais = parametrosFormais

  

###
class corpoMetodo(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class corpoMetodoConcrete(corpoMetodo):
  def __init__(self, comando, corpoComando):
    self.comando = comando
    self.corpoComando = corpoComando

###

class tipo(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class tipoConcrete(tipo):
  def __init__(self, int, string, id, bool):
    self.int = int
    self.string = string
    self.id = id
    self.bool =bool

###

class chamadaMetodo(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class chamadaMetodoConcrete(chamadaMetodo):
  def __init__(self, id, parametrosReais):
    self.id = id
    self.parametrosReais = parametrosReais

###
class parametrosReais(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class parametrosReaisConcrete(parametrosReais):
  def __init__(self, id, int, virgula, parametrosReais):
    self.id = id
    self.int = int
    self.virgula = virgula
    self.parametrosReais = parametrosReais

###

class comandos(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class comandosConcrete(comandos):
  def __init__(self, comandos1, comandos2):
    self.comandos1 = comandos1
    self.comandos2 = comandos2

###
class comandos1(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class comandos1Concrete(comandos1):
  def __init__(self, for1, foreach1, while1, Return, IF, exp1, ELSE, bloco ):
    self.for1 = for1
    self.foreach1 = foreach1
    self.while1 = while1
    self.Return = Return
    self.IF = IF
    self.exp1 = exp1
    self.ELSE = ELSE
    self.bloco = bloco

###
class bloco(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class blocoConcrete(bloco):
  def __init__(self, bloco):
    self.bloco = bloco

###
class comandos2(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class comandos2Concrete(comandos2):
  def __init__(self, IF, exp1, comandos, comandos1, comandos2, bloco, ELSE):
    self.IF = IF
    self.exp1 = exp1
    self.comandos = comandos
    self.comandos1 = comandos1
    self.comandos2 = comandos2
    self.bloco = bloco
    self.ELSE = ELSE
    

###
class corpoComando(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class corpoComandoConcrete(corpoComando):
  def __init__(self, comandos, corpoComandos):
    self.comandos = comandos
    self.corpoComando = corpoComando

###
class for1(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class for1Concrete(for1):
  def __init__(self, FOR, tipo, atribuicao, exp1, bloco, comandos1):
    self.FOR = FOR
    self.tipo = tipo
    self.atribuicao = atribuicao
    self.exp1 = exp1
    self.bloco = bloco
    self.comandos1 = comandos1

###
class for2(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class for2Concrete(for2):
  def __init__(self, FOR, tipo, atribuicao, exp1, comandos2):
    self.FOR = FOR
    self.tipo = tipo
    self.atribuicao = atribuicao
    self.exp1 = exp1
    self.comandos1 = comandos2

###

class while1(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class while1Concrete(while1):
  def __init__(self, WHILE, exp1, bloco, comandos1):
    self.WHILE = WHILE
    self.exp1 = exp1
    self.bloco = bloco
    self.comandos1 = comandos1

###
class while2(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class while2Concrete(while2):
  def __init__(self, WHILE, exp1, comandos2):
    self.WHILE = WHILE
    self.exp1 = exp1
    self.comandos1 = comandos2


###
class foreach1(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class foreach1Concrete(foreach1):
  def __init__(self, FOREACH, tipo, id, IN, comandos1, bloco):
    self.FOREACH = FOREACH
    self.tipo = tipo
    self.bloco = bloco
    self.comandos1 = comandos1
    self.IN = IN
    self.id = id

###
class foreach2(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class foreach2Concrete(foreach2):
  def __init__(self, FOREACH, tipo, id, IN, comandos2):
    self.FOREACH = FOREACH
    self.tipo = tipo
    self.comandos2 = comandos2
    self.IN = IN
    self.id = id

###
class Return(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ReturnConcrete(Return):
  def __init__(self, RETURN , id):
    self.RETURN = RETURN
    self.id = id

###
class exp1_atribuicao(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp1_atribuicaoConcrete(exp1_atribuicao):
  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2

###
class exp2_or(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp2_orConcrete(exp2_or):
  def __init__(self, exp2, exp3):
    self.exp2 = exp2
    self.exp3 = exp3

###
class exp3_and(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp3_andConcrete(exp3_and):
  def __init__(self, exp3, exp4):
    self.exp4 = exp4
    self.exp3 = exp3

###
class exp4_bit_or(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp4_bit_orConcrete(exp4_bit_or):
  def __init__(self, exp4, exp5):
    self.exp4 = exp4
    self.exp5 = exp5

###

class exp5_xor(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp5_xorConcrete(exp5_xor):
  def __init__(self, exp5, exp6):
    self.exp5 = exp5
    self.exp6 = exp6

###
class exp6_bit_and(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp6_bit_andConcrete(exp6_bit_and):
  def __init__(self, exp6, exp7):
    self.exp6 = exp6
    self.exp7 = exp7
###
    
class exp7(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp7Concrete(exp7):
  def __init__(self, exp2, exp3):
    self.exp2 = exp2
    self.exp3 = exp3

###
    
class exp7_dif(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass
    
class exp7_difConcrete(exp7):
  def __init__(self, exp7, exp8):
    self.exp7 = exp7
    self.exp8 = exp8

###

class exp7_igual(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp7_igualConcrete(exp7):
  def __init__(self, exp7, exp8):
    self.exp7 = exp7
    self.exp8 = exp8

###
class exp8(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp8Concrete(exp8):
  def __init__(self, exp8, exp9):
    self.exp8 = exp8
    self.exp9 = exp9

###

class exp8_menor(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp8_menorConcrete(exp8):
  def __init__(self, exp8, exp9):
    self.exp8 = exp8
    self.exp9 = exp9

###
class exp8_menor_igual(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp8_menor_igualConcrete(exp8):
  def __init__(self, exp8, exp9):
    self.exp8 = exp8
    self.exp9 = exp9

###
class exp8_maior(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp8_maiorConcrete(exp8):
  def __init__(self, exp8, exp9):
    self.exp8 = exp8
    self.exp9 = exp9

###

class exp8_maior_igual(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp8_maior_igualConcrete(exp8):
  def __init__(self, exp8, exp9):
    self.exp8 = exp8
    self.exp9 = exp9

###

class exp9(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp9Concrete(exp9):
  def __init__(self, exp9, exp10):
    self.exp9 = exp9
    self.exp10 = exp10

###

class exp9_sub(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp9_subConcrete(exp9):
  def __init__(self, exp9, exp10):
    self.exp9 = exp9
    self.exp10 = exp10

###

class exp9_soma(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp9_somaConcrete(exp9):
  def __init__(self, exp9, exp10):
    self.exp9 = exp9
    self.exp10 = exp10

###

class exp10(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp10Concrete(exp10):
  def __init__(self, exp10, exp11):
    self.exp10 = exp10
    self.exp11 = exp11

###

class exp10_mul(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp10_mulConcrete(exp10):
  def __init__(self, exp10, exp11):
    self.exp10 = exp10
    self.exp11 = exp11

###

class exp10_div(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp10_divConcrete(exp10):
  def __init__(self, exp10, exp11):
    self.exp10 = exp10
    self.exp11 = exp11

###

class exp11(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp11Concrete(exp11):
  def __init__(self, exp11, exp12):
    self.exp11 = exp11
    self.exp12 = exp12

###

class exp11_bit_not(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp11_bit_notConcrete(exp11):
  def __init__(self, exp11, exp12):
    self.exp11 = exp11
    self.exp12 = exp12

###

class exp11_not(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp11_notConcrete(exp11):
  def __init__(self, exp11, exp12):
    self.exp11 = exp11
    self.exp12 = exp12

###

class exp12(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp12Concrete(exp12):
  def __init__(self, exp12, exp13):
    self.exp12 = exp12
    self.exp13 = exp13

###

class exp12_decremento(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp12_decrementoConcrete(exp12):
  def __init__(self, exp12, exp13):
    self.exp12 = exp12
    self.exp13 = exp13

###

class exp12_incremento(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp12_incrementoConcrete(exp12):
  def __init__(self, exp12, exp13):
    self.exp12 = exp12
    self.exp13 = exp13

###

class exp13(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class exp13Concrete(exp13):
  def __init__(self, exp1):
    self.exp1 = exp1

###