# -*- coding: utf-8 -*-

from datetime import date

from abc import ABCMeta, abstractmethod

##
#
##
class Pedido(object):

    def __init__(self, cliente, valor):

        self.__cliente = cliente
        self.__valor = valor
        self.__status = 'NOVO'
        self.__data_finalizacao = None

    def paga(self):
        self.__status = 'PAGO'

    def finaliza(self):
        self.__data_finalizacao = date.today()
        self.__status = 'ENTREGUE'

    @property
    def cliente(self):
        return self.__cliente

    @property
    def valor(self):
        return self.__valor

    @property
    def status(self):
        return self.__status

    @property
    def data_finalizacao(self):
        return self.__data_finalizacao

##
# Abstract Class dos Comandos
##
class Comando(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def executa(self):
        pass

##
# Comando - Conclui Pedido
##
class Conclui_pedido(Comando):

    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.finaliza()

class Paga_pedido(Comando):

    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.paga()
##
# Classe que gerencia um Workflow de Comandos
##
class Fila_de_trabalho(object):

    def __init__(self):
        self.__pedidos = []
        self.__comandos = []

    def adiciona(self, comando):
        self.__comandos.append(comando)

    def processa(self):
        for comando in self.__comandos:
            comando.executa()

if __name__ == '__main__':

    pedido1 = Pedido("Ben 10", 200)
    pedido2 = Pedido("Sabre de Luz", 300)

    comando1 = Conclui_pedido(pedido1)
    comando2 = Paga_pedido(pedido2)
    comando3 = Paga_pedido(pedido2)

    fila_de_trabalho = Fila_de_trabalho()

    fila_de_trabalho.adiciona(comando1)
    fila_de_trabalho.adiciona(comando2)
    fila_de_trabalho.adiciona(comando3)

    fila_de_trabalho.processa()



