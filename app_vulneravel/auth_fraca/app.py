# Exemplo de autenticação fraca
from flask import Flask, request
app = Flask(__name__)

# Usuário e senha hardcoded (má prática)
USUARIO = 'admin'
SENHA = '1234'

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    senha = request.form['senha']
    if usuario == USUARIO and senha == SENHA:
        return 'Login bem-sucedido!'
    else:
        return 'Falha no login.'

if __name__ == '__main__':
    app.run(debug=True, port=5003)
