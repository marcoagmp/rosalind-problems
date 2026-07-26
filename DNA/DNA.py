"""
DNA - Counting DNA Nucleotides
Code for DNA exercise without using BioPython Package
========================================================================

Problem:
A string is simply an ordered collection of symbols selected from some
alphabet and formed into a word; the length of a string is the number of
symbols that it contains. An example of a length 21 DNA string (whose al-
phabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTC
TTACG."

Input: A DNA string s of length at most 1000 nt.

Output: Four integers (separated by spaces) counting the respective num-
ber of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""

import os

from utils.files import extrair_conteudo_arquivo

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "data")

caminho_arquivo = ""
if os.path.exists(DATA_DIR) and os.listdir(DATA_DIR):
    arquivo = os.listdir(DATA_DIR)[0]
    caminho_arquivo = os.path.join(os.path.abspath(DATA_DIR), arquivo)
else:
    print("Pasta sem arquivo ou extensão não é .txt")

nucleotides: dict[str, int] = {}
if caminho_arquivo:
    dna = extrair_conteudo_arquivo(caminho_arquivo)
    for nucleotide in dna:
        if nucleotide in nucleotides:
            nucleotides[nucleotide] += 1
        else:
            nucleotides[nucleotide] = 1
else:
    print("Caminho não existe!")

resultado = nucleotides.values()

print(*resultado)
