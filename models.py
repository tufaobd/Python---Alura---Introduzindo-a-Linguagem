# -*- coding: utf-8 -*-

class Perfil():
	'Classe Padrão para perfis de usuários'

	def __init__(self, nome, telefone, empresa):
		if(len(nome) < 3):
			raise Argumento_Invalido_Error('Nome deve ter pelo menos 3 caracteres')
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
		self.__curtidas = 0


	def imprimir(self):
		print 'Nome: %s, Telefone %s, empresa %s ,você tem %s curtida(s).' %(self.nome, self.telefone, self.empresa, self.__curtidas)

	def curtir(self):
		self.__curtidas += 1

	def obter_curtidas(self):
		return self.__curtidas

	@classmethod
	def gerar_perfis(classe, nome_arquivo):
		arquivo = open(nome_arquivo, 'r')
		perfis = []
		for linhas in arquivo:
			valores = linhas.split(',')
			if(len(valores) is not 3):
				raise ValueError('Uma linha do arquivo %s deve ter 3 valores' %nome_arquivo)
			perfis.append(classe(*valores))
		arquivo.close()
		return perfis


class Perfil_vip(Perfil):
	'Classe Padrão para perfis de usuários vips'

	def __init__(self, nome, telefone, empresa, apelido=''):
		super(Perfil_vip, self).__init__(nome, telefone, empresa)
		self.apelido = apelido

	def obter_creditos(self):
		if self.__tipo ==1:
			return super(Perfil_vip, self).obter_curtidas() * 10.0


class Argumento_Invalido_Error(Exception):
	def __init__(self, mensagem):
		self.mensagem = mensagem

	def __str__(self):
		return repr(self.mensagem)

#Daqui para baixo não faz parte do principal
class Data():
	'classe formatacao de data'
	
	def __init__(self, dia, mes, ano):
		self.dia = dia
		self.mes = mes
		self.ano = ano

	def imprime(self):
		print '%s/%s/%s' %(self.dia, self.mes, self.ano)


class Pessoa():

	def __init__(self, nome, peso, altura):
		self.nome = nome
		self.peso = peso
		self.altura = altura

	def imprime_imc(self):
		a = (self.peso)/(self.altura * self.altura)
		print 'IMC de Ronaldo: %s' %(a)

