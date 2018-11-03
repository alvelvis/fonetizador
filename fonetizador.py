# -*- coding: utf-8 -*-

import re
import string
import sys

def fonetiza(palavra):

	#CHECA SE A PALAVRA NÃO CONTÉM NÚMEROS NEM ESPAÇOS
	#CASO CONTRÁRIO, NÃO MODIFICA A PALAVRA (retorna ela própria)
	if re.match(r'[^\d\s]+', palavra):

		#CRIA A LISTA DAS REGRAS DE FONETIZAÇÃO
		expressao = list()

		#VOGAIS E CONSOANTESS
		v = r'AEIOUÁÉÍÓÚÃẼĨÕŨÀÈÌÒÙÂÊÎÔÛ@'
		c = r'BCDFGHJKLMNPQRSTVWXYZ"'

		#REGRAS DE FONETIZAÇÃO
		#('expressão regular', 'substituto', grupo anterior que permanece, grupo posterior que permanece)
		expressao.extend([							
								(r'(.*)Y(.*)','I',1,2),

								(r'(.*)W([LR'+v+'].*)','V',1,2),
								(r'(.*)W(['+c+'].*)','"0',1,2),

								(r'(.*)[AÃÁ][N]$','Ã',1,0),
								(r'(.*)[AÃÁ][M]$','ÃW',1,0),
								(r'(.*)[Ã][O]$','ÃW',1,0),
								(r'(.*)[EÉẼ][MN]$','ẼI',1,0),
								(r'(.*)[IÍĨ][MN]$','Ĩ',1,0),
								(r'(.*)[OÓÕ][MN]$','ÕW',1,0),
								(r'(.*)[UÚŨ][MN]$','Ũ',1,0),
								(r'(.*)[AÃÁ][N]S$','ÃS',1,0),
								(r'(.*)[AÁÃ][M]S$','ÃWS',1,0),
								(r'(.*)[Ã][O]S$','ÃWS',1,0),
								(r'(.*)[EÉẼ][MN]S$','ẼIS',1,0),
								(r'(.*)[IĨÍ][MN]S$','ĨS',1,0),
								(r'(.*)[OÓÕ][MN]S$','ÕWS',1,0),
								(r'(.*)[UÚŨ][MN]S$','ŨS',1,0),

								(r'(.*[^SWNR])S(['+v+'].*)','Z',1,2),

								(r'(.*)[AÂÁ][MN]([^'+v+'H].*)','Ã',1,2),
								(r'(.*)[EÊÉ][MN]([^'+v+'H].*)','Ẽ',1,2),
								(r'(.*)[IÎÍ][MN]([^'+v+'H].*)','Ĩ',1,2),
								(r'(.*)[OÔÓ][MN]([^'+v+'H].*)','Õ',1,2),
								(r'(.*)[UÛÚ][MN]([^'+v+'H].*)','Ũ',1,2),
								(r'(.*)[AÂÁ]([MN]['+v+'].*)','Ã',1,2),
								(r'(.*)[EÊÉ]([MN]['+v+'].*)','Ẽ',1,2),
								(r'(.*)[IÎÍ]([MN]['+v+'].*)','Ĩ',1,2),
								(r'(.*)[OÔÒ]([MN]['+v+'].*)','Õ',1,2),
								(r'(.*)[UÛÚ]([MN]['+v+'].*)','Ũ',1,2),
								(r'(.*)[AÂÁ]([MN][H].*)','Ã',1,2),
								(r'(.*)[EÊÉ]([MN][H].*)','Ẽ',1,2),
								(r'(.*)[IÎÍ]([MN][H].*)','Ĩ',1,2),
								(r'(.*)[OÔÓ]([MN][H].*)','Õ',1,2),
								(r'(.*)[UÛÚ]([MN][H].*)','Ũ',1,2),

								(r'(.*)[AÁÂ][L]([^'+v+'H].*)','AW',1,2),
								(r'(.*)[EÉÊ][L]([^'+v+'H].*)','EW',1,2),
								(r'(.*)[IÍĨ][L]([^'+v+'H].*)','IW',1,2),
								(r'(.*)[OÓÔ][L]([^'+v+'H].*)','OW',1,2),
								(r'(.*)[UŨÚ][L]([^'+v+'H].*)','UW',1,2),
								(r'(.*)[AÁÂ][L]$','AW',1,0),
								(r'(.*)[EÉÊ][L]$','EW',1,0),
								(r'(.*)[IĨÍ][L]$','IW',1,0),
								(r'(.*)[OÓÔ][L]$','OW',1,0),
								(r'(.*)[UŨÚ][L]$','UW',1,0),
								(r'(.*)[AÁÂ][U](.*)','AW',1,2),
								(r'(.*)[EÉÊ][U](.*)','EW',1,2),
								(r'(.*)[IÍĨ][U](.*)','IW',1,2),
								(r'(.*)[OÓÔ][U](.*)','OW',1,2),
								(r'(.*)[UÚŨ][U](.*)','UW',1,2),

								(r'(.*)[O]$','U',1,0),
								(r'(.*)[O][S]$','US',1,0),
								(r'(.*)[E]$','I',1,0),
								(r'(.*)[E][S]$','IS',1,0),
								(r'(.+)[A]$','@',1,0),
								(r'(.+)[A][S]$','@S',1,0),
								(r'(.*)[Z]$','S',1,0),

								(r'(.*)[T]([IĨÍ].*)','"T',1,2),
								(r'(.*)[D]([IĨÍ].*)','"D',1,2),

								(r'(.*)SS(.*)','S',1,2),
								(r'(.*)SH(.*)','X',1,2),
								(r'(.*)SC([EIẼĨÉÍ].*)','S',1,2),
								(r'(.*)SC([AUOÃŨÕÁÚÓ].*)','SK',1,2),
								(r'(.*)SCH(.*)','X',1,2),

								(r'(.*)TH(.*)','T',1,2),
								(r'^(E)X(['+v+'].*)','Z',1,2),
								(r'(.*E)X([AOUÁÓÚÃÕŨ].*)','KS',1,2),
								(r'(.*E)X([PTC].*)','S',1,2),
								(r'(.*E)X([^EIAOUẼĨÃÕŨÉÍÁÓÚ].*)','KS',1,2),
								(r'(.*[DFMNPQSTVZ][AIOUÃĨÕŨÁÍÓÚ])X(.*)','KS',1,2),

								(r'(.*)CH(R.*)','K',1,2),
								(r'(.*)CH(.*)','X',1,2),
								(r'(.*)C([ÂAÃÔÕOÛŨU].*)','K',1,2),
								(r'(.*)C(['+c+'].*)','K',1,2),
								(r'(.*)C([EÊẼIÎĨ].*)','S',1,2),
								(r'(.*)C$','K',1,0),
								(r'(.*)Ç(.*)','S',1,2),
								(r'(.*)GH?([EẼÉIĨÍ].*)','J',1,2),
								(r'^H(['+v+'].*)','',0,1),
								(r'LH','"1',0,0),
								(r'(.*)N$','M',1,0),
								(r'(.*)NH(.*)','"3',1,2),
								(r'(.*)PH(.*)','F',1,2),

								(r'(.*)QU([IEĨẼÍÉÎÊ].*)','K',1,2),
								(r'(.*)Q(U[AOÃÕÁÓÂÔ].*)','K',1,2),
								(r'(.*)Q(.*)','K',1,2),
								(r'(.*)GU([IEĨẼÍÉÎÊ].*)','G',1,2),

								(r'^R(.*)','"2',0,1),
								(r'(.*)R$','"2',1,0),
								(r'(.*)RR(.*)','"2',1,2),
								(r'(.*)R(['+c+'].*)','"2',1,2),

								#CORREÇÃO
								(r'TAKS@','TAX@',0,0),
								(r'TAKSA','TAXA',0,0),
								(r'máKSĨ','máXĨ',0,0),
								(r'maKSĨ','maXĨ',0,0),	
						])

		#PASSA POR TODAS AS REGRAS DE TRANSFORMAÇÃO
		#PARA CADA REGRA, TRANSFORMA A VARIÁVEL "PALAVRA"
		k = 0
		while k < len(expressao):
			match = re.search(expressao[k][0], palavra, flags=re.IGNORECASE)
			if match:
				antes = str(expressao[k][2])
				depois = str(expressao[k][3])
				if antes != '0': antes = '\\' + antes
				else: antes = ''
				if depois != '0': depois = '\\' + depois
				else: depois = ''
				palavra = re.sub(expressao[k][0], antes + expressao[k][1] + depois, palavra, flags=re.IGNORECASE)			
			k += 1

	#RETORNA A "PALAVRA", TRANSFORMADA OU NÃO
	return palavra


