"""
HAMM - Inferring mRNA from Protein
========================================================================
Code for HAMM exercise without using BioPython Package
========================================================================
Problem

Given two strings s and t of equal length, the Hamming distance between s and t,
denoted dH(s,t), is the number of corresponding symbols that differ in s and t.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

Sample Dataset
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Sample Output
7
"""
from utils.files import encontrar_arquivo, extrair_multiplas_linhas_arquivo

if __name__ == "__main__":
    arquivo = encontrar_arquivo(__file__)
    sequencias = extrair_multiplas_linhas_arquivo(arquivo)
    print(sequencias)
    dna1 = sequencias[0]
    dna2 = sequencias[1]
    matches = 0
    print(dna1)
    print(dna2)
    
    for i in range(len(dna1)):
        if dna1[i] == dna2[i]:
            print(f"{i}:{dna2[i]}->{dna1[i]}:MATCH!")
            matches += 1

    print(f"MATCHES:{matches}")
    print()
    print(f"HAMM:{len(dna1) - matches}")