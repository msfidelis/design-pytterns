class Desconto_por_cinco_itens(object):

	def __init__(self):
		self._proximo_desconto = None

  	def adicionar_proximo_desconto(self, proximo_desconto):
  		self.__proximo_desconto = proximo_desconto

  	def calcular(orcamento):

	    if (orcamento.total_itens > 5):
	        return orcamento.valor * 0.1
	    else: 
	      return self._proximo_desconto.calcular(orcamento)


class Desconto_por_mais_de_quinhetos_reais(object): 

	def adicionar_proximo_desconto(self, proximo_desconto):
		self.__proximo_desconto = proximo_desconto

	def __init__(self):
		self._proximo_desconto = None

  	def calcular(orcamento):

	    if(orcamento.valor > 500):
	      return orcamento.valor * 0.07
	    else:
	      return self._proximo_desconto.calcular(orcamento)

class Sem_desconto(object):

	def calcula(self, orcamento):
		return 0