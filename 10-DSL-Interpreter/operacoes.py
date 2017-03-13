# -*- coding: utf-8 -*-

# DSL Domain Design Language

from abc import ABCMeta, abstractmethod

##
# Abstract Class de Expressão
# obriga a implementação do método Avalia()
##
class Expressao(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def avalia(self):
		pass

##
# Classe responsável pela subtração
##
class Subtracao(Expressao):

	def __init__(self, expressao_esquerda, expressao_direita):
		self.__expressao_esquerda = expressao_esquerda
		self.__expressao_direita = expressao_direita

	def avalia(self):
		return self.__expressao_esquerda.avalia() - self.__expressao_direita.avalia()

##
# Classe responsável pela soma
##
class Soma(Expressao):

	def __init__(self, expressao_esquerda, expressao_direita):
		self.__expressao_esquerda = expressao_esquerda
		self.__expressao_direita = expressao_direita

	def avalia(self):
		return self.__expressao_esquerda.avalia() + self.__expressao_direita.avalia()

##
# Objeto de representação de um número
##
class Numero(Expressao):

	def __init__(self, numero):
		self.__numero = numero

	def avalia(self):
		return self.__numero


if __name__ == "__main__":

	print Soma(Numero(10), Numero(30)).avalia()

	expressao_esquerda = Soma(Numero(40), Numero(120))
	expressao_direita = Subtracao(Numero(50), Numero(20))

	print Soma(expressao_esquerda, expressao_direita).avalia()
