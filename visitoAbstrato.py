from abc import abstractmethod
from abc import ABCMeta

class visitor_abstract(metaclass=ABCMeta):

    @abstractmethod
    def visit_programaConcrete(self, programaConcrete):
        pass

    @abstractmethod
    def visit_secaoUsingConcrete(self, secaoUsingConcrete):
        pass
      
    @abstractmethod
    def visit_secaoNamespaceConcrete(self, secaoNamespaceConcretesecaoUsingConcrete):
        pass

    @abstractmethod
    def visit_defClassConcrete(self, defClassConcrete):
        pass

    @abstractmethod
    def visit_corpoClassConcrete(self, corpoClassConcrete):
        pass

    @abstractmethod
    def visit_atributoConcrete(self, atributoConcrete):
        pass

    @abstractmethod
    def visit_atribuicaoConcrete(self, atribuicaoConcrete):
        pass

    @abstractmethod
    def visit_assinaturaConcrete(self, assinaturaConcrete):
        pass

    @abstractmethod
    def visit_parametrosFormaisConcrete(self, parametrosFormaisConcrete):
        pass

    @abstractmethod
    def visit_corpoMetodoConcrete(self, corpoMetodoConcrete):
        pass

    @abstractmethod
    def visit_tipoConcrete(self, tipoConcrete):
        pass

    @abstractmethod
    def visit_chamadaMetodoConcrete(self, chamadaMetodoConcrete):
        pass

    @abstractmethod
    def visit_parametrosReaisConcrete(self, parametrosReaisConcrete):
        pass

    @abstractmethod
    def visit_comandosConcrete(self, comandosConcrete):
        pass

    @abstractmethod
    def visit_comandos1Concrete(self, comandos1Concrete):
        pass

    @abstractmethod
    def visit_blocoConcrete(self, blocoConcrete):
        pass

    @abstractmethod
    def visit_comandos2Concrete(self, comandos2Concrete):
        pass

    @abstractmethod
    def visit_corpoComandoConcrete(self, corpoComandoConcrete):
        pass

    @abstractmethod
    def visit_for1Concrete(self, for1Concrete):
        pass

    @abstractmethod
    def visit_for2Concrete(self, for2Concrete):
        pass

    @abstractmethod
    def visit_while1Concrete(self, while1Concrete):
        pass

    @abstractmethod
    def visit_while2Concrete(self, while2Concrete):
        pass

    @abstractmethod
    def visit_foreach1Concrete(self, foreach1Concrete):
        pass

    @abstractmethod
    def visit_foreach2Concrete(self, foreach2Concrete):
        pass

    @abstractmethod
    def visit_ReturnConcrete(self, ReturnConcrete):
        pass

    @abstractmethod
    def exp1_atribuicaoConcrete(self, exp1_atribuicaoConcrete):
        pass

    @abstractmethod
    def visit_exp2_orConcrete(self, exp2_orConcrete):
        pass

    @abstractmethod
    def visit_exp3_andConcrete(self, exp3_andConcrete):
        pass

    @abstractmethod
    def visit_exp4_bit_orConcrete(self, exp4_bit_orConcrete):
        pass

    @abstractmethod
    def visit_exp5_xorConcrete(self, exp5_xorConcrete):
        pass

    @abstractmethod
    def visit_exp6_bit_andConcrete(self, exp6_bit_andConcrete):
        pass

    @abstractmethod
    def visit_exp7Concrete(self, exp7Concrete):
        pass

    @abstractmethod
    def visit_exp7_difConcrete(self, exp7_difConcrete):
        pass

    @abstractmethod
    def visit_exp7_igualConcrete(self, exp7_igualConcrete):
        pass

    @abstractmethod
    def visit_exp8Concrete(self, exp8Concrete):
        pass

    @abstractmethod
    def visit_exp8_menorConcrete(self, exp8_menorConcrete):
        pass

    @abstractmethod
    def visit_exp8_menor_igualConcrete(self, exp8_menor_igualConcrete):
        pass

    @abstractmethod
    def visit_exp8_maiorConcrete(self, exp8_maiorConcrete):
        pass

    @abstractmethod
    def visit_exp8_maior_igualConcrete(self, exp8_maior_igualConcrete):
        pass

    @abstractmethod
    def visit_exp9Concrete(self, exp9Concrete):
        pass

    @abstractmethod
    def visit_exp9_subConcrete(self, exp9_subConcrete):
        pass

    @abstractmethod
    def visit_exp9_somaConcrete(self, exp9_somaConcrete):
        pass

    @abstractmethod
    def visit_exp10Concrete(self, exp10Concrete):
        pass

    @abstractmethod
    def visit_exp10_mulConcrete(self, exp10_mulConcrete):
        pass

    @abstractmethod
    def visit_exp10_divConcrete(self, exp10_divConcrete):
        pass

    @abstractmethod
    def visit_exp11Concrete(self, exp11Concrete):
        pass

    @abstractmethod
    def visit_exp11_bit_notConcrete(self, exp11_bit_notConcrete):
        pass

    @abstractmethod
    def visit_exp11_notConcrete(self, exp11_notConcrete):
        pass

    @abstractmethod
    def visit_exp12Concrete(self, exp12Concrete):
        pass

    @abstractmethod
    def visit_exp12_decrementoConcrete(self, exp12_decrementoConcrete):
        pass

    @abstractmethod
    def visit_exp12_incrementoConcrete(self, exp12_incrementoConcrete):
        pass

    @abstractmethod
    def visit_exp13Concrete(self, exp13Concrete):
        pass



