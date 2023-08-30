# API-com-Flask 
Flask: https://flask.palletsprojects.com/en/2.2.x/quickstart/#redirects-and-errors 
Criação de api com python, para rodar local - usando postman: https://www.postman.com/

# Livro API

Esta é uma API construída usando o framework Flask, projetada para gerenciar informações sobre livros. Ela oferece operações básicas de consulta, criação, edição e exclusão de livros.

## Endpoints

### Consultar todos os livros

- **URL:** `GET /livros`
- **Descrição:** Retorna uma lista de todos os livros disponíveis.

### Consultar um livro por ID

- **URL:** `GET /livros/<int:id>`
- **Descrição:** Retorna os detalhes de um livro com base no seu ID.

### Editar um livro por ID

- **URL:** `PUT /livros/<int:id>`
- **Descrição:** Permite a edição das informações de um livro existente, usando o seu ID.

### Criar um novo livro

- **URL:** `POST /livros`
- **Descrição:** Adiciona um novo livro à coleção.

### Excluir um livro por ID

- **URL:** `DELETE /livros/<int:id>`
- **Descrição:** Remove um livro da coleção com base no seu ID.

## Recursos

A API lida com objetos de livro, cada um contendo as seguintes informações:

- `id`: Identificador único do livro.
- `titulo`: O título do livro.
- `autor`: O autor do livro.

## Exemplos de Uso

### Consultar todos os livros

**Requisição:**

```http
GET /livros
```

**Resposta:**

```json
[
    {"id": 1, "titulo": "O Senhor do Anéis", "autor": "J.R.R. Tolkien"},
    {"id": 2, "titulo": "Harry Potter", "autor": "J.K. Rowling"}
    // ...
]
```

### Consultar um livro por ID

**Requisição:**

```http
GET /livros/1
```

**Resposta:**

```json
{"id": 1, "titulo": "O Senhor do Anéis", "autor": "J.R.R. Tolkien"}
```

### Editar um livro por ID

**Requisição:**

```http
PUT /livros/1
```

**Corpo:**

```json
{"titulo": "Novo Título", "autor": "Novo Autor"}
```

**Resposta:**

```json
{"id": 1, "titulo": "Novo Título", "autor": "Novo Autor"}
```

### Criar um novo livro

**Requisição:**

```http
POST /livros
```

**Corpo:**

```json
{"titulo": "Novo Livro", "autor": "Autor Desconhecido"}
```

**Resposta:**

```json
{"id": 3, "titulo": "Novo Livro", "autor": "Autor Desconhecido"}
```

### Excluir um livro por ID

**Requisição:**

```http
DELETE /livros/1
```

**Resposta:**

```json
{"message": "Livro removido com sucesso"}
```

## Execução

Para rodar a API, assegure-se de ter o Flask instalado. Em seguida, execute o arquivo `app.py`. A API estará acessível em `http://localhost:5000`.

```bash
$ python app.py
```

Lembre-se de substituir `<int:id>` nas URLs pelos IDs reais dos livros que deseja consultar, editar ou excluir.
