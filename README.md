# Tradutor fonético pt-BR

O **todutrar** traduz arquivos de texto para uma representação semi-fiel do IPA (Alfabeto Fonético Internacional). Algumas opções de transcrição são da variante carioca do português brasileiro; outras, são da fonologia da língua portuguesa.

## Como usar

Clone ou baixe o repositório e execute o script *todutrar.py* com os seguintes argumentos:

    python todutrar.py input output encoding-input encoding-output

1. Input: arquivo de texto original
2. Output*: arquivo com a transcrição fonética (padrão: "fonetizado.txt")
3. Encoding-input*: codificação do arquivo original (padrão: "utf8")
4. Encoding-output*: codificação do arquivo alvo (padrão: "utf8") 
(*) **Argumentos opcionais**

## Regras de transformação

## Deficiências
* O **todutrar** não consegue identificar as sílabas tônicas das palavras e, por isso, algumas transcrições fonéticas não conseguem ser fiéis à fala do português brasileiro.