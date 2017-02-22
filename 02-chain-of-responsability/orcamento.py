# -*- coding: UTF-8 -*-

class Orcamento(object):

	def __init__(self):
		self._itens = []

	@property
	def valor(self):
		total = 0.0
		for item in self._itens:
			total += item.valor

		return total

	def obter_itens(self):
		return tuple(self._itens)

	def adiciona_item(self, item):
		self._itens.append(item)

	@property
	def total_itens(self):
		return len(self._itens)

class Item(object):
	def __init__(self, nome, valor):
		self._nome = nome
		self._valor = valor

	@property
	def valor(self):
		return self._valor 

	@property
	def nome(self):
		return self._nome