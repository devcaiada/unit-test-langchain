# Gerando Testes Unitários com LangChain e Azure ChatGPT

## Introdução ao Projeto

Este projeto visa automatizar a geração de testes unitários para funções Python, utilizando o poder dos modelos de linguagem da Azure OpenAI (como ChatGPT/GPT-4) integrados via LangChain. Ele foi desenvolvido seguindo a abordagem de Test-Driven Development (TDD), servindo como um utilitário inteligente para otimizar a produtividade de desenvolvedores Python na criação e manutenção de testes automatizados.

## Tecnologias Utilizadas

*   **Python 3.11+**: Linguagem de programação principal.
*   **LangChain**: Framework para desenvolvimento de aplicações com modelos de linguagem.
*   **Azure OpenAI**: Provedor dos modelos de linguagem (ChatGPT/GPT-4).
*   **Pytest**: Framework para execução de testes unitários.
*   **python-dotenv**: Para gerenciamento de variáveis de ambiente.

## Como Configurar o Azure OpenAI

Para utilizar este projeto, você precisará configurar suas credenciais do Azure OpenAI. Siga os passos abaixo:

1.  **Crie uma conta no Azure** e configure um recurso de Azure OpenAI.
2.  **Obtenha suas credenciais**: Você precisará da `API Key`, `Endpoint`, `API Version` e `Deployment Name` do seu modelo.
3.  **Crie um arquivo `.env`**: Na raiz do projeto (`unit-test-gen/`), crie um arquivo chamado `.env` (você pode copiar e renomear o `.env.example`).
4.  **Preencha o arquivo `.env`** com suas credenciais:

    ```
    AZURE_OPENAI_API_KEY=sua_chave_api_aqui
    AZURE_OPENAI_ENDPOINT=seu_endpoint_aqui
    AZURE_OPENAI_API_VERSION=2024-02-15-preview
    AZURE_OPENAI_DEPLOYMENT_NAME=seu_deployment_name_aqui
    ```

    *Substitua os valores `sua_chave_api_aqui`, `seu_endpoint_aqui` e `seu_deployment_name_aqui` pelas suas credenciais reais.* A `API Version` pode variar, mas `2024-02-15-preview` é um bom ponto de partida.

## Passo a Passo de Instalação

1.  **Clone o repositório** (se aplicável, ou descompacte o projeto).
2.  **Navegue até o diretório do projeto**:

    ```bash
    cd unit-test-gen
    ```

3.  **Instale as dependências**:

    ```bash
    pip install -r requirements.txt
    ```

## Como Utilizar o Projeto

O projeto pode ser utilizado via interface de linha de comando (CLI).

**Exemplo de uso:**

```bash
python main.py --input examples/sample_function.py --output tests/
```

*   `--input`: Caminho para o arquivo Python contendo a função (ou funções) para a qual você deseja gerar testes.
*   `--output`: (Opcional) Diretório onde os testes gerados serão salvos. O padrão é `tests/`.

**Exemplo de entrada (`examples/sample_function.py`):**

```python
def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b
```

**Exemplo de saída (arquivo gerado em `tests/test_sample_function.py`):**

```python
# Conteúdo gerado pelo Azure ChatGPT
from examples.sample_function import soma, subtrai

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0
    assert soma(100, -50) == 50

def test_subtrai():
    assert subtrai(5, 2) == 3
    assert subtrai(10, 10) == 0
    assert subtrai(0, 5) == -5
    assert subtrai(-5, -2) == -3
```

## Explicação de como a LangChain constrói os prompts

No arquivo `app/generator.py`, a classe `UnitTestGenerator` utiliza a biblioteca LangChain para interagir com o modelo da Azure OpenAI. Um `PromptTemplate` é definido com uma instrução clara para a IA, solicitando a geração de testes unitários Pytest para uma função Python fornecida. O template inclui diretrizes sobre cobertura de casos de uso e borda, e a necessidade de retornar apenas o código Python.

```python
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
```

Essa abordagem permite que a IA entenda o contexto e o formato esperado da saída, garantindo que os testes gerados sejam relevantes e bem estruturados.

## Como Executar os Testes

Após a geração, o próprio script `main.py` tenta executar os testes gerados usando o `pytest`. Você verá a saída no console indicando se os testes passaram ou falharam.

Para executar os testes manualmente (após a geração):

```bash
pytest tests/test_sample_function.py
```

Ou para executar todos os testes no diretório `tests/`:

```bash
pytest tests/
```

## Possíveis Melhorias Futuras

*   **Interface Web (FastAPI)**: Implementar uma interface web para facilitar o uso, permitindo upload de arquivos e visualização dos resultados no navegador.
*   **Histórico de Versões**: Integrar com um sistema de controle de versão (e.g., Git) ou um banco de dados simples para manter um histórico das versões dos testes gerados.
*   **Explicação do Raciocínio da IA**: Adicionar uma funcionalidade para que a IA explique o raciocínio por trás dos testes gerados, o que pode ser útil para depuração e aprendizado.
*   **Suporte a Múltiplas Funções no Mesmo Script**: Aprimorar a lógica para identificar e gerar testes para múltiplas funções dentro de um único arquivo de entrada de forma mais robusta.
*   **Configuração de Modelos**: Permitir que o usuário selecione diferentes modelos da Azure OpenAI (e.g., GPT-3.5, GPT-4) via linha de comando ou interface.
*   **Configuração de Prompts**: Oferecer opções para personalizar os prompts enviados à IA, permitindo maior controle sobre o estilo e a cobertura dos testes.
*   **Análise de Cobertura**: Integrar com ferramentas de cobertura de código (e.g., `coverage.py`) para reportar a porcentagem de código coberto pelos testes gerados.


