with open('/home/marco/Rosalind/rosalind_subs.txt') as DNA:
    DNA = DNA.read().rsplit('\n')
    DNA.pop()
    dna, motif = DNA


contador = 0
resultado = []
for i in range(len(dna)):
    variavel = ''.join(dna[i:i+9])
    if variavel == motif:
        contador += 1
        resultado.append(i+1)
    else:
        continue
print()
print(contador)
print()
for i in range(len(resultado)):
    print(resultado[i],end=' ')



