"""
PROT - Translating RNA to Protein
========================================================================
Code for PROT exercise using BioPython Package
========================================================================

Problem
The 20 commonly occurring amino acids are abbreviated by using 20 letters
from the English alphabet (all letters except for B, J, O, U, X, and Z).
Protein strings are constructed from these 20 symbols. Henceforth, the
term genetic string will incorporate protein strings along with DNA strings
and RNA strings.

The RNA codon table dictates the details regarding the encoding of
specific codons into the amino acid alphabet.

Given:
An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return:
The protein string encoded by s.

Sample Dataset:
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

Sample Output:
MAMAPRTEINSTRING
"""

from Bio.Seq import Seq

from core.aminoacidos import AMINOACIDOS
from utils.files import encontrar_arquivo, extrair_conteudo_arquivo


def Biopython_traducao():

    arquivo = encontrar_arquivo(__file__)
    rna = Seq(extrair_conteudo_arquivo(arquivo))
    proteina = rna.translate()
    return proteina


if __name__ == "__main__":
    resultado = Biopython_traducao()
    print(resultado)
