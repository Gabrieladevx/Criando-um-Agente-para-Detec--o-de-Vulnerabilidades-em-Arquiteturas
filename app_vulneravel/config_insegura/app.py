# Exemplo de configuração insegura
from flask import Flask
import os
app = Flask(__name__)

# Chave secreta exposta (má prática)
app.config['SECRET_KEY'] = 'segredo_super_fraco'

@app.route('/')
def index():
    return 'Aplicação rodando com configuração insegura!'

if __name__ == '__main__':
    app.run(debug=True, port=5004)
