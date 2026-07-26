"""
Helpers para ajudar na leitura e tratamento de arquivos
======================================================
A pessoa deve baixar e salvar o arquivo do exercício na
pasta específica do exercício.

Exemplo: Suponha que você esteja trabalhando no exercício
DNA. Na hora de baixar o arquivo você deve salvá-lo na pasta
./rosalind-problems/DNA/<nome-do-arquivo>.txt

Obs.: A extensão .txt é como exemplo, mas pode ser um arquivo do
tipo FASTA, .pdf, etc...
"""


def extrair_conteudo_arquivo(filepath: str) -> str:

    with open(filepath) as f:
        content = f.read().strip()

    return content
