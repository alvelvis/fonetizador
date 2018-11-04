# Tradutor fonético pt-BR

O **fonetizador** transcreve arquivos de texto para uma representação semi-fiel do IPA (Alfabeto Fonético Internacional).

Algumas opções de transcrição são da variante carioca do português brasileiro; outras, da fonologia da língua portuguesa.

* [Exemplo](#exemplo)
* [Como usar](#como-usar)
* [Símbolos importantes](#símbolos-importantes)
* [Regras de transformação](#regras-de-transformação)
* [Deficiências](#deficiências)

# Exemplo

Considere o parágrafo inicial de Memórias Póstumas de Brás Cubas (Machado de Assis).

### Original

>Algum tempo hesitei se devia abrir estas memórias pelo princípio ou pelo fim, isto é, se poria em primeiro lugar o meu nascimento ou a minha morte. Suposto o uso vulgar seja começar pelo nascimento, duas considerações me levaram a adotar diferente método: a primeira é que eu não sou propriamente um autor defunto, mas um defunto autor, para quem a campa foi outro berço; a segunda é que o escrito ficaria assim mais galante e mais novo. Moisés, que também contou a sua morte, não a pôs no intróito, mas no cabo; diferença radical entre este livro e o Pentateuco.

### Transcrito

Veja a transcrição fonética do mesmo parágrafo:

>AWgŨ tẼpU eZitei sI devi@ abri"2 est@S mẼmóri@S pelU prĨcípiU OW pelU fĨ , istU é , sI pori@ ẼI prĨmeirU luga"2 U mEW naSĨmẼtU OW a mĨ"3@ mo"2"TI . SupostU U uZU vUWga"2 sej@ KÕmeSa"2 pelU naSĨmẼtU , du@S KÕsideraSõIS mI levarÃW a adota"2 "DiferẼ"TI métodU : a prĨmeir@ é KI EW nÃW sOW propriÃmẼ"TI Ũ AWto"2 defŨtU , mas Ũ defŨtU AWto"2 , par@ KẼI a KÃp@ foi OWtrU be"2SU ; a segŨd@ é KI U esKritU fiKari@ aSĨ mais galÃ"TI I mais novU . MoiZés , KI tÃbẼI KÕtOW a su@ mo"2"TI , nÃW a pôs nU ĨtróitU , mas nU KabU ; "DiferẼS@ "2a"DiKAW ẼtrI es"TI livrU I U PẼtatEWKU .

# Como usar

* Clone ou baixe o repositório e execute o script *fonetizador.py* com Python 3+, utilizando os seguintes argumentos:

		>> fonetizador.py entrada saída codificação-da-entrada codificação-da-saída

1. Entrada: arquivo de texto original
2. Saída(\*): novo arquivo com a transcrição fonética (padrão: "fonetizado.txt")
3. Codificação da entrada(\*): codificação do arquivo original (padrão: "utf8")
4. Codificação da saída(\*): codificação do arquivo alvo (padrão: "utf8")

(\*) Argumento opcional

* Outra possibilidade é digitar o texto diretamente na linha de comando, utilizando o argumento *-t* :

		>> fonetizador.py -t texto a ser transcrito foneticamente
		
		teStU a se"2 trÃsKritU fÕne"TiKÃmẼ"TI

# Símbolos importantes

| símbolo | som |
| -- | -- |
| @ | arar**a** |
| "T | **t**ia |
| "D | **d**ia |
| "2 | **r**ua / ca**rr**o |
| "1 | nava**lh**a |
| "3 | ma**nh**ã |

# Regras de transformação

Parte das regras para consoantes foram adaptadas do projeto [Metaphone for Brazilian Portuguese](https://sourceforge.net/p/metaphoneptbr/code/ci/master/tree/README#l56).

### Notação

A notação é, em grande parte, a mesma das expressões regulares:

	v	--> vogais
	c	--> consoantes
	[]	--> qualquer caracter dentro dos colchetes
	[^]	--> qualquer caracter exceto os que estão dentro dos colchetes
	^	--> início da palavra
	$	--> final da palavra
	?	--> 1 ou 0
	+	--> 1 ou mais

### Regras

As regras são aplicadas a todas as palavras, na ordem em que aparecem. Considera-se *palavra* o conjunto de caracteres entre espaços que não contenha números.

Abaixo, você confere algumas das regras de transcrição fonética:

| expressão | resultado |
| -- | -- |
| W[LRv] | V |
| [Ã][O]$ | ÃW |
| [AÃÁ][N]$ | Ã |
| [AÃÁ][M]$ | ÃW |
| [EẼÉ][M]$ | ẼI |
| [^SWNR]S[v] | Z |
| [AÁÂ][L][^vH] | AW |
| [AÁÂ][U] | AW |
| [O]$ | U |
| [E]$ | I |
| [A]$ | @ |
| [Z]$ | S |
| [T][IĨÍ] | "T |
| [D][IĨÍ] | "D |
| SS | S |
| SH | X |
| SC[EIẼĨÉÍ] | S |
| SC[AUOÃŨÕÁÚÓ] | SK |
| SCH | X |
| TH | T |
| ^EX[v] | Z |
| CH | X |
| C[ÂAÃÔÕOÛŨU] | K |
| C[c] | K |
| C[EÊẼIÎĨ] | S |
| C$ | K |
| Ç | S |
| ^H[v] | desaparece |
| LH | "1 |
| N$ | M |
| NH | "3 |
| PH | F |
| QU[IEĨẼÍÉÎÊ] | K |
| QU[AOÃÕÁÓÂÔ] | K |
| Q | K |
| GU[IEĨẼÍÉÎÊ] | G |
| ^R | "2 |
| R$ | "2 |
| RR | "2 |
| R[c] | "2 |

# Deficiências

* O **fonetizador** não consegue identificar as sílabas tônicas das palavras e, por isso, algumas transcrições fonéticas não conseguem ser fiéis à fala do português brasileiro:

| atual | ideal |
| -- | -- |
| est@S | ést@S |
| mo"2"TI | mó"2"TI |
| propriÃmẼ"TI | própriamẼ"TI |
| pôs | poIS |
| voSês | voSeIS |

* Há alguns casos de nasalização das vogais que não deveriam ocorrer:

| atual | ideal |
| -- | -- |
| prĨmeirU | primeirU |
| naSĨmẼtU | naSimẼtU |
| KÕmeSa"2 | KomeSa"2 |
