import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

class UnitTestGenerator:
    def __init__(self):
        self.llm = self._configure_azure_openai()

    def _configure_azure_openai(self):
        # Configuração do Azure OpenAI
        # Certifique-se de que as variáveis de ambiente estão definidas
        # AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_VERSION, AZURE_OPENAI_DEPLOYMENT_NAME
        return AzureChatOpenAI(
            openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            temperature=0.7 # Adicionado para maior criatividade na geração de testes
        )

    def generate_tests(self, function_code: str) -> str:
        # Lógica para gerar testes unitários
        prompt_template = PromptTemplate(
            input_variables=["function_code"],
            template="""
            Você é um engenheiro de software especialista em testes unitários Python.
            Sua tarefa é gerar testes unitários Pytest para a seguinte função Python.
            Certifique-se de cobrir casos de uso comuns e casos de borda.
            O teste deve ser independente e não deve depender de arquivos externos.
            Retorne apenas o código Python do teste, sem explicações adicionais.
            Inclua a importação da função original se necessário.

            Função:
            {function_code}

            Testes Pytest:
            """
        )

        chain = LLMChain(llm=self.llm, prompt=prompt_template)
        response = chain.invoke({"function_code": function_code})
        
        # O LangChain retorna um dicionário, precisamos extrair o texto gerado
        generated_text = response.get('text', '').strip()
        
        # Tentar extrair apenas o bloco de código Python se houver formatação Markdown
        if generated_text.startswith('```python') and generated_text.endswith('```'):
            generated_text = generated_text[len('```python'):-len('```')].strip()
        elif generated_text.startswith('```') and generated_text.endswith('```'):
            generated_text = generated_text[len('```'):-len('```')].strip()
            
        return generated_text

if __name__ == '__main__':
    # Exemplo de uso (para testes internos)
    generator = UnitTestGenerator()
    sample_code = """
def soma(a, b):
    return a + b
"""
    generated_test = generator.generate_tests(sample_code)
    print(generated_test)


