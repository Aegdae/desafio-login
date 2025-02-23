# Projeto Django - Autenticação de Usuários

Este é um projeto desenvolvido em Django que implementa um sistema de login e registro de usuários.

## Tecnologias Utilizadas
- Python
- Django
- SQLite (banco de dados padrão)
- HTML/CSS/JavaScript (para as páginas de autenticação)

## Funcionalidades
- Registro de usuário
- Login e logout
- Proteção de rotas para usuários autenticados

## Como Executar o Projeto

### 1. Clonar o Repositório
```bash
git clone https://github.com/Aegdae/desafio-login.git
cd desafio-login

```

### 2. Criar e Ativar um Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4. Aplicar Migrações do Banco de Dados
```bash
python manage.py migrate
```

### 5. Executar o Servidor
```bash
python manage.py runserver
```
O projeto estará disponível em http://127.0.0.1:8000/.


## 🚀 Estrutura do Projeto
  ```plaintext
    auth_system/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
    static/
        script.js
        style.css
    users/
        migrations/
        templates/
            login.html
            main.html
            register.html
        __init__.py
        admin.py
        apps.py
        backend.py
        forms.py
        models.py
        tests.py
        urls.py
        views.py
    db.sqlite3
    manage.py
    README.md
    requirements.txt
  ```
