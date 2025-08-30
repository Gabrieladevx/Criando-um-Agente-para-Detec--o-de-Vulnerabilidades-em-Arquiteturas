# Script simples para detectar XSS refletido
import requests

url = 'http://localhost:5002/comentario'
payload = {'comentario': '<script>alert(1)</script>'}

response = requests.post(url, data=payload)
if '<script>alert(1)</script>' in response.text:
    print('Possível vulnerabilidade de XSS detectada!')
else:
    print('Nenhuma vulnerabilidade detectada.')
