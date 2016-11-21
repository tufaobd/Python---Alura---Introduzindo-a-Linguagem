from models import *
#try:
#	arquivo = open('perfis.csv')
#	valores = arquivo.readline().split(',')
#	Perfil(*valores)
#	print('arquivo aberto')
#	arquivo.close()
#except (IOError,TypeError) as erro:
#	print('Deu Erro %s entre em contato com os programadores' % erro)
perfis = Perfil.gerar_perfis('perfis.csv')