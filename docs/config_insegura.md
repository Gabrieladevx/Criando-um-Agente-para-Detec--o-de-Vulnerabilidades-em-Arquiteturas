# Configuração Insegura

**Descrição:**
Configurações inseguras, como chaves secretas fracas ou expostas, aumentam o risco de ataques.

**Exemplo:**
No arquivo `app_vulneravel/config_insegura/app.py`, a chave secreta está exposta:

app.config['SECRET_KEY'] = 'segredo_super_fraco'

**Como explorar:**
Verifique se a chave está exposta no código.

**Como mitigar:**

- Use variáveis de ambiente para segredos

- Gere chaves fortes e nunca exponha no código
