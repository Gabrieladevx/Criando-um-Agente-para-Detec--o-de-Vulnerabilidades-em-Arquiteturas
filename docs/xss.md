# Cross-Site Scripting (XSS)

**Descrição:**
XSS ocorre quando entradas do usuário são refletidas na página sem sanitização, permitindo execução de scripts maliciosos.

**Exemplo:**
No arquivo `app_vulneravel/xss/app.py`, o comentário é exibido sem filtragem:
**```python**
return f"Comentário recebido: {comentario}"

**Como explorar:**
Envie `<script>alert(1)</script>` no campo de comentário.

**Como mitigar:**

- Escape/sanitize todas as entradas exibidas
- Use frameworks que previnem XSS por padrão
