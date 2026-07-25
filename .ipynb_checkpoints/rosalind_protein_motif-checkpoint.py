import re

with open('/home/marco/Rosalind/3idmapping_2025_11_09.fasta') as f:
    arquivo = f.read().split('\n')


informações = []
indices_cabeçalho = []
for item in arquivo:
    if item.startswith('>'):
        informações.append(item)
        #print(arquivo.index(item))
        indices_cabeçalho.append(arquivo.index(item))

print("Índices do cabeçalho:")
print(indices_cabeçalho)
print()

valores_id = []
for item in informações:
    valores_id.append(item.strip('>sp').split(' ')[0])

#i=0
#for i in range(len(valores_id)):
#    valores_id[i] = valores_id[i].split('|')
#    valores_id[i].pop(0)




print()
print("Lista com os ids:")
print()
print(valores_id)

sequencias = []
for i in range(len(indices_cabeçalho)-1):
    valor = indices_cabeçalho[i] + 1
    proximo = indices_cabeçalho[i+1]
    sequencias.append(''.join(arquivo[valor:proximo]))

sequencias.append(''.join(arquivo[proximo + 1:]))

print()
print("Sequência proteica:")
print()
print(sequencias)
print()

id_sequencia = dict(zip(valores_id,sequencias))

print()
print("'ID':'Sequencia'")
print()
print(id_sequencia)

motivo = r"(?=(N[^P][ST][^P]))"
results_dict = {}

# Iterar sobre cada chave e sequência no dicionário
for valores_id, sequencia in id_sequencia.items():
    
    # Lista temporária para armazenar os índices desta proteína
    indices_sequencia = []
    
    # Usar re.finditer para buscar todas as correspondências
    # O loop só funciona se houver pelo menos uma correspondência
    for match in re.finditer(motivo, sequencia):
        
        # match.start() retorna o índice de início da correspondência
        index = match.start() + 1
        indices_sequencia.append(index)
        
    # Armazenar a lista de índices no dicionário de resultados
    results_dict[valores_id] = indices_sequencia

## Exibição dos Resultados
print()
print("--- 🧬 Resultados da Busca por Motivo 🧬 ---")

for valores_id, indices in results_dict.items():
    if indices:
        print(f"\n{valores_id}")
        for i in range(len(indices)):
            print(f"{indices[i]}", end=' ') 


