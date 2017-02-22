class DescontoPorCincoItens(object):

	def calcula(self, orcamento):

		if orcamento.total_itens > 5:
			return orcamento.valor * 0.1
		else:
			return 0


class DescontoParaValoresMaioresQueQuinhentosReais(object):

	def calcula(self, orcamento):

		if orcamento.valor > 500:
			return orcamento.valor * 0.07
		else:
			return 0