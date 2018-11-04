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

>AUgÛ tÊpU eZitËI sÏ devÏA abrÏ"2 Ëstas mẼmÖrias pËlU prĨSÏpiU ÖU pËlU fÎ , ÏstU Ë , sÏ porÏA ÊI prĨmËIrU lugÄ"2 Ü mËU naSĨmÊtU ÖU Ä mÎ"4a mÖ"2"TI . SupÖstU Ü ÜZU vulgÄ"2 sËja KÕmeSÄ"2 pËlU naSĨmÊtU , dÜas KÕsideraSÔIs mÏ levÄrÃU Ä adotÄ"2 "DiferÊ"TI mËtodU : Ä prĨmËIra Ë QË ËU nÂU sÖU propriÃmÊ"TI Û autÖ"2 defÛtU , mÄs Û defÛtU autÖ"2 , pÄra QÊI Ä KÂpa fÖI ÖUtrU bË"2SU ; Ä segÛda Ë QË Ü esKrÏtU fiKarÏA aSÎ mÄIs galÂ"TI Ï mÄIs nÖvU . MoiZËs , QË tÃbÊI KÕtÖU Ä sÜa mÖ"2"TI , nÂU Ä pÖs nÜ ĨtrÖitU , mÄs nÜ KÄbU ; "DiferÊSa "2a"DiKÄU ÊtrI Ës"TI lÏvrU Ï Ü PẼtatËUKU .

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
		
		tËStU Ä sË"2 trÃsKrÏtU fÕne"TiKÃmÊ"TI

# Símbolos importantes

| símbolo | som |
| -- | -- |
| AEIOU | vogais |
| ÄËÏÖÜ | vogais tônicas |
| ÃẼĨÕŨ | vogais nasais |
| ÂÊÎÔÛ | vogais tônicas e nasais |
| "T | **t**ia |
| "D | **d**ia |
| d | **d**ado |
| "2 | ca**rr**o / **r**aro |
| r | tesou**r**o / ra**r**o |
| "3 | nava**lh**a |
| "4 | ma**nh**ã |

# Regras de transformação

