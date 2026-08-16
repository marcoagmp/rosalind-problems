"""Tabela do código genético, que mapeia códons de RNA para aminoácidos 
correspondentes. Cada códon é uma sequência de três nucleotídeos (A, U, C, G) 
que codifica um aminoácido específico ou um sinal de parada na síntese 
proteica. A tabela é organizada em quatro linhas, cada uma representando 
um nucleotídeo inicial (U, C, A, G) e todas as combinações possíveis de 
códons de RNA. 

Os aminoácidos são representados por suas abreviações de uma letra, e os 
códons de parada são indicados por '*'.
"""
AMINOACIDOS = {
    # 1ª Linha: U (Uracila)
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*', # Códon de Parada
    'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W', # Códon de Parada

    # 2ª Linha: C (Citosina)
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',

    # 3ª Linha: A (Adenina)
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',  # Start codon
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',

    # 4ª Linha: G (Guanina)
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }