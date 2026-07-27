"""
RNA - Transcribing DNA into RNA
Code for RNA exercise without using BioPython Package
========================================================================
Problem
An RNA string is a string formed from the alphabet containing 'A', 'C',
'G', and 'U'. Given a DNA string t corresponding to a coding strand, its
transcribed RNA string u is formed by replacing all occurrences of 'T'
in t with 'U' in u.

Input:
    A DNA string t having length at most 1000 nt.

Return:
    The transcribed RNA string of t.

Sample Dataset
`GATGGAACTTGACTACGTAAATT`

Sample Output
`GAUGGAACUUGACUACGUAAAUU`
"""

from line_profiler import profile

from utils.profiling import setup_profiler
from utils.files import extrair_conteudo_arquivo, encontrar_arquivo

setup_profiler(__file__)


@profile
def transcription():
    caminho_arquivo = encontrar_arquivo(__file__)

    if caminho_arquivo:
        dna = extrair_conteudo_arquivo(caminho_arquivo)
        rna = dna.replace("T", "U")
        print(rna)
    else:
        print("Caminho não existe!")


if __name__ == "__main__":
    transcription()
