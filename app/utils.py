import os

def read_function_from_file(file_path: str) -> str:
    """Lê o conteúdo de uma função Python de um arquivo."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def save_test_file(content: str, output_path: str):
    """Salva o conteúdo gerado em um arquivo de teste."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)


