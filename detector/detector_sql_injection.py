# Detector de SQL Injection com saída de debug
import requests

url = 'http://127.0.0.1:5001/login'
payload = {'username': "' OR '1'='1", 'password': "' OR '1'='1"}

try:
    response = requests.post(url, data=payload, timeout=5)
    print('status_code:', response.status_code)
    print('response_text:', repr(response.text))
    if 'Login bem-sucedido' in response.text:
        print('Possível vulnerabilidade de SQL Injection detectada!')
    else:
        print('Nenhuma vulnerabilidade detectada.')
except Exception as e:
    print('Erro ao conectar ao endpoint:', e)
