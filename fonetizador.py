# -*- coding: utf-8 -*-

import re
import sys
import string
import os

#Atualizar a versão do fonetizador
def atualizar():
	try:
		from git import Git
	except:
		from pip import main as pipmain
		pipmain(['install','GitPython'])
		print('GitPython instalado com sucesso!')
		exit()
	else:
		if os.path.isdir('.git'):
			Git().pull()
		else:
			Git().init()
			Git().remote('add','origin','https://github.com/alvelvis/fonetizador.git')
			Git().fetch()
			if os.path.isfile('README.md'): os.remove('README.md')
			if os.path.isfile('fonetizador.py'): os.remove('fonetizador.py')
			Git().checkout('master')
		print('fonetizador atualizado com sucesso!')
		exit()

def fonetiza(palavra):

	#CHECA SE A PALAVRA NÃO CONTÉM NÚMEROS NEM ESPAÇOS
	#CASO CONTRÁRIO, NÃO MODIFICA A PALAVRA (retorna ela própria)
	notword = '\d'
	for item in string.punctuation:
		notword = notword + '\\' + item

	if re.match(r'^[^'+notword+']+$', palavra) and palavra.strip() != '':

		#VOGAIS E CONSOANTESS
		vt = 'ÄËÏÖÜÂÊÎÔÛ'
		vd = 'AEIOUÃẼĨÕŨ'
		v = vt + vd
		c = 'BCÇDFGHJKLMNPQRSTVWXYZ"234'

		#CRIA A LISTA DAS REGRAS DE FONETIZAÇÃO
		expressao = list()

		#ADICIONA AS REGRAS DE FONETIZAÇÃO
		#('expressão regular','substituto',grupo anterior que permanece,grupo posterior que permanece)
		expressao.extend([
								#TIRAR O "U" DO "GUE"
								(r'GH?([EIÊÎËÏẼĨ])','J',0,1),
								(r'GUI','GI',0,0),
								(r'GUE','GE',0,0),

								#TÔNICAS ORAIS
								(r'Á','Ä',0,0),
								(r'É','Ë',0,0),
								(r'Í','Ï',0,0),
								(r'Ó','Ö',0,0),
								(r'Ú','Ü',0,0),
								(r'Â','Ä',0,0),
								(r'Ê','Ë',0,0),
								(r'Î','Ï',0,0),
								(r'Ô','Ö',0,0),
								(r'Û','Ü',0,0),

								#TÔNICAS NASAIS
								(r'Ã','Â',0,0),
								(r'Ẽ','Ê',0,0),
								(r'Ĩ','Î',0,0),
								(r'Õ','Ô',0,0),
								(r'Ũ','Û',0,0),

								#ÁTONO ORAL
								(r'À','A',0,0),

								#TÔNICAS ESPECIAIS
								(r'^([^'+vt+']*)AIA(S?)$','ÄIA',1,2),
								(r'^([^'+vt+']*)EIA(S?)$','ËIA',1,2),
								(r'^([^'+vt+']*)OIA(S?)$','ÖIA',1,2),
								(r'^([^'+vt+']*)UIA(S?)$','ÜIA',1,2),
								(r'^([^'+vt+']*)AU(S?)$','ÄU',1,2),
								(r'^([^'+vt+']*)EU(S?)$','ËU',1,2),
								(r'^([^'+vt+']*)OU(S?)$','ÖU',1,2),
								(r'^([^'+vt+']*)IU(S?)$','ÏU',1,2),
								(r'^([^'+vt+']*)EI(S?)$','ËI',1,2),
								(r'^([^'+vt+']*)AI(S?)$','ÄI',1,2),
								(r'^([^'+vt+']*)UI(S?)$','ÜI',1,2),
								(r'^([^'+vt+']*)OI(S?)$','ÖI',1,2),
								(r'^([^'+vt+']*)AR$','ÄR',1,0),
								(r'^([^'+vt+']*)ER$','ËR',1,0),
								(r'^([^'+vt+']*)IR$','ÏR',1,0),
								(r'^([^'+vt+']*)OR$','ÖR',1,0),
								(r'^([^'+vt+']*)UR$','ÜR',1,0),
								(r'^([^'+vt+']*)IM$','ÏM',1,0),
								(r'^([^'+vt+']*)UM$','ÜM',1,0),
								(r'^([^'+vt+']*)AL$','ÄL',1,0),
								(r'^([^'+vt+']*)EL$','ËL',1,0),
								(r'^([^'+vt+']*)IL$','ÏL',1,0),
								(r'^([^'+vt+']*)OL$','ÖL',1,0),
								(r'^([^'+vt+']*)AZ$','ÄZ',1,0),
								(r'^([^'+vt+']*)EZ$','ËZ',1,0),
								(r'^([^'+vt+']*)IZ$','ÏZ',1,0),
								(r'^([^'+vt+']*)OZ$','ÖZ',1,0),
								(r'^([^'+vt+']*)UZ$','ÜZ',1,0),
								(r'^([^'+vt+']*)QUI([^'+vt+']*)$','QÏ',1,2),
								(r'^([^'+vt+']*)QUE([^'+vt+']*)$','QË',1,2),
								(r'^([^'+vt+']*)EI(['+c+']*['+vd+']['+c+']*)$','ËI',1,2),
								(r'^([^'+vt+']*)AI(['+c+']*['+vd+']['+c+']*)$','ÄI',1,2),
								(r'^([^'+vt+']*)UI(['+c+']*['+vd+']['+c+']*)$','ÜI',1,2),
								(r'^([^'+vt+']*)OI(['+c+']*['+vd+']['+c+']*)$','ÖI',1,2),
								(r'^([^'+vt+']*)AU(['+c+']*['+vd+']['+c+']*)$','ÄU',1,2),
								(r'^([^'+vt+']*)EU(['+c+']*['+vd+']['+c+']*)$','ËU',1,2),
								(r'^([^'+vt+']*)IU(['+c+']*['+vd+']['+c+']*)$','ÏU',1,2),
								(r'^([^'+vt+']*)OU(['+c+']*['+vd+']['+c+']*)$','ÖU',1,2),
								(r'^([^'+vt+']*)I(S?)$','Ï',1,2),
								(r'^([^'+vt+']*)U(S?)$','Ü',1,2),

								#CONSOANTES MUDAS
								(r'([^'+v+'SXMNZLHR])([^'+v+'HRL])','I',1,2),
								(r'^([^'+v+'SXMNZLHR])([^'+v+'HRL])','I',1,2),
								(r'([^'+v+'SXMNZLHR])$','I',1,0),
								(r'([^'+v+'][^'+v+'SXMNZLH])$','I',1,0),

								#S E Z
								(r'Z$','S',0,0),
								(r'([^SWNR])S(['+v+'])','Z',1,2),
								(r'Y','I',0,0),
								(r'W(['+v+'])','V',0,1),

								#FINAL DAS PALAVRAS
								(r'X(I?)$','KS',0,1),
								(r'E(S?)$','I',0,1),
								(r'O(S?)$','U',0,1),
								(r'ËS$','ËIS',0,0),
								(r'ÖS$','ÖIS',0,0),

								#PAROXÍTONAS, QUE SÃO A REGRA
								(r'^([^'+vt+']*)A(['+c+']*['+vd+']['+c+']*)$','Ä',1,2),
								(r'^([^'+vt+']*)E(['+c+']*['+vd+']['+c+']*)$','Ë',1,2),
								(r'^([^'+vt+']*)I(['+c+']*['+vd+']['+c+']*)$','Ï',1,2),
								(r'^([^'+vt+']*)O(['+c+']*['+vd+']['+c+']*)$','Ö',1,2),
								(r'^([^'+vt+']*)U(['+c+']*['+vd+']['+c+']*)$','Ü',1,2),

								#MONOSSÍLABA, É TÔNICA
								(r'^(['+c+']*)A(['+c+']*)$','Ä',1,2),
								(r'^(['+c+']*)E(['+c+']*)$','Ë',1,2),
								(r'^(['+c+']*)I(['+c+']*)$','Ï',1,2),
								(r'^(['+c+']*)O(['+c+']*)$','Ö',1,2),
								(r'^(['+c+']*)U(['+c+']*)$','Ü',1,2),

								#DÍGRAFOS
								(r'LH','"3',0,0),
								(r'NH','"4',0,0),

								#DITONGOS
								(r'([AEIOÄËÏÖ])L([^'+v+'])','U',1,2),
								(r'([AEIOÄËÏÖ])L$','U',1,0),
								(r'([UÜ])L([^'+v+'])','',1,2),
								(r'([UÜ])L$','',1,0),

								#NASALIZAÇÃO DOS ÁTONOS (e algumas ditongações)
								(r'A(([MN]|"4)['+v+'])','Ã',0,1),
								(r'E(([MN]|"4)['+v+'])','Ẽ',0,1),
								(r'I(([MN]|"4)['+v+'])','Ĩ',0,1),
								(r'O(([MN]|"4)['+v+'])','Õ',0,1),
								(r'U(([MN]|"4)['+v+'])','Ũ',0,1),
								(r'A[MN]([^'+v+'])','Ã',0,1),
								(r'E[MN]([^'+v+'])','Ẽ',0,1),
								(r'I[MN]([^'+v+'])','Ĩ',0,1),
								(r'O[MN]([^'+v+'])','Õ',0,1),
								(r'U[MN]([^'+v+'])','Ũ',0,1),
								(r'A[MN]$','ÃU',0,0),
								(r'E[MN]$','ẼI',0,0),
								(r'I[MN]$','Ĩ',0,0),
								(r'O[MN]$','ÕU',0,0),
								(r'U[MN]$','Ũ',0,0),

								#NASALIZAÇÃO DOS TÔNICOS (e algumas ditongações)
								(r'Ä(([MN]|"4)['+v+'])','Â',0,1),
								(r'Ë(([MN]|"4)['+v+'])','Ê',0,1),
								(r'Ï(([MN]|"4)['+v+'])','Î',0,1),
								(r'Ö(([MN]|"4)['+v+'])','Ô',0,1),
								(r'Ü(([MN]|"4)['+v+'])','Û',0,1),
								(r'Ä[MN]([^'+v+'])','Â',0,1),
								(r'Ë[MN]([^'+v+'])','Ê',0,1),
								(r'Ï[MN]([^'+v+'])','Î',0,1),
								(r'Ö[MN]([^'+v+'])','Ô',0,1),
								(r'Ü[MN]([^'+v+'])','Û',0,1),
								(r'Ä[MN]$','ÂU',0,0),
								(r'Ë[MN]$','ÊI',0,0),
								(r'Ï[MN]$','Î',0,0),
								(r'Ö[MN]$','ÔU',0,0),
								(r'Ü[MN]$','Û',0,0),

								#TIA, DIA
								(r'[T]([IÏĨÎ])','"T',0,1),
								(r'[D]([IÏĨÎ])','"D',0,1),

								#S, SK
								(r'Ç','S',0,0),
								(r'SS','S',0,0),
								(r'SH','X',0,0),
								(r'SC([EIËÏẼĨÊÎ])','S',0,1),
								(r'SC([AUOÃŨÕÂÛÔÄÜÖ])','SK',0,1),
								(r'SCH','X',0,0),

								#X, Z, KS
								(r'TH','T',0,0),
								(r'([EÊẼË])X([PTC])','S',1,2),
								(r'^([EË])X(['+v+'])','Z',1,2),
								(r'([EÊẼË])X([^'+v+'])','KS',1,2),
								(r'([DFMNQSTVZ]['+v+'])X','KS',1,0),

								#K, X, H
								(r'CH(R)','K',0,0),
								(r'CH','X',0,0),
								(r'C([AOUÃÕŨÂÔÛÄÖÜ])','K',0,1),
								(r'C(['+c+'])','K',0,1),
								(r'C([EIÊÎËÏẼĨ])','S',0,1),
								(r'C$','K',0,0),
								(r'^H(['+v+'])','',0,1),

								#RR
								(r'^R','"2',0,0),
								(r'R$','"2',0,0),
								(r'RR','"2',0,0),
								(r'R(['+c+'])','"2',0,1),

								#CORREÇÃO
								(r'(T[AÄ])KS(A)','X',1,2),
								(r'(m[aÄ])KS([ĨI])','maXĨ',1,2),
								(r'(tr[ÖO]U)x([IËE])','S',1,2),

						])

		#TESTE DE REGRA
		TESTAR = False
		word = "trazer"

		#PASSA POR TODAS AS REGRAS DE TRANSFORMAÇÃO
		#PARA CADA REGRA, TRANSFORMA A VARIÁVEL "PALAVRA"
		k = 0
		while k < len(expressao):

			match = re.search(expressao[k][0], palavra, flags=re.IGNORECASE)
			if match:

				if (TESTAR == True) and (palavra == word or palavra == palavra):
					print(palavra, ': ', expressao[k][0], ' --> ', expressao[k][1])

				#GRUPOS QUE NÃO SERÃO SUBSTITUÍDOS
				antes = str(expressao[k][2])
				depois = str(expressao[k][3])
				if antes != '0':
					antes = '\\' + antes
				else:
					antes = ''
				if depois != '0':
					depois = '\\' + depois
				else:
					depois = ''

				palavra = re.sub(expressao[k][0], antes + expressao[k][1] + depois, palavra, flags=re.IGNORECASE)

			k += 1

	#RETORNA A "PALAVRA", TRANSFORMADA OU NÃO
	return palavra