def main(caminho, output='fonetizado.txt', CODE='utf8', CODEFINAL='utf8'):

	#ABRE O ARQUIVO E TRANSFORMA EM LISTA
	with open(caminho, 'r', encoding=CODE) as arq:
		texto = arq.read()
	texto = texto.splitlines()

	#DESTACA A PONTUAÇÃO E SEPARA AS PALAVRAS (critério: espaço)
	for i in range(len(texto)):
		for ponto in string.punctuation:
			texto[i] = texto[i].replace(ponto, ' ' + ponto + ' ')
		texto[i] = texto[i].split()

	#FONETIZA PALAVRA POR PALAVRA
	for i, linha in enumerate(texto):
		for w, palavra in enumerate(linha):
			texto[i][w] = fonetiza(texto[i][w])

	#REFAZ ARQUIVO NOS MOLDES DO ORIGINAL -> em cada linha, cada item (as palavras) recebe um espaço
	for i,linha in enumerate(texto):
		texto[i] = " ".join(texto[i])

	#SALVA ARQUIVO OUTPUT -> cada item da lista recebe um "\n"
	with open(output, 'w', encoding=CODEFINAL) as arq:
		arq.write("\n".join(texto))


if __name__ == '__main__':

	#CHECA ARGUMENTOS
	if len(sys.argv) <= 1:
		print('Argumentos esperados para o fonetizador')
		print('uso: fonetizador.py entrada saída codificação-da-entrada codificação-da-saída')
		print("Tente `-h' para mais informações")
	else:
		if sys.argv[1] == '-h':
			print('uso: fonetizador.py entrada saída codificação-da-entrada codificação-da-saída')
			print('É obrigatório informar apenas a entrada (arquivo de texto original)')
			print('Saída padrão: "fonetizado.txt"')
			print('Codificação padrão: utf8')
		elif len(sys.argv) == 2: main(sys.argv[1])
		elif len(sys.argv) == 3: main(sys.argv[1], sys.argv[2])
		elif len(sys.argv) == 4: main(sys.argv[1], sys.argv[2], sys.argv[3])
		elif len(sys.argv) == 5: main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
		else:
			print('Argumentos demais')
			print("Tente `-h' para mais informações")