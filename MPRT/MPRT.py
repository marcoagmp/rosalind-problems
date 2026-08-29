"""
MPRT - Finding a Protein Motif
========================================================================
Code for MPRT exercise without using BioPython Package
========================================================================

Problem
To allow for the presence of its varying forms, a protein motif is
represented by a shorthand as follows: [XY] means "either X or Y" and {X}
means "any amino acid except X." For example, the N-glycosylation motif
is written as N{P}[ST]{P}.

You can see the complete description and features of a particular protein
by its access ID "uniprot_id" in the UniProt database, by inserting the
ID number into http://www.uniprot.org/uniprot/uniprot_id.

Alternatively, you can obtain a protein sequence in FASTA format by following
http://www.uniprot.org/uniprot/uniprot_id.fasta. For example, the data
for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its
given access ID followed by a list of locations in the protein string
where the motif can be found.

Sample Dataset
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST
Sample Output
B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614
"""

import requests
import re

from utils.files import encontrar_arquivo, extrair_multiplas_linhas_arquivo


def extract_protein_sequences(uniprot_ids: list[str]) -> dict[str, str]:
    """
    Extrai as sequências de proteínas do UniProt para uma lista de IDs fornecida.
    Retorna um dicionário com os IDs como chaves e as sequências correspondentes como valores.
    """
    sequencias_fasta = {}
    with requests.Session() as session:
        for uniprot_id in uniprot_ids:
            url = f"http://www.uniprot.org/uniprot/{uniprot_id}.fasta"
            response = session.get(url)
            if response.status_code == 200:
                sequences = response.text.splitlines()[
                    1:
                ]  # sequência sem o cabeçalho
                sequencias_fasta[uniprot_id] = {"sequence": "".join(sequences)}
            else:
                print(f"Erro ao acessar {url}: {response.status_code}")
    return sequencias_fasta


def normalize_id(uniprot_id: list) -> list:
    """
    Normaliza o ID do UniProt para o formato correto.
    """
    normalized_ids = []
    for id in uniprot_id:
        if "_" in id:
            normalized_ids.append(id.split("_")[0])
        else:
            normalized_ids.append(id.strip())
    return normalized_ids


def finding_protein_motif():
    arquivo = encontrar_arquivo(__file__)
    conteudo = extrair_multiplas_linhas_arquivo(arquivo)

    uniprot_ids = normalize_id(conteudo)
    sequencias_fasta = extract_protein_sequences(uniprot_ids)
    print(sequencias_fasta)
    print()

    # r = raw; ?= sobreposição de correspondências;
    # [^P] = qualquer aminoácido exceto Prolina (P)
    # [ST] = Serina (S) OU Treonina (T)
    motivo = r"(?=(N[^P][ST][^P]))"
    for id, value in sequencias_fasta.items():

        matches = [
            m.start() + 1
            for m in re.finditer(motivo, value.get("sequence", ""))
        ]
        if matches:
            sequencias_fasta[id]["motif_positions"] = " ".join(
                map(str, matches)
            )
        else:
            sequencias_fasta[id]["motif_positions"] = " "

    for id, value in sequencias_fasta.items():
        if "motif_positions" in value:
            print(f"{id}")
            print(value["motif_positions"])


if __name__ == "__main__":
    finding_protein_motif()
