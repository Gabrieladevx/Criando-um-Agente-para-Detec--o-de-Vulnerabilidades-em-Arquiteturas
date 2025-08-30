# SQL Injection

**Descrição:**
SQL Injection ocorre quando comandos SQL maliciosos são inseridos em campos de entrada, permitindo acesso ou manipulação indevida do banco de dados.

**Exemplo:**

```python
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
```

**Como explorar:**
Envie no campo usuário: `' OR '1'='1` e senha: `' OR '1'='1`.

**Como mitigar:**

- Use consultas parametrizadas (prepared statements): separe o SQL dos dados e passe parâmetros ao driver/ORM.
- Não concatene entradas do usuário em strings SQL; utilize APIs que aceitam parâmetros (ex.: cursor.execute(sql, params) ou parâmetros do ORM).

- Valide e sanitize entradas do usuário
