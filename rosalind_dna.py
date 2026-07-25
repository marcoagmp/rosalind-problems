
'''
    O método .open() cria um objeto e o método .read() lê o conteúdo e retorna
    tudo (inclusive os caracteres no final de linha '\n') como uma única string.

    O método .rstrip() retira o caracter '\n' do final da linha.

    O objeto 'Seq' é uma estrutura da biblioteca Biopython que lida
    melhor com sequências de bases nitrogenadas.
    '''

from Bio.Seq import Seq

with open('/home/marco/Rosalind/rosalind_dna.txt') as DNA:
    sequencia = Seq(DNA.read()).rstrip('\n')
    print(sequencia)

# Cria um dicionário que irá armazenar os valores das chaves 'A', 'C', 'G' e 'T'. 
nucleotideos = {}


for nt in sequencia:
    
    # Adiciona +1 a contagem ou cria uma nova chave nt:{'A': , 'C': , 'G': , 'T': } 
    if nt in nucleotideos:
        nucleotideos[nt] += 1
    else:
        nucleotideos[nt] = 1

print(nucleotideos)



