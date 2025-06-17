# Credit Card Fraud Detection

## Descrição do Projeto

Este projeto é uma aplicação fullstack para detecção de fraudes em transações de cartão de crédito desenvolvida como parte do trabalho final da disciplina de Engenharia de Sistemas de Software Inteligentes do curso de Engenharia de Software da Pontifícia Universidade Católica do Rio de Janeiro (PUC-Rio).

## Execução do Projeto

Este projeto é dividido em três partes principais:

1. **Web**: Desenvolvido em HTML e JavaScript, responsável pela interface do usuário.
2. **Server**: Desenvolvido em Python, responsável por receber os dados da transação, processá-los e retornar a predição de fraude.
3. **Machine Learning**: Desenvolvido em Python, contém o modelo de machine learning treinado com dados de transações. O modelo é responsável por analisar os dados recebidos do servidor e fornecer uma predição sobre a probabilidade de fraude.

## Pré-requisitos

- Python 3.8 ou superior

## Inicialização do Projeto

1. Clone o repositório

2. Navegue até o diretório do projeto:

```bash
cd credit-card-fraud-detection
```

3. Inicialize o ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Inicie o servidor:

```bash
cd server
flask run --host 0.0.0.0 --port 5000
```

6. Abra o arquivo [`web/index.html`](web/index.html) no navegador para acessar a interface do usuário.

Agora com o servidor em execução, você pode enviar dados de transações através da interface web e receber predições sobre a probabilidade de fraude.
