# DNA — Counting DNA Nucleotides

[Problema no Rosalind](https://rosalind.info/problems/dna/)

Conta quantas vezes cada base (`A`, `C`, `G`, `T`) aparece em uma sequência
de DNA. Este exercício tem duas implementações de propósito, para comparar
uma solução escrita à mão com uma solução usando uma biblioteca
especializada:

| Arquivo | Abordagem |
| --- | --- |
| [`DNA.py`](DNA.py) | Conta os nucleotídeos manualmente, iterando a string e acumulando em um `dict`. |
| [`DNA_BioPython.py`](DNA_BioPython.py) | Usa [`Bio.Seq.Seq`](https://biopython.org/) e o método `.count()` do Biopython. |

Entrada: [`data/rosalind_dna_dataset.txt`](data/rosalind_dna_dataset.txt).

## Profiling: comparando desempenho

O objetivo aqui não é só resolver o exercício, mas medir e comparar o
custo de cada abordagem — a mão vs. biblioteca pronta — usando o
[`line_profiler`](https://github.com/pyutils/line_profiler) para medir o
tempo de execução **linha a linha** dentro da função `main()`.

Isso é feito com duas peças reutilizáveis em [`utils/`](../utils/):

- [`utils/profiling.py`](../utils/profiling.py) — `setup_profiler(__file__)`
  liga o `line_profiler` e configura a pasta de saída como
  `<pasta_do_script>/logs_profiler/<nome_do_script>/`.
- O decorator `@profile` (importado de `line_profiler`) marca a função que
  deve ser medida.

Ao rodar `DNA.py` ou `DNA_BioPython.py`, o profiler gera automaticamente,
dentro de `logs_profiler/`:

- `profile_output.txt` — relatório legível, linha a linha, com tempo e
  percentual gasto em cada linha da função.
- `profile_output_<timestamp>.txt` — cópia do mesmo relatório com marca de
  tempo (histórico de execuções).
- `profile_output.lprof` — dados binários, para inspecionar depois com:

  ```bash
  python -m line_profiler -rtmz DNA/logs_profiler/DNA/profile_output.lprof
  ```

`logs_profiler/` é gerado automaticamente a cada execução e não deveria
ser versionado no git.

### Exemplo real (dataset atual, execução única)

| Versão | Tempo total medido |
| --- | --- |
| `DNA.py` (manual) | ~0,63 ms |
| `DNA_BioPython.py` (Biopython) | ~1,42 ms |

Nesta execução, a versão manual foi mais rápida — a maior parte do tempo
do `DNA_BioPython.py` foi gasta construindo o objeto `Seq(...)`, não nas
chamadas de `.count()` em si (isso fica visível no relatório linha a
linha). Isso não é uma conclusão geral sobre Biopython vs. código puro —
é só o que o profiling mostrou para essa entrada específica, e é
justamente esse tipo de coisa que vale a pena investigar com dados reais
em vez de supor.

## Como executar

Os scripts importam `utils` (pacote na raiz do projeto) com import
absoluto, então precisam ser executados **como módulo, a partir da raiz
do repositório**, e não pelo caminho do arquivo diretamente:

```bash
uv run python -m DNA.DNA
```

```bash
uv run python -m DNA.DNA_BioPython
```

## Convenção de dados

Cada exercício guarda seu dataset em uma subpasta `data/` (ver
[`utils/files.py`](../utils/files.py)): o arquivo baixado do Rosalind deve
ser salvo em `DNA/data/<nome-do-arquivo>`, e `encontrar_arquivo()` localiza
automaticamente o primeiro arquivo dessa pasta.