def main(caminho, output='fonetizado.txt', CODE='utf8', CODEFINAL='utf8'):

	#SE FOR INTERNO, O TEXTO ESTÁ NA VARIÁVEL OUTPUT
	#CASO CONTRÁRIO, CARREGAR O ARQUIVO E SEPARAR LINHAS EM LISTAS
	if caminho != 'interno':
		texto = open(caminho, 'r', encoding=CODE).read().replace(';',' ; ').splitlines()
	else:
		texto = output.splitlines()

	#DESTACA A PONTUAÇÃO E SEPARA AS PALAVRAS (critério: espaço)
	for i in range(len(texto)):
		for ponto in string.punctuation:
			texto[i] = texto[i].replace(ponto, ' ' + ponto + ' ')
		texto[i] = texto[i].split()

	#FONETIZA PALAVRA POR PALAVRA
	for i, linha in enumerate(texto):
		for w, palavra in enumerate(linha):
			texto[i][w] = fonetiza(texto[i][w])

	#REFORMATA ARQUIVO NOS MOLDES DO ORIGINAL
	for i,linha in enumerate(texto):
		texto[i] = " ".join(texto[i])

	#SE FOR INTERNO, PRINTA
	#SE NÃO, SALVA ARQUIVO OUTPUT
	if caminho != 'interno':
		open(output, 'w', encoding=CODEFINAL).write("\n".join(texto).replace(' ; ',';'))
	else:
		return("\n".join(texto))


