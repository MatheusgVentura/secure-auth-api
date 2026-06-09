# Guia de Setup Local

Este documento descreve como preparar o ambiente local para desenvolver a API. Ele sera atualizado conforme o projeto Django for criado e novas dependencias forem adicionadas.

## Requisitos

Antes de iniciar, tenha instalado:

- Python 3.12 ou superior
- Git
- pip
- Um editor de codigo, como VS Code

Versao local usada durante a preparacao do projeto:

```txt
Python 3.14.3
```

## Clonar o repositorio

```bash
git clone <url-do-repositorio>
cd secure-auth-api
```

Se voce ja esta com o repositorio aberto localmente, pode seguir para a criacao do ambiente virtual.

## Criar ambiente virtual

No Windows PowerShell:

```powershell
python -m venv .venv
```

Ativar o ambiente virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativacao, execute:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Depois tente ativar o ambiente novamente.

## Instalar dependencias

Com o ambiente virtual ativado, atualize o pip:

```powershell
python -m pip install --upgrade pip
```

Depois instale as dependencias do projeto:

```powershell
pip install -r requirements.txt
```

Dependencias iniciais:

```txt
Django
Django REST Framework
Django REST Framework Simple JWT
python-decouple
dj-database-url
django-cors-headers
```

O projeto usa Django `5.2.x` LTS como base inicial.

## Criar arquivo de variaveis de ambiente

O projeto deve usar um arquivo `.env` para configuracoes locais sensiveis.

Exemplo planejado:

```env
SECRET_KEY=change-me
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
ACCESS_TOKEN_LIFETIME_MINUTES=15
REFRESH_TOKEN_LIFETIME_DAYS=7
```

Importante:

- O arquivo `.env` nao deve ser enviado para o Git.
- O projeto deve ter um `.env.example` com valores ficticios.

Para criar o arquivo local, copie o exemplo:

```powershell
Copy-Item .env.example .env
```

## Criar projeto Django

Quando formos iniciar a implementacao, o comando planejado sera:

```powershell
django-admin startproject config .
```

Depois, criaremos um app para autenticacao/usuarios:

```powershell
python manage.py startapp accounts
```

## Rodar migrations

Depois que o projeto Django existir:

```powershell
python manage.py migrate
```

## Criar superusuario

```powershell
python manage.py createsuperuser
```

## Rodar servidor local

```powershell
python manage.py runserver
```

Servidor local esperado:

```txt
http://127.0.0.1:8000/
```

## Comandos uteis

Verificar versao do Python:

```powershell
python --version
```

Verificar pacotes instalados:

```powershell
pip freeze
```

Salvar dependencias instaladas:

```powershell
pip freeze > requirements.txt
```

Use esse comando apenas quando a intencao for congelar as versoes exatas instaladas no ambiente local. Para o inicio do projeto, o `requirements.txt` usa intervalos de versao para receber atualizacoes compativeis.

Rodar testes:

```powershell
python manage.py test
```

## Proximos ajustes neste guia

- Atualizar comandos depois que o projeto Django for criado.
- Adicionar instrucoes de Docker.
- Adicionar instrucoes para Swagger/OpenAPI.
- Adicionar instrucoes para banco de dados de producao.
