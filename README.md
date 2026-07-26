# Rosalind Problems

Soluções, códigos e anotações de estudo para problemas de bioinformática do
[Rosalind](https://rosalind.info/problems/locations/), focados na trilha
**Bioinformatics Stronghold**. O objetivo deste repositório é praticar
manipulação de sequências biológicas (DNA, RNA e proteínas) em Python, tanto
com bibliotecas prontas (Biopython) quanto implementando a lógica na mão.

## Problemas resolvidos

| Problema (Rosalind) | Descrição | Solução | Entrada |
| --- | --- | --- | --- |
| [DNA — Counting DNA Nucleotides](https://rosalind.info/problems/dna/) | Conta a quantidade de cada base (A, C, G, T) em uma sequência de DNA. Ver [`DNA/README.md`](DNA/README.md) — inclui profiling comparando a versão manual com Biopython. | [`DNA/DNA.py`](DNA/DNA.py) (sem bibliotecas externas), [`DNA/DNA_BioPython.py`](DNA/DNA_BioPython.py) (com Biopython) | [`DNA/data/rosalind_dna_dataset.txt`](DNA/data/rosalind_dna_dataset.txt) |
| [RNA — Transcribing DNA into RNA](https://rosalind.info/problems/rna/) | Transcreve uma sequência de DNA em RNA, trocando `T` por `U`. | *ainda sem script próprio* — a lógica antiga foi removida no refactor do DNA e este exercício ainda não foi reimplementado na nova estrutura | [`RNA/rosalind_rna.txt`](RNA/rosalind_rna.txt) |
| [REVC — Complementing a Strand of DNA](https://rosalind.info/problems/revc/) | Calcula o complemento reverso de uma sequência de DNA. | *ainda sem script próprio* — mesmo caso do RNA acima | [`REVC/rosalind_revc.txt`](REVC/rosalind_revc.txt) |
| [SUBS — Finding a Motif in DNA](https://rosalind.info/problems/subs/) | Encontra todas as posições em que um motivo (substring) ocorre em uma sequência de DNA. | [`SUBS/rosalind_dna_motif.py`](SUBS/rosalind_dna_motif.py) | [`SUBS/rosalind_subs.txt`](SUBS/rosalind_subs.txt) |
| [PROT — Translating RNA into Protein](https://rosalind.info/problems/prot/) | Traduz uma sequência de RNA em uma cadeia de aminoácidos usando a tabela do código genético. | [`PROT/rosalind_rna_protein.py`](PROT/rosalind_rna_protein.py) | [`PROT/rosalind_prot.txt`](PROT/rosalind_prot.txt) |
| [ORF — Open Reading Frames](https://rosalind.info/problems/orf/) | Identifica todas as possíveis proteínas codificadas nas *open reading frames* de uma sequência de DNA. | [`ORF/finding_org_regions.ipynb`](ORF/finding_org_regions.ipynb) | [`ORF/rosalind_orf.txt`](ORF/rosalind_orf.txt) |
| [MPRT — Finding a Protein Motif](https://rosalind.info/problems/mprt/) | Busca o motivo N-glicosilação (`N{P}[ST]{P}`) em proteínas identificadas por IDs do UniProt. | [`MPRT/rosalind_protein_motif.py`](MPRT/rosalind_protein_motif.py), [`MPRT/finding_protein_motif.ipynb`](MPRT/finding_protein_motif.ipynb), [`MPRT/finding_protein_motif_api.ipynb`](MPRT/finding_protein_motif_api.ipynb) (busca as sequências direto na API do UniProt) | [`MPRT/rosalind_mprt.txt`](MPRT/rosalind_mprt.txt) e arquivos `MPRT/*idmapping*.fasta` |

> `ORF/finding_org_regions-Copy1.ipynb` e `ORF/finding_org_regions-Copy2.ipynb` são
> versões de rascunho/experimentação do notebook do problema ORF, mantidas
> apenas como histórico de tentativas.
>

## Estrutura do repositório

```
.
├── DNA/             # DNA — Counting DNA Nucleotides (estrutura nova, com profiling)
│   ├── DNA.py
│   ├── DNA_BioPython.py
│   ├── data/        # dataset baixado do Rosalind para este exercício
│   ├── logs_profiler/  # gerado automaticamente pelo line_profiler a cada execução
│   └── README.md
├── RNA/             # RNA — Transcribing DNA into RNA
├── REVC/            # REVC — Complementing a Strand of DNA
├── SUBS/            # SUBS — Finding a Motif in DNA
├── PROT/            # PROT — Translating RNA into Protein
├── ORF/             # ORF — Open Reading Frames
├── MPRT/            # MPRT — Finding a Protein Motif (inclui os arquivos idmapping.fasta[.gz] do UniProt)
├── utils/           # código compartilhado entre exercícios (leitura de arquivo, setup de profiling)
├── pyproject.toml   # metadados do projeto e dependências (gerenciado com uv)
├── uv.lock          # versões exatas resolvidas das dependências
└── .python-version  # versão do Python usada pelo projeto
```

Cada pasta reúne o(s) script(s)/notebook(s) daquele problema junto com o
arquivo de entrada (`.txt`) baixado do Rosalind.

## Requisitos

O projeto é gerenciado com [uv](https://docs.astral.sh/uv/), que cuida do
ambiente virtual e das dependências automaticamente.

- Python 3.14 (fixado em [`.python-version`](.python-version))
- [Biopython](https://biopython.org/) — usado em `DNA/DNA_BioPython.py`
- [requests](https://pypi.org/project/requests/) — usado em `MPRT/finding_protein_motif_api.ipynb` para consultar a API do UniProt
- [Jupyter](https://jupyter.org/) — para abrir os arquivos `.ipynb`
- [line-profiler](https://github.com/pyutils/line_profiler) — usado para medir tempo de execução linha a linha (ver [`DNA/README.md`](DNA/README.md) e [`utils/profiling.py`](utils/profiling.py))

### Instalando o uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Instalando as dependências do projeto

```bash
uv sync
```

Esse comando cria o `.venv/` e instala exatamente as versões travadas em
`uv.lock`. Não é necessário ativar o ambiente virtual manualmente.

## Como executar

O exercício `DNA/` importa o pacote `utils/` (na raiz do projeto) com
import absoluto, então precisa ser executado **como módulo, a partir da
raiz do repositório**:

```bash
uv run python -m DNA.DNA
```

```bash
uv run python -m DNA.DNA_BioPython
```

Os demais exercícios (`RNA/`, `REVC/`, `SUBS/`, `PROT/`, `ORF/`, `MPRT/`)
ainda são scripts avulsos, escritos originalmente com caminhos de arquivo
fixos (ex.: `/home/marco/Rosalind/rosalind_dna.txt`). Antes de rodar, ajuste
o caminho do `open(...)` em cada script para apontar para o arquivo `.txt`
correspondente dentro da respectiva pasta, e rode normalmente por caminho:

```bash
uv run python SUBS/rosalind_dna_motif.py
```

Para os notebooks, basta abrir com Jupyter:

```bash
uv run jupyter lab ORF/finding_org_regions.ipynb
```

Para adicionar uma nova dependência ao projeto:

```bash
uv add <pacote>
```

## Observações

Este é um repositório de estudo pessoal: o código prioriza clareza da lógica
de cada problema em vez de reuso ou performance, e alguns comentários em
português documentam o raciocínio por trás de cada etapa.
