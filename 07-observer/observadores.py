
def imprime(nota_fiscal):
	print 'Imprimindo nota fiscal %s' % (nota_fiscal.cnpj)

def salva_no_banco(nota_fiscal):
	print 'Salvando a nota fiscal %s no banco de dados' % (nota_fiscal.cnpj)

def envia_por_email(nota_fiscal):
	print 'Enviando a nota fiscal %s por e-mail' % (nota_fiscal.cnpj)