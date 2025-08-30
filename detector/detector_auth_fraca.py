# Script para detectar autenticação fraca (usuário/senha padrão)
import requests

url = 'http://localhost:5003/login'
payload = {'usuario': 'admin', 'senha': '1234'}

response = requests.post(url, data=payload)
if 'Login bem-sucedido' in response.text:
    print('Possível autenticação fraca detectada!')
else:
    print('Nenhuma vulnerabilidade detectada.')
