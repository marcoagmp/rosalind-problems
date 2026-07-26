"""
DNA - Counting DNA Nucleotides
Code for DNA exercise using BioPython Package
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

The 'Seq' method is an structure from BioPython library that is optmize
to deal with sequence of nucleotides.
"""

import os

from Bio.Seq import Seq

from utils.files import extrair_conteudo_arquivo

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "data")

caminho_arquivo = ""
if os.path.exists(DATA_DIR) and os.listdir(DATA_DIR):
    arquivo = os.listdir(DATA_DIR)[0]
    caminho_arquivo = os.path.join(os.path.abspath(DATA_DIR), arquivo)
else:
    print("Pasta sem arquivo ou extensão não é .txt")

sequencia = Seq(extrair_conteudo_arquivo(caminho_arquivo))

print(
    sequencia.count("A"),
    sequencia.count("C"),
    sequencia.count("G"),
    sequencia.count("T"),
)
