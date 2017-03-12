# -*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod

##
# Templated Method de Taxas condicionais
# implementa as classes e métodos abstratos
# em todas as classes que herdarem a mesma
##
class Template_de_imposto_condicional(object):
	__metaclass__ = ABCMeta

	def calcula(self, orcamento):

		if self.deve_usar_maxima_taxacao(orcamento):
			return self.maxima_taxacao(orcamento)
		else:
			return self.minima_taxacao(orcamento)

	@abstractmethod
	def deve_usar_maxima_taxacao(self, orcamento):
		pass

	@abstractmethod
	def maxima_taxacao(self, orcamento):
		pass

	@abstractmethod
	def minima_taxacao(self, orcamento):
		pass

##
# Classe de calculo de ICMS sobre o valor do orçamento
##
class ICMS(object):
	def calcula(self, orcamento):
		return orcamento.valor * 0.1
##
# Classe de calculo de ISS sobre o valor do orçamento
##	
class ISS(object):
	def calcula(self, orcamento):
		return orcamento.valor * 0.06

##
# Classe de calculo de ICPP sobre o valor do orçamento
##
class ICPP(Template_de_imposto_condicional):

	def calcula(self, orcamento):
			if orcamento.valor > 500:
				return orcamento.valor * 0.07
			else:
				return orcamento.valor * 0.05

	def deve_usar_maxima_taxacao(self, orcamento):
		if orcamento.valor > 500:
			return True
		else:
			return False

	def maxima_taxacao(self, orcamento):
		return orcamento.valor * 0.07

	def minima_taxacao(self, orcamento):
		return orcamento.valor * 0.05

##
# Classe de calculo de IKCV sobre o valor do orçamento
##
class IKCV(Template_de_imposto_condicional):

	def deve_usar_maxima_taxacao(self, orcamento):
		return orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento)

	def maxima_taxacao(self, orcamento):
		return orcamento.valor * 0.10

	def minima_taxacao(self, orcamento):
		return orcamento.valor * 0.06

	def __tem_item_maior_que_100_reais(self, orcamento):
		for item in orcamento.obter_itens():
			if(item.valor > 100):
				return True
		return False
