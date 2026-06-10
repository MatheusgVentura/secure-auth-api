# Guia de Setup Local

Este guia mostra como preparar o ambiente local para desenvolver o MVP da Secure Auth API.

Publico-alvo: pessoa desenvolvedora que clonou o repositorio e quer deixar as dependencias prontas para estudar, implementar e testar o projeto localmente.

## Estado atual

O projeto Django ja existe neste repositorio. Hoje voce consegue:

- Criar o ambiente virtual.
- Instalar as dependencias.
- Criar o arquivo `.env` local a partir do `.env.example`.
- Rodar `manage.py`, migrations, testes Django e servidor local.

## Requisitos

Instale antes de comecar:

- Python 3.12 ou superior.
- Git.
- pip.
- PowerShell, se estiver no Windows.
- Um editor de codigo, como VS Code.

Versao local registrada durante a preparacao inicial:

```txt
Python 3.14.3
```

## Clonar o repositorio

```powershell
git clone <url-do-repositorio>
cd secure-auth-api
```

Se o repositorio ja estiver aberto na sua maquina, siga para a criacao do ambiente virtual.

## Criar e ativar ambiente virtual

Crie o ambiente virtual:

```powershell
python -m venv .venv
```

Ative o ambiente virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

Quando o ambiente estiver ativo, o terminal normalmente mostra `(.venv)` antes do caminho.

Se o PowerShell bloquear a ativacao, libere scripts para o usuario atual:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Depois execute novamente:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Instalar dependencias

Atualize o pip:

```powershell
python -m pip install --upgrade pip
```

Instale as dependencias do projeto:

```powershell
pip install -r requirements.txt
```

Dependencias iniciais:

| Pacote | Uso planejado |
| --- | --- |
| Django | Framework web principal. |
| djangorestframework | Criacao da API REST. |
| djangorestframework-simplejwt | Autenticacao com JWT. |
| python-decouple | Leitura de variaveis de ambiente. |
| dj-database-url | Configuracao do banco via `DATABASE_URL`. |
| django-cors-headers | Configuracao de CORS por ambiente. |

## Configurar variaveis de ambiente

Copie o arquivo de exemplo:

```powershell
Copy-Item .env.example .env
```

O `.env` deve conter valores locais e nao deve ser versionado.

Variaveis iniciais:

| Variavel | Exemplo | Descricao |
| --- | --- | --- |
| `SECRET_KEY` | `change-me-to-a-long-random-secret-key` | Chave secreta do Django. Use um valor forte fora do ambiente local. |
| `DJANGO_DEBUG` | `True` | Ativa detalhes de debug apenas em desenvolvimento. |
| `ALLOWED_HOSTS` | `localhost,127.0.0.1` | Hosts permitidos para atender requisicoes. |
| `DATABASE_URL` | `sqlite:///db.sqlite3` | URL de conexao do banco. |
| `ACCESS_TOKEN_LIFETIME_MINUTES` | `15` | Duracao planejada do access token. |
| `REFRESH_TOKEN_LIFETIME_DAYS` | `7` | Duracao planejada do refresh token. |

## Verificar instalacao

Confira a versao do Python:

```powershell
python --version
```

Confira se as dependencias foram instaladas:

```powershell
pip freeze
```

Rodar migrations:

```powershell
python manage.py migrate
```

Criar superusuario:

```powershell
python manage.py createsuperuser
```

Rodar servidor local:

```powershell
python manage.py runserver
```

Endereco local esperado:

```txt
http://127.0.0.1:8000/
```

Rodar testes:

```powershell
python -m pytest
```

Os testes fazem parte do MVP. A suite inicial valida modelo de usuario, health check, cadastro, login, `/users/me/` e troca de senha.

## Verificar qualidade de codigo

O projeto usa `ruff` para lint e formatacao.

Verifique lint:

```powershell
python -m ruff check .
```

Verifique formatacao:

```powershell
python -m ruff format . --check
```

Formate o codigo:

```powershell
python -m ruff format .
```

## Manutencao de dependencias

O `requirements.txt` usa intervalos de versao para permitir atualizacoes compativeis no inicio do projeto.

Use o comando abaixo apenas quando quiser congelar exatamente as versoes do ambiente atual:

```powershell
pip freeze > requirements.txt
```

Antes de alterar o arquivo, confira se isso e mesmo desejado para a fase atual do projeto.

## Solucao de problemas

### `python` nao e reconhecido

Verifique se o Python esta instalado e adicionado ao `PATH`. No Windows, tambem pode ser necessario fechar e abrir o terminal novamente depois da instalacao.

### Ativacao da `.venv` bloqueada

Execute:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Depois tente ativar o ambiente novamente.

### `pip install` falha

Atualize o pip e tente novamente:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Proximos ajustes neste guia

- Adicionar instrucoes para Swagger/OpenAPI.
- Adicionar instrucoes de Docker.
- Adicionar instrucoes para banco de dados de producao.
