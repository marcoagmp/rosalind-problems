with open('/home/marco/Rosalind/rosalind_prot.txt') as DNA:
    dna = list(DNA.read().rstrip('\n'))
    print("Sequência original do arquivo:")
    print()
    
    for i in range(len(dna)):
        print(dna[i],end='')
    
    print()
    print(len(dna))
    print()

rna = []

print()
print("Sequencia RNA:")
print()

for i in range(len(dna)):
    if dna[i] == 'T':
        rna.append('U')
    else:
        rna.append(dna[i])
    
    print(rna[i], end='')

print()
print(len(rna))

print()
print("Sequencia Codon:")
print()

rna_m = []

for i in range(0,len(rna),3):
    codon = ''.join(rna[i:i+3])
    rna_m.append(codon)

print(rna_m)
print()
print(len(rna_m))

'''
Gemini comenta que não é tão eficiente mapear a tradução dessa maneira. 
É mais eficiente utilizar os códons como chaves e os valores como o código
de uma letra de aminoácidos

codons_fenilalanina = ['UUU','UUC']
codons_leucina = ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG']
codons_serina = ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC']
codons_tyrosina = ['UAU', 'UAC']
codons_cisteina = ['UGU', 'UGC']
codons_prolina = ['CCU', 'CCC', 'CCA', 'CCG']
codons_histidina = ['CAU','CAC']
codons_glutamina = ['CAA','CAG']
codons_arginina = ['CGU','CGC','CGA','CGG','AGA','AGG']
codons_isoleucina = ['AUU','AUC','AUA']
codons_treonina = ['ACU','ACC','ACA','ACG']
codons_asparagina = ['AAU','AAC']
codons_lisina = ['AAA','AAG']
codons_valina = ['GUU','GUC','GUA','GUG']
codons_alanina = ['GCU','GCC','GCA','GCG']
codons_aspartato = ['GAU','GAC']
codons_glutamato = ['GAA','GAG']
codons_glicina = ['GGU','GGC','GGA','GGG']
codons_parada = ['UAA','UAG','UGA']


aminoacidos = {

            'A': codons_alanina,
            'C': codons_cisteina,
            'D': codons_aspartato,
            'E': codons_glutamato,
            'F': codons_fenilalanina,
            'G': codons_glicina,
            'H': codons_histidina,
            'I': codons_isoleucina,
            'K': codons_lisina,
            'L': codons_leucina,
            'M': 'AUG',
            'N': codons_asparagina,
            'P': codons_prolina,
            'Q': codons_glutamina,
            'R': codons_arginina,
            'S': codons_serina,
            'T': codons_treonina,
            'V': codons_valina,
            'W': 'UGG',
            'Y': codons_tyrosina,
            '*': codons_parada
            }

'''

aminoacidos = {
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
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',     # 'AUG' também é o códon de INICIAÇÃO
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',

    # 4ª Linha: G (Guanina)
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }


proteina = []
for codon in range(len(rna_m)):
    proteina.append(aminoacidos[rna_m[codon]])
proteina = ''.join(proteina[:])

print()
print("Proteína:")
print()
print(proteina)

