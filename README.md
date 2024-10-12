# API de Doguinhos

Uma API simples para cadastrar, listar, atualizar e deletar informações sobre cachorros, incluindo nome, raça, idade e disponibilidade para adoção.

## Funcionalidades

- **Cadastrar doguinhos**: Nome, raça, idade e disponibilidade para adoção.
- **Consultar todos os doguinhos**.
- **Consultar doguinhos pelo nome**.
- **Atualizar dados de um doguinho**.
- **Deletar um doguinho do cadastro**.

## Tecnologias utilizadas

- **Flask**: Framework web em Python.
- **Flask-RESTful**: Extensão para construir APIs RESTful.
- **MongoDB**: Banco de dados NoSQL utilizado para armazenar as informações dos doguinhos.
- **Flask-PyMongo**: Para conectar o MongoDB ao Flask.
- **Flask-Marshmallow**: Para serialização e validação de dados.
- **PyMongo**: Biblioteca para conectar com MongoDB.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado:

1. **Python 3.x**: Você pode baixar a versão mais recente de [python.org](https://www.python.org/downloads/).
2. **MongoDB**: Um banco de dados MongoDB rodando localmente ou em um serviço de nuvem como o [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).

## Passo a passo para rodar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/api-doguinho.git
```

### 2. Criar um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```
Caso não tenha o arquivo requirements.txt, você pode instalar as dependências manualmente:

```bash
pip install Flask Flask-RESTful Flask-PyMongo Flask-Marshmallow marshmallow-sqlalchemy pymongo
```

### 4. Rodar a aplicação

```bash
python app.py
```

## Uso

### 1. Criar doguinhos
```bash
POST: http://localhost:5000/dogs
```

### 2. Atualizar doguinhos 
```bash
PUT: http://localhost:5000/dogs/<id-do-doguinho>
```

### 3. Listar todos os doguinhos ou algum doguinho específico 
```bash
ALL GET: http://localhost:5000/dogs/
GET BY ID: http://localhost:5000/dogs/<id-do-doguinho>
```

### 4. Remover doguinhos :(
```bash
DELETE: http://localhost:5000/dogs/<id-do-doguinho>
```