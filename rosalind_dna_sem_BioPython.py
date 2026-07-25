with open('/home/marco/Rosalind/rosalind_dna.txt') as DNA:
    dna = list(DNA.read().rstrip('\n'))
    print("Sequência original do arquivo:")
    print()
    
    for i in range(len(dna)):
        print(dna[i],end='')
    
    print()
    print(len(dna))
    print()

A = dna.count('A')
C = dna.count('C')
G = dna.count('G')
T = dna.count('T')

print ('A =',A,'C =',C,'G =',G,'T =',T)
print()

'''
'''
'''
Transcrição do DNA para RNA (troca da base T por U)
'''
'''
with open('/home/marco/Rosalind/rosalind_rna.txt') as DNA:
    dna = list(DNA.read().rstrip('\n'))
    print(dna)

for i in range(len(dna)):
    if dna[i] == 'T':
        dna[i] = 'U'
    print(dna[i], end='')
'''


'''
Reverso complementar
'''

def reverso_complementar(dna):
    valor = []
    for i in range(len(dna)):
        if dna[i] == 'A':
            valor.append('T')
        elif dna[i] == 'C':
            valor.append('G')
        elif dna[i] == 'G':
            valor.append('C')
        elif dna[i] == 'T':
            valor.append('A')
        else:
            print('Base nao encontrada')
    return valor

with open('/home/marco/Rosalind/rosalind_revc.txt') as DNA:
    dna = list(DNA.read().rstrip('\n'))
    print("Sequência original do arquivo:")
    print()

    for i in range(len(dna)):
        print(dna[i],end='')

    print()
    print(len(dna))
    print()

print("O DNA reverso:")
print()

dna_reverso = reverso_complementar(dna)

for i in range(len(dna_reverso)):
    print(dna_reverso[i], end='')

print()
print()
print("O inverso do reverso:")
print()
dna_inverso_do_reverso = dna_reverso[::-1]

for i in range(len(dna_inverso_do_reverso)):
    print(dna_inverso_do_reverso[i], end='')
print()
print(len(dna))

