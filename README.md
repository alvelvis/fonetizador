# Tradutor fonético pt-BR

O **todutrar** transcreve arquivos de texto para uma representação semi-fiel do IPA (Alfabeto Fonético Internacional). Algumas opções de transcrição são da variante carioca do português brasileiro; outras, são da fonologia da língua portuguesa.

* [Exemplo](#exemplo)
* [Como usar](#como-usar)
* [Regras de transformação](#regras-de-tranformação)
* [Deficiências](#deficiências)

# Exemplo

### Original

Considere o parágrafo inicial de Memórias Póstumas de Brás Cubas (Machado de Assis):

>Algum tempo hesitei se devia abrir estas memórias pelo princípio ou pelo fim, isto é, se poria em primeiro lugar o meu nascimento ou a minha morte. Suposto o uso vulgar seja começar pelo nascimento, duas considerações me levaram a adotar diferente método: a primeira é que eu não sou propriamente um autor defunto, mas um defunto autor, para quem a campa foi outro berço; a segunda é que o escrito ficaria assim mais galante e mais novo. Moisés, que também contou a sua morte, não a pôs no intróito, mas no cabo; diferença radical entre este livro e o Pentateuco.

### Transcrito

Veja a transcrição fonética do mesmo parágrafo:

>AWgŨ tẼpU eZitei sI devi@ abri"2 est@S mẼmóri@S pelU prĨcípiU OW pelU fĨ , istU é , sI pori@ ẼI prĨmeirU luga"2 U mEW naSĨmẼtU OW a mĨ"3@ mo"2"TI . SupostU U uZU vUWga"2 sej@ KÕmeSa"2 pelU naSĨmẼtU , du@S KÕsideraSõIS mI levarÃW a adota"2 "DiferẼ"TI métodU : a prĨmeir@ é KI EW nÃW sOW propriÃmẼ"TI Ũ AWto"2 defŨtU , m@S Ũ defŨtU AWto"2 , par@ KẼI a KÃp@ foi OWtrU be"2SU ; a segŨd@ é KI U esKritU fiKari@ aSĨ mais galÃ"TI I mais novU . MoiZés , KI tÃbẼI KÕtOW a su@ mo"2"TI , nÃW a pôs nU ĨtróitU , m@S nU KabU ; "DiferẼS@ "2a"DiKAW ẼtrI es"TI livrU I U PẼtatEWKU .

# Como usar

Clone ou baixe o repositório e execute o script *todutrar.py* com os seguintes argumentos:

    python todutrar.py entrada saúda codificação-da-entrada codificação-da-saída

1. Entrada: arquivo de texto original
2. Saída*: arquivo com a transcrição fonética (padrão: "fonetizado.txt")
3. Codificação da entrada*: codificação do arquivo original (padrão: "utf8")
4. Codificação da saída*: codificação do arquivo alvo (padrão: "utf8")


(*) **Argumentos opcionais**


# Regras de transformação

# Deficiências
* O **todutrar** não consegue identificar as sílabas tônicas das palavras e, por isso, algumas transcrições fonéticas não conseguem ser fiéis à fala do português brasileiro.