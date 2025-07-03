import argparse
import os
from app.generator import UnitTestGenerator
from app.test_runner import TestRunner
from app.utils import read_function_from_file, save_test_file

def main():
    parser = argparse.ArgumentParser(description="Gerador de Testes Unitários com LangChain e Azure ChatGPT.")
    parser.add_argument("--input", type=str, required=True, help="Caminho para o arquivo Python contendo a função a ser testada.")
    parser.add_argument("--output", type=str, default="tests/", help="Diretório para salvar os testes gerados. Padrão: tests/")

    args = parser.parse_args()

    input_file_path = args.input
    output_dir = args.output

    if not os.path.exists(input_file_path):
        print(f"Erro: Arquivo de entrada não encontrado: {input_file_path}")
        return

    try:
        function_code = read_function_from_file(input_file_path)
    except Exception as e:
        print(f"Erro ao ler o arquivo de entrada: {e}")
        return

    generator = UnitTestGenerator()
    print("Gerando testes unitários...")
    generated_test_code = generator.generate_tests(function_code)

    # Determinar o nome do arquivo de teste
    input_filename = os.path.basename(input_file_path)
    test_filename = f"test_{os.path.splitext(input_filename)[0]}.py"
    output_test_path = os.path.join(output_dir, test_filename)

    try:
        save_test_file(generated_test_code, output_test_path)
        print(f"✅ Teste gerado com sucesso: {output_test_path}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo de teste: {e}")
        return

    runner = TestRunner()
    print("Executando testes...")
    test_passed = runner.run_tests(output_test_path)

    if test_passed:
        print("Todos os testes passaram! 🎉")
    else:
        print("Alguns testes falharam. 😔")

if __name__ == "__main__":
    main()


