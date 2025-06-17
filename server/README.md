# Credit Card Fraud Detection - Server

Este projeto é uma API para predição de fraudes de cartão de crédito, utilizando um modelo de machine learning treinado com dados de transações. A API permite enviar dados de transações e receber uma predição sobre a probabilidade de fraude.

## Instalação e Execução da API

### Pré-requisitos

- [Python](https://www.python.org/downloads/) (versão 3.8 ou superior)
- Virtualenv (opcional, mas recomendado)

### Passos para Instalação

1. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

Executando a API

Para iniciar a API, execute o seguinte comando no diretório raiz do projeto:

```bash
flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento, utilize o modo reload para que as mudanças no código sejam refletidas automaticamente:

```bash
flask run --host 0.0.0.0 --port 5000 --reload
```

Acesse [`http://localhost:5000`](http://localhost:5000) no navegador para visualizar a documentação da API e testar os endpoints.
