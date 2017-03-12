# -*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod

##
# Abstract Class - Estado dos Orçamentos
##
class Estado_de_um_orcamento(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass

    @abstractmethod
    def aprova(self, orcamento):
        pass

    @abstractmethod
    def reprova(self, orcamento):
        pass

    @abstractmethod
    def finaliza(self, orcamento):
        pass
##
# State: Em aprovação
##
class Em_aprovacao(Estado_de_um_orcamento):

    def aplica_desconto_extra(self, orcamento):
        if orcamento.total_desconto > 0:
            raise Exception("Desconto já aplicado")
        else:
            orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)

    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()
        
    def finaliza(self, orcamento):
        raise Exception("Orçamentos em aprovação não podem ser finalizados")

##
# State: Aprovado
##
class Aprovado(Estado_de_um_orcamento):

    def aplica_desconto_extra(self, orcamento):
        
        if orcamento.total_desconto > 0:
            raise Exception("Desconto já aplicado")
        else:
            orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)

    def aprova(self, orcamento):
        raise Exception("Orçamento já aprovado")

    def reprova(self, orcamento):
        raise Exception("Orçamentos aprovados não podem ser reprovados")
        
    def finaliza(self, orcamento):
       orcamento.estado_atual = Finalizado()

##
# State: Reprovado
##
class Reprovado(Estado_de_um_orcamento):

    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos reprovados não recebem desconto extra')

    def aprova(self, orcamento):
        raise Exception("Orçamentos reprovados não podem ser aprovados")

    def reprova(self, orcamento):
        raise Exception("Orçamento já reprovado")
        
    def finaliza(self, orcamento):
       orcamento.estado_atual = Finalizado()

##
# State: Finalizado
##
class Finalizado(Estado_de_um_orcamento):

    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos reprovados não recebem desconto extra')

    def aprova(self, orcamento):
        raise Exception("Orçamentos finalizado não podem ser aprovados")

    def reprova(self, orcamento):
        raise Exception("Orçamentos finalizado não podem ser reprovados")
        
    def finaliza(self, orcamento):
        raise Exception("Orçamentos finalizado não podem ser finalizados novamente")


##
# Classe de Orçamento
##
class Orcamento(object):

    def __init__(self):
        self.__itens = []
        self.estado_atual = Em_aprovacao()
        self.__desconto_extra = 0

    ##
    # Retorna o valor total do orçamento
    # menos o valor de descontos existentes
    ##
    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total+= item.valor

        return total - self.__desconto_extra
    ##
    # Retorna a quantidade de itens
    # no Orçamento
    ##
    @property
    def total_itens(self):
        return len(self.__itens)

    ##
    # Retorna o total de desconto existente
    # no orçamento
    ##
    @property
    def total_desconto(self):
        return self.__desconto_extra;

    ##
    # Retorna todos os itens do orçamento
    ##
    def obter_itens(self):
        return tuple(self.__itens)

    ##
    # Adiciona um item ao orçamento
    ##
    def adiciona_item(self, item):
        self.__itens.append(item)

    ##
    # Aplica um desconto a mais no valor dependendo do estado 
    # de aprovação do orçamento
    ##
    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)

    ##
    # Soma um valor de desconto ao total de desconto existente
    # no Orcamento
    ##
    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto

    ##
    #
    ##
    def aprova(self):
        self.estado_atual.aprova(self)

    ##
    #
    ##
    def reprova(self):
        self.estado_atual = Reprovado()

    ##
    #
    ##
    def finaliza(self):
        self.estado_atual = Finalizado()

##
# Classe de representação de um Orçamento
##
class Item(object):

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome


# Teste

if __name__ == '__main__':
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM 1', 50))
    orcamento.adiciona_item(Item('ITEM 2', 200))
    orcamento.adiciona_item(Item('ITEM 3', 250))

    print orcamento.valor

    orcamento.aprova()

    orcamento.aplica_desconto_extra()

    print orcamento.valor






