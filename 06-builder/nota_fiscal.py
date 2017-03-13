# -*- coding: UTF-8 -*-

from datetime import date

##
# Objeto de Representação de um Item da Nota Fiscal
##
class Item(object):

	def __init__(self, descricao, valor):
		self.__descricao = descricao
		self.__valor = valor

	@property
	def descricao(self):
		return self.__descricao

	@property
	def valor(self):
		return self.__valor

##
# Objeto de Representação de uma Nota Fiscal
##
class Nota_fiscal(object):

	##
	# Os parâmetros opcionais da classe devem ficar por ultimo no construtor
	# ou em qualquer método
	##
	def __init__(self, razao_social, cnpj, itens, data_de_emissao=date.today(), detalhes=''):
		self.__razao_social = razao_social
		self.__cnpj = cnpj
		self.__data_de_emissao = data_de_emissao
		self.__itens = itens

		if len(detalhes) > 12:
			raise Exception("Detalhes da nota não podem ser maiores que 20 caracteres")
		else:
			self.__detalhes = detalhes

	@property
	def razao_social(self):
		return self.__razao_social

	@property
	def cnpj(self):
		return self.__cnpj

	@property
	def data_de_emissao(self):
		return self.__data_de_emissao

	@property
	def itens(self):
		return self.__itens


	@property
	def detalhes(self):
		return self.__detalhes


if __name__ == "__main__":

	from criador_de_nota_fiscal import Criador_de_nota_fiscal

	itens = [
		Item("Item I", 100), 
		Item("Item II", 200)
	]

	#Parâmetros Nomeados - Sem Builder
	nota_fiscal = Nota_fiscal(
		cnpj="123456789900",
		razao_social="Empresa Seje Loko LTDA",
		itens=itens
		);

	#Builder no código
	nota_fiscal_criada_no_builder = (Criador_de_nota_fiscal()
		.com_razao_social("Empresa Seje Loko LTDA")
		.com_data_de_emissao("22/03/2018")
		.com_cnpj("123456789900")
		.com_itens(itens)
		.constroi())


