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
	def __init__(self, razao_social, cnpj, itens, data_de_emissao=date.today(), detalhes='', observadores=[]):
		self.__razao_social = razao_social
		self.__cnpj = cnpj
		self.__data_de_emissao = data_de_emissao
		self.__itens = itens

		if len(detalhes) > 12:
			raise Exception("Detalhes da nota não podem ser maiores que 20 caracteres")
		else:
			self.__detalhes = detalhes

		for observador in observadores:
			observador(self)

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
	
	from observadores import imprime, envia_por_email, salva_no_banco
	from criador_de_nota_fiscal import Criador_de_nota_fiscal

	itens = [
		Item("Item I", 100), 
		Item("Item II", 200)
	]

	#Observers que vão ser notificados e acionados
	observadores = [
		imprime, envia_por_email, salva_no_banco
	]

	#Parâmetros Nomeados - Sem Builder
	nota_fiscal = Nota_fiscal(
		cnpj="123456789900",
		razao_social="Empresa Seje Loko LTDA",
		itens=itens, 
		observadores=observadores
		);




