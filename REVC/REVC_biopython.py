"""
REVC - Complementing a Strand of DNA
Code for REVC exercise using BioPython Package
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
from Bio.Seq import Seq

from utils.profiling import setup_profiler
from utils.files import extrair_conteudo_arquivo, encontrar_arquivo

setup_profiler(__file__)


@profile
def bio_python_reverso_complementar():

    arquivo = encontrar_arquivo(__file__)

    if arquivo:
        dna = Seq(extrair_conteudo_arquivo(arquivo))
        reverso_complementar = dna.reverse_complement()
        print(reverso_complementar)
    else:
        print("Arquivo não encontrado!")


if __name__ == "__main__":
    bio_python_reverso_complementar()
