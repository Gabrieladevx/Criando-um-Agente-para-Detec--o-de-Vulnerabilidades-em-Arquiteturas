# Autenticação Fraca

**Descrição:**
O uso de credenciais padrão, senhas fracas ou hardcoded facilita ataques de força bruta e acesso não autorizado.

**Exemplo:**
No arquivo `app_vulneravel/auth_fraca/app.py`, o usuário e senha estão fixos no código:

```python
USUARIO = 'admin'
SENHA = '1234'
```

**Como explorar:**
Tente autenticar com as credenciais padrão.

**Como mitigar:**

- Nunca use senhas padrão ou credenciais codificadas no código; armazene segredos em um gerenciador de segredos confiável ou em variáveis de ambiente seguras.

- Exija senhas fortes e políticas de expiração; armazene apenas hashes seguros (bcrypt, Argon2).

- Habilite autenticação multifator (MFA) e limite tentativas de login (rate limiting / bloqueio temporário).

- Registre e monitore tentativas de autenticação e reveja logs regularmente.

- Faça varreduras automatizadas e revisão de código para detectar credenciais vazadas.
- Implemente autenticação forte e política de senhas
- Implemente autenticação forte e política de senhas
