import pytest
import os

class TestRunner:
    def __init__(self):
        pass

    def run_tests(self, test_file_path: str) -> bool:
        """Executa testes Pytest em um arquivo específico."""
        if not os.path.exists(test_file_path):
            print(f"Erro: Arquivo de teste não encontrado: {test_file_path}")
            return False
        
        # Pytest pode ser executado programaticamente
        # Captura a saída para verificar o resultado
        # -s: não suprime a saída (para ver prints)
        # --tb=no: não mostra traceback completo em caso de falha
        # -q: modo silencioso
        try:
            # pytest.main retorna um código de saída. 0 para sucesso, != 0 para falha.
            result = pytest.main([test_file_path, '-s', '--tb=no', '-q'])
            if result == 0:
                print(f"✅ Teste executado: PASSED")
                return True
            else:
                print(f"❌ Teste executado: FAILED")
                return False
        except Exception as e:
            print(f"Ocorreu um erro ao executar os testes: {e}")
            return False


