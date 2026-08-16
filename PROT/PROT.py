"""
PROT - Translating RNA to Protein
========================================================================
Code for PROT exercise without using BioPython Package
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

from core.aminoacidos import AMINOACIDOS
from utils.files import encontrar_arquivo, extrair_conteudo_arquivo


def traducao():

    arquivo = encontrar_arquivo(__file__)
    rna = extrair_conteudo_arquivo(arquivo)

    proteina = []
    for i in range(0, len(rna), 3):
        codon = rna[i:i + 3]
        proteina.append(AMINOACIDOS[codon])
    return ''.join(proteina)


if __name__ == "__main__":
    resultado = traducao()
    print(resultado)
