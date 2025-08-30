# Exemplo vulnerável a XSS
from flask import Flask, request
app = Flask(__name__)

@app.route('/comentario', methods=['GET', 'POST'])
def comentario():
    if request.method == 'POST':
        comentario = request.form['comentario']
        # Vulnerável a XSS: não faz sanitização
        return f"Comentário recebido: {comentario}"
    return '''<form method="post">
                Comentário: <input name="comentario">
                <input type="submit">
              </form>'''

if __name__ == '__main__':
    app.run(debug=True, port=5002)
