import os
from line_profiler import profile


def setup_profiler(script_path: str) -> None:
    """
    Configura o line_profiler para salvar os logs dentro de uma pasta
    'logs_profiler' na mesma pasta do script que está sendo executado.
    """
    filepath = os.path.abspath(script_path)
    nome_arquivo = script_path.rsplit("/", maxsplit=1)[1]
    nome_dir = nome_arquivo.split(".")[0]

    pasta_exercicio = os.path.join(os.path.dirname(filepath), "logs_profiler")
    pasta_logs = os.path.join(pasta_exercicio, nome_dir)
    os.makedirs(pasta_logs, exist_ok=True)
    profile.enable(output_prefix=os.path.join(pasta_logs, "profile_output"))
