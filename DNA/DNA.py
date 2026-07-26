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

from line_profiler import profile

from utils.profiling import setup_profiler

setup_profiler(__file__)

from utils.files import extrair_conteudo_arquivo, encontrar_arquivo


@profile
def count_DNA():
    caminho_arquivo = encontrar_arquivo(__file__)

    nucleotides: dict[str, int] = {
        "A": 0,
        "C": 0,
        "G": 0,
        "T": 0,
    }
    if caminho_arquivo:
        dna = extrair_conteudo_arquivo(caminho_arquivo)
        for nucleotide in dna:
            nucleotides[nucleotide] += 1

        resultado = nucleotides.values()
        print(*resultado)
    else:
        print("Caminho não existe!")


if __name__ == "__main__":
    count_DNA()
