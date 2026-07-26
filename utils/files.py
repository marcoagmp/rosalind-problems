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

import os


def extrair_conteudo_arquivo(filepath: str) -> str:

    with open(filepath) as f:
        content = f.read().strip()

    return content


def encontrar_arquivo(filepath: str) -> str:
    SCRIPT_DIR = os.path.dirname(filepath)

    if "data" in os.listdir(SCRIPT_DIR):
        DATA_DIR = os.path.join(SCRIPT_DIR, "data")
    else:
        DIR = SCRIPT_DIR.rsplit("/", maxsplit=1)
        return f"{DIR} não possui pasta /data"

    caminho_arquivo = ""
    if os.path.exists(DATA_DIR) and os.listdir(DATA_DIR):
        arquivo = os.listdir(DATA_DIR)[0]
        caminho_arquivo = os.path.join(os.path.abspath(DATA_DIR), arquivo)
    else:
        return "Pasta sem arquivos!"

    return caminho_arquivo
