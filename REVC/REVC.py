"""
REVC - Complementing a Strand of DNA
========================================================================
Code for REVC exercise without using BioPython Package
========================================================================

Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as
are 'C' and 'G'. The reverse complement of a DNA string s is the string
s^c formed by reversing the symbols of s, then taking the complement of
each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Input: A DNA string s of length at most 1000 bp.

Output: The reverse complement s^c of s.

Sample Dataset
AAAACCCGGT

Sample Output
ACCGGGTTTT
"""

from line_profiler import profile

from utils.profiling import setup_profiler
from utils.files import extrair_conteudo_arquivo, encontrar_arquivo

setup_profiler(__file__)


@profile
def reverso_complementar():

    arquivo = encontrar_arquivo(__file__)

    mapa: dict[str, str] = {"A": "T", "C": "G", "G": "C", "T": "A"}
    temp = []

    if arquivo:
        dna = extrair_conteudo_arquivo(arquivo)
        print(dna)
        print()
        for base in dna:
            temp.append(mapa[base])
        complementar = "".join(temp[:])
        reverso_complementar = complementar[::-1]
        print(reverso_complementar)
    else:
        print("Arquivo não encontrado!")


if __name__ == "__main__":
    reverso_complementar()
