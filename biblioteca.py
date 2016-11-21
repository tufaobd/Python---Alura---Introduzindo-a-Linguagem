def gera_convite(convite):
	posicao_final = len(convite)
	posicao_inicial = posicao_final -4
	parte1 = convite[0:4]
	parte2 = convite[posicao_inicial:posicao_final]
	envia_convite = parte1 + ' ' + parte2
	print 'Enviando convite para %s ' %(envia_convite)

def envia_convite(nome_formatado):
	print 'Enviando convite para %s ' %(nome_formatado)

