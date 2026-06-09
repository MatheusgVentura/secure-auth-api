# Guia de Setup Local

Este documento descreve como preparar o ambiente local para desenvolver a API. Ele sera atualizado conforme o projeto Django for criado e novas dependencias forem adicionadas.

## Requisitos

Antes de iniciar, tenha instalado:

- Python 3.12 ou superior
- Git
- pip
- Um editor de codigo, como VS Code

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

Quando o arquivo `requirements.txt` existir, instale as dependencias com:

```powershell
pip install -r requirements.txt
```

Enquanto o projeto ainda estiver no inicio, as dependencias previstas sao:

```powershell
pip install django djangorestframework djangorestframework-simplejwt python-decouple
```

## Criar arquivo de variaveis de ambiente

O projeto deve usar um arquivo `.env` para configuracoes locais sensiveis.

Exemplo planejado:

```env
SECRET_KEY=change-me
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

Importante:

- O arquivo `.env` nao deve ser enviado para o Git.
- O projeto deve ter um `.env.example` com valores ficticios.

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

Rodar testes:

```powershell
python manage.py test
```

## Proximos ajustes neste guia

- Atualizar comandos depois que o projeto Django for criado.
- Adicionar instrucoes de Docker.
- Adicionar instrucoes para Swagger/OpenAPI.
- Adicionar instrucoes para banco de dados de producao.
