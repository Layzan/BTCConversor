# Conversor de Bitcoin

Este é um projeto simples feito com **FastAPI** que converte valores de Bitcoin para outras moedas (como USD, BRL, EUR etc.) utilizando a API pública do [CoinGecko](https://www.coingecko.com/).

A aplicação possui:

* Uma interface web com HTML e Jinja2
* Um endpoint `/convert` que realiza a conversão em tempo real
* Possibilidade de rodar localmente ou em um container Docker

---

## 🚀 Como rodar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/conversor-bitcoin.git
cd conversor-bitcoin
```

### 2. Rodar localmente com ambiente virtual (recomendado)

#### Criar o ambiente virtual

```bash
python -m venv venv
```

#### Ativar o ambiente virtual

* No Windows:

```bash
venv\Scripts\activate
```

* No Linux/Mac:

```bash
source venv/bin/activate
```

#### Instalar as dependências

```bash
pip install -r requirements.txt
```

#### Rodar o servidor

```bash
uvicorn app.main:app --reload
```

Acesse em: [http://localhost:8000](http://localhost:8000)

---

### 3. Rodar com Docker

#### Build da imagem

```bash
docker build -t conversor-bitcoin .
```

#### Executar o container

```bash
docker run -d -p 8000:8000 --name conversor-bitcoin-app conversor-bitcoin
```

Acesse em: [http://localhost:8000](http://localhost:8000)

---

## 🛠 Estrutura do Projeto

```
conversor-bitcoin/
├── app/
│   ├── templates/
│   │   └── index.html
│   ├── main.py
│   └── api.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 📌 Requisitos

* Python 3.11+
* Docker (opcional, caso deseje usar container)


---

Feito com ❤️ por \[Seu Nome]
