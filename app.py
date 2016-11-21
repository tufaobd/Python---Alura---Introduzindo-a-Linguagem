# -*- coding: utf-8 -*-
import re
def cadastrar(nomes):
	print "Digite o nome:"
	nome = raw_input()
	nomes.append(nome)

def menu():
	nomes = []
	escolha = ''
	while (escolha !='0'):
		print 'Opções:\n 1 - Para cadastrar\n 2 - Listar Nomes\n 3 - Remover Nome\n 4 - Alterar nome '
		print ' 5 - Procurar nome \n 6 - Testando o Regex \n 0 - Para Sair'
		escolha = raw_input()
		if(escolha == '1'):
			cadastrar(nomes)
		if(escolha=='2'):
			listar(nomes)
		if(escolha =='3'):
			remover(nomes)
		if(escolha == '4'):
			alterar(nomes)
		if(escolha == '5'):
			procurar(nomes);
		if(escolha=='6'):
			procura_regex(nomes)
		else:
			print 'Opção não encontrada'

def listar(nomes):
	print 'Listando nomes'
	for nome in nomes:
		print nome

def remover(nomes):
	print 'Digite nome você gostaria de remover?'
	nome = raw_input()
	nomes.remove(nome)

def alterar(nomes):
	print 'Atuais nomes na lista'
	listar(nomes)
	print 'Digite o nome que você gostaria de alterar:'
	nome = raw_input()
	posicao = nomes.index(nome)
	print posicao
	print 'Digite a alteração:'
	nome_alterado = raw_input()
	nomes[posicao] = nome_alterado
	listar(nomes)

def procurar(nomes):
	print 'Digite o nome que procura'
	nome_a_procurar = raw_input()
	if(nome_a_procurar in nomes):
		print 'Nome %s consta na lista' %nome_a_procurar
	else:
		print 'Nome não encontrado na lista'

def procura_regex(nomes):
	print 'Digite a expressao regular'
	regex = raw_input()
	nomes_concatenados = ''.join(nomes)
	busca = re.findall(regex+'\w+', nomes_concatenados)
	print(busca)


menu()