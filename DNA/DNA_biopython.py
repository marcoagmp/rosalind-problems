"""
DNA - Counting DNA Nucleotides
========================================================================
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
from line_profiler import profile
from utils.profiling import setup_profiler
from utils.files import extrair_conteudo_arquivo, encontrar_arquivo

setup_profiler(__file__)


@profile
def biopython_count_DNA():
    caminho_arquivo = encontrar_arquivo(os.path.abspath(__file__))

    if caminho_arquivo:
        sequencia = Seq(extrair_conteudo_arquivo(caminho_arquivo))
        print(
            sequencia.count("A"),
            sequencia.count("C"),
            sequencia.count("G"),
            sequencia.count("T"),
        )
    else:
        print("Caminho não existe!")


if __name__ == "__main__":
    biopython_count_DNA()
