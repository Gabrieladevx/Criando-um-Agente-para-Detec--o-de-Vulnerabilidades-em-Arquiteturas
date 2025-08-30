# Exemplo vulnerável a SQL Injection
from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Vulnerável a SQL Injection!
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        return 'Login bem-sucedido!'
    else:
        return 'Falha no login.'

if __name__ == '__main__':
    app.run(debug=True, port=5001)
