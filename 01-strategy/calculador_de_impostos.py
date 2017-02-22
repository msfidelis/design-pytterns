# -*- coding: UTF-8 -*-

class Calculador_De_Impostos(object):

	def realiza_calculo(self, orcamento, calcula_imposto):
		valor = calcula_imposto(orcamento)
		print valor



if __name__ == '__main__':

	from orcamento import Orcamento
	from impostos import ISS, ICMS

	orcamento = Orcamento(500)
	calculador_de_impostos = Calculador_De_Impostos()
	calculador_de_impostos.realiza_calculo(orcamento, ISS().calcula)
	calculador_de_impostos.realiza_calculo(orcamento, ICMS().calcula)