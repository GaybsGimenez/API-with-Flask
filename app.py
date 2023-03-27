"""
API: LUGAR PARA DISPONIBILIZAR RECURSOS OU FUNCINALIDADES

1. objetivo: criar uma api que disponibiliza a consulta, criação, edição e exclusão de livros
2. URL base: localhost
3. Endpoints: quais os verbos/funcionalidades que vao ser disponibilizados 
    - localhost/livro(GET)
    - localhost/livro(POST)
    - localhost/livros/id (GET)
    - localhost/livros/id(PUT)
    - localhost;livros/id (DELETE)
4. Quais rescursos serão disponibilizados: livros
    
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

#criar lista de dicionários

livros = [
    {
       'id':1,
       'titulo': 'O Senhor do Anéis - A Sociedade do Anel',
       'autor': 'J.R.R Tolkien' 
    },
    {
       'id':2,
       'titulo': 'Harry Potter e a Pedra Filosofal',
       'autor': 'J.K Rouling'
    },
    {
       'id':3,
       'titulo': 'James Clear',
       'autor': 'Hábitos Atômicos'
    }

]

#consultar(todos)
@app.route('/livros', methods=['GET'])  # adcionar a rota especifica - get = consultar
def obter_livros():
    return jsonify(livros)

#consultar por (id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
    
#editar
@app.route('/livros/<int:id>', methods=['PUT']) # put para alterar informação
def editar_livro_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros): #retorna tanto a lista quanto o livro em si
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

#criar
@app.route('/livros', methods=['POST'])  # post= criar algo
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

#excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)


#rodar
app.run(port=5000,host='localhost',debug=True)