if __name__ == '__main__':

	#CHECA ARGUMENTOS
	if len(sys.argv) <= 1:
		print('Argumentos esperados para o fonetizador')
		print('uso: fonetizador.py entrada saída codificação-da-entrada codificação-da-saída')
		print("Com o comando `-t' é possível digitar o texto diretamente")
		print("Tente `-help' para mais informações")
		print("Para atualizar o fonetizador, `-update'")
	else:
		if sys.argv[1] == '-help':
			print('uso: fonetizador.py entrada saída codificação-da-entrada codificação-da-saída')
			print("É obrigatório informar a entrada (arquivo de texto original) OU o texto que será transcrito, após o comando `-t'")
			print('Saída padrão: "fonetizado.txt"')
			print('Codificação padrão: utf8')
		elif sys.argv[1] == '-update': atualizar()
		elif sys.argv[1] == '-t': print(main('interno', " ".join(sys.argv[2:])))
		elif len(sys.argv) == 2: main(sys.argv[1])
		elif len(sys.argv) == 3: main(sys.argv[1], sys.argv[2])
		elif len(sys.argv) == 4: main(sys.argv[1], sys.argv[2], sys.argv[3])
		elif len(sys.argv) == 5: main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
		else:
			print('Argumentos demais')
			print("Tente `-help' para mais informações")