Parte das regras para consoantes foram adaptadas do projeto [Metaphone for Brazilian Portuguese](https://sourceforge.net/p/metaphoneptbr/code/ci/master/tree/README#l56).

### Notação

A notação é, em grande parte, a mesma das expressões regulares:

	v	--> vogais
	vt	--> vogais tônicas
	vd	--> vogais átonas
	c	--> consoantes
	[]	--> qualquer caracter dentro dos colchetes
	[^]	--> qualquer caracter exceto os que estão dentro dos colchetes
	^	--> início da palavra
	$	--> final da palavra
	*	--> 0 ou mais
	+	--> 1 ou mais
	?	--> 1 ou 0
	|	--> ou

### Regras

As regras são aplicadas a todas as palavras, na ordem em que aparecem. Considera-se *palavra* o conjunto de caracteres entre espaços que não contenha números.

Abaixo, você confere as regras de transcrição fonética. Apenas o que não está entre parênteses é efetivamente substituído.

| expressão | transformação |
| -- | -- |
| GH?([EIÊÎËÏẼĨ]) | J |
| GUI | GI |
| GUE | GE |
| Á | Ä |
| É | Ë |
| Í | Ï |
| Ó | Ö |
| Ú | Ü |
| Â | Ä |
| Ê | Ë |
| Î | Ï |
| Ô | Ö |
| Û | Ü |
| Ã | Â |
| Ẽ | Ê |
| Ĩ | Î |
| Õ | Ô |
| Ũ | Û |
| ^([^vt]*)AIA$ | ÄIA |
| ^([^vt]*)EIA$ | ËIA |
| ^([^vt]*)AR$ | Ä |
| ^([^vt]*)ER$ | Ë |
| ^([^vt]*)IR$ | Ï |
| ^([^vt]*)OR$ | Ö |
| ^([^vt]*)IM$ | ÏM |
| ^([^vt]*)UM$ | ÜM |
| ^([^vt]*)IA$ | ÏA |
| ^([^vt]*)IU$ | ÏU |
| ^([^vt]*)AL$ | ÄL |
| ^([^vt]*)EL$ | ËL |
| ^([^vt]\*)TU([^vt]*)$ | TÜ |
| ^([^vt]\*)QUI([^vt]*)$ | QÏ |
| ^([^vt]\*)QUE([^vt]*)$ | QË |
| ^([^vt]\*)EI([^vtNM]*)$ | ËI |
| ^([^vt]\*)AI([^vtNM]*)$ | ÄI |
| ^([^vt]\*)UI([^vtNM]*)$ | ÜI |
| ^([^vt]\*)OI([^vtNM]*)$ | ÖI |
| ^([^vt]\*)EU([^vtNM]*)$ | ËU |
| ^([^vt]\*)OU([^vtNM]*)$ | ÖU |
| ^([^vt]*)I$ | Ï |
| E(S?)$ | I |
| O(S?)$ | U |
| ([^vSMNRZL])$ | I |
| ^([^vt]\*)A([c]\*[vd][c]*)$ | Ä |
| ^([^vt]\*)E([c]\*[vd][c]*)$ | Ë |
| ^([^vt]\*)I([c]\*[vd][c]*)$ | Ï |
| ^([^vt]\*)O([c]\*[vd][c]*)$ | Ö |
| ^([^vt]\*)U([c]\*[vd][c]*)$ | Ü |
| ^([c]\*)A([c]*)$ | Ä |
| ^([c]\*)E([c]*)$ | Ë |
| ^([c]\*)I([c]*)$ | Ï |
| ^([c]\*)O([c]*)$ | Ö |
| ^([c]\*)U([c]*)$ | Ü |
| [Z]$ | S |
| ([^SWNR])S([v]) | Z |
| Y | I |
| W([Lv]) | V |
| W([c]) | "0 |
| LH | "3 |
| NH | "4 |
| ([AEIOÄËÏÖ])L([^v]) | U |
| ([AEIOÄËÏÖ])L$ | U |
| A(([MN]\|"4)[v]) | Ã |
| E(([MN]\|"4)[v]) | Ẽ |
| I(([MN]\|"4)[v]) | Ĩ |
| O(([MN]\|"4)[v]) | Õ |
| U(([MN]\|"4)[v]) | Ũ |
| Ä(([MN]\|"4)[v]) | Â |
| Ë(([MN]\|"4)[v]) | Ê |
| Ï(([MN]\|"4)[v]) | Î |
| Ö(([MN]\|"4)[v]) | Ô |
| Ü(([MN]\|"4)[v]) | Û |
| A\[MN]([^v]) | Ã |
| E\[MN]([^v]) | Ẽ |
| I\[MN]([^v]) | Ĩ |
| O\[MN]([^v]) | Õ |
| U\[MN]([^v]) | Ũ |
| Ä\[MN]([^v]) | Â |
| Ë\[MN]([^v]) | Ê |
| Ï\[MN]([^v]) | Î |
| Ö\[MN]([^v]) | Ô |
| Ü\[MN]([^v]) | Û |
| A[MN]$ | ÃU |
| E[MN]$ | ẼI |
| I[MN]$ | Ĩ |
| O[MN]$ | ÕU |
| U[MN]$ | Ũ |
| Ä[MN]$ | ÂU |
| Ë[MN]$ | ÊI |
| Ï[MN]$ | Î |
| Ö[MN]$ | ÔU |
| Ü[MN]$ | Û |
| \[T]([IÏĨÎ]) | "T |
| \[D]([IÏĨÎ]) | "D |
| Ç | S |
| SS | S |
| SH | X |
| SC([EIËÏẼĨÊÎ]) | S |
| SC([AUOÃŨÕÂÛÔÄÜÖ]) | SK |
| SCH | X |
| TH | T |
| ([EÊẼË])X([PTC]) | S |
| ^([EÊẼË])X([v]) | Z |
| ([EÊẼË])X([AOUÄÖÜÂÔÛÃÕŨ]) | KS |
| ([EÊẼË])X([^EIAOUÃẼĨÕŨÄËÏÖÜÂÊÎÔÛ]) | KS |
| (\[DFMNPQSTVZ][AIOUÂIÔÛÃĨÕŨÄÏÖÜ])X | KS |
| CH(R) | K |
| CH | X |
| C([AOUÃÕŨÂÔÛÄÖÜ]) | K |
| C([c]) | K |
| C([EIÊÎËÏẼĨ]) | S |
| C$ | K |
| ^H([v]) | desaparece |
| ^ | "2 |
| R$ | "2 |
| R | "2 |
| R([c]) | "2 |
| TÄKSA | TÄXA |
| TAKSA | TAXA |
| mÄKSĨ | mÄXĨ |
| maKSĨ | maXĨ |

# Deficiências

* O **fonetizador** não consegue identificar se as vogais *E* e *I* são abertas ou fechadas e, por isso, algumas transcrições fonéticas não conseguem ser fiéis à fala do português brasileiro:

| fechada | aberta |
| -- | -- |
| m**Ö**"2tU / m**o**"2"TÎ"4U | m**Ö**"2"TI |
| pr**o**priedÄ"DI | pr**Ö**pria / pr**o**priÃmÊ"TI |

* Há alguns casos de nasalização das vogais que não deveriam ocorrer:

| atual | ideal |
| -- | -- |
| pr**Ĩ**mËIrU | pr**I**mËIrU |
| naS**Ĩ**mÊtU | naS**I**mÊtU |
| K**Õ**meSÄ"2 | K**O**meSÄ"2 |