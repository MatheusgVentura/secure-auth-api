# Django Secure Auth API

API REST de autenticacao segura em desenvolvimento, criada como projeto de estudo bem feito para praticar backend e fortalecer portfolio para vaga de estagio.

O foco e entregar primeiro um MVP pequeno, completo e bem documentado com **Python**, **Django**, **Django REST Framework** e **JWT**. Depois disso, o projeto pode evoluir com melhorias incrementais.

## Status do projeto

Este repositorio ja possui a fundacao do projeto Django e os primeiros endpoints do MVP.

Itens ja presentes:

- Projeto Django em `config/` com settings separados para desenvolvimento, teste e producao.
- App `accounts` com usuario customizado usando email como login.
- Django REST Framework configurado com JWT.
- Endpoints iniciais de health check, cadastro, login, refresh, logout, usuario autenticado e troca de senha.
- Testes automatizados iniciais com pytest.
- Documentacao inicial em `docs/`.

Consulte o [roadmap](docs/ROADMAP.md) para acompanhar o MVP e as melhorias futuras.

## Objetivos

- Construir um projeto de estudo bem feito para apresentar no GitHub.
- Praticar fundamentos importantes para uma vaga de estagio backend.
- Praticar criacao de APIs REST com Django REST Framework.
- Implementar autenticacao baseada em email e senha.
- Usar JWT com access token e refresh token.
- Aplicar boas praticas de seguranca desde o inicio.
- Implementar testes automatizados basicos para os fluxos principais.
- Manter documentacao clara o suficiente para estudo, revisao e portfolio.

## Tecnologias planejadas

- Python 3.12 ou superior.
- Django 5.2 LTS.
- Django REST Framework.
- Django REST Framework Simple JWT.
- Banco SQL, inicialmente SQLite em desenvolvimento.
- Configuracao por variaveis de ambiente.

## Primeiros passos

Para preparar o ambiente local:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

Depois de instalar as dependencias e criar o `.env`, rode:

```powershell
python manage.py migrate
python -m pytest
python manage.py runserver
```

Com o servidor rodando, acesse:

```txt
http://127.0.0.1:8000/
```

Documentacao interativa da API:

```txt
http://127.0.0.1:8000/api/docs/
```

Leia o [guia de setup local](docs/SETUP_GUIDE.md) para instrucoes completas.

## Documentacao OpenAPI

O projeto disponibiliza documentacao interativa e schema OpenAPI para facilitar testes, revisao e apresentacao da API.

| Recurso | URL local |
| --- | --- |
| Swagger UI | `http://127.0.0.1:8000/api/docs/` |
| ReDoc | `http://127.0.0.1:8000/api/redoc/` |
| Schema OpenAPI | `http://127.0.0.1:8000/api/schema/` |

## Exemplos de uso da API

Os exemplos abaixo usam PowerShell com `Invoke-RestMethod`.

### Health check

```powershell
Invoke-RestMethod http://127.0.0.1:8000/api/v1/health/
```

Resposta esperada:

```json
{
  "status": "ok"
}
```

### Cadastro

```powershell
Invoke-RestMethod `
  -Uri http://127.0.0.1:8000/api/v1/auth/register/ `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"username":"matheus","email":"matheus@example.com","password":"SenhaForte123!","password_confirm":"SenhaForte123!"}'
```

### Login

```powershell
$login = Invoke-RestMethod `
  -Uri http://127.0.0.1:8000/api/v1/auth/login/ `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"email":"matheus@example.com","password":"SenhaForte123!"}'

$access = $login.access
$refresh = $login.refresh
```

### Usuario autenticado

```powershell
Invoke-RestMethod `
  -Uri http://127.0.0.1:8000/api/v1/users/me/ `
  -Headers @{ Authorization = "Bearer $access" }
```

### Refresh token

```powershell
Invoke-RestMethod `
  -Uri http://127.0.0.1:8000/api/v1/auth/token/refresh/ `
  -Method Post `
  -ContentType "application/json" `
  -Body "{`"refresh`":`"$refresh`"}"
```

### Troca de senha

```powershell
Invoke-RestMethod `
  -Uri http://127.0.0.1:8000/api/v1/auth/change-password/ `
  -Method Post `
  -Headers @{ Authorization = "Bearer $access" } `
  -ContentType "application/json" `
  -Body '{"current_password":"SenhaForte123!","new_password":"NovaSenhaForte123!","new_password_confirm":"NovaSenhaForte123!"}'
```

### Logout

```powershell
Invoke-RestMethod `
  -Uri http://127.0.0.1:8000/api/v1/auth/logout/ `
  -Method Post `
  -Headers @{ Authorization = "Bearer $access" } `
  -ContentType "application/json" `
  -Body "{`"refresh`":`"$refresh`"}"
```

## Documentacao

| Documento | Tipo | Quando usar |
| --- | --- | --- |
| [Guia de setup local](docs/SETUP_GUIDE.md) | How-to | Para preparar o ambiente de desenvolvimento. |
| [Design inicial da API](docs/API_DESIGN.md) | Referencia | Para consultar endpoints, payloads e padroes de resposta planejados. |
| [Modelo de dados](docs/DATABASE_MODEL.md) | Referencia | Para entender o modelo de usuario planejado. |
| [Requisitos de seguranca](docs/SECURITY_REQUIREMENTS.md) | Referencia/checklist | Para validar decisoes de autenticacao, permissao e configuracao. |
| [Roadmap do projeto](docs/ROADMAP.md) | Planejamento | Para acompanhar as fases de implementacao. |

## MVP

O MVP deve ser pequeno e completo. A primeira versao planejada inclui exatamente:

1. Setup Django + Django REST Framework.
2. Usuario customizado com email como login.
3. Cadastro de usuario.
4. Login com JWT.
5. Refresh token.
6. Endpoint `/users/me/`.
7. Logout.
8. Troca de senha.
9. Testes basicos dos fluxos principais.
10. README caprichado com instrucoes e exemplos.

## Fora do MVP

- Recuperacao de senha por email.
- Verificacao de email.
- Login social.
- Frontend.
- Perfil publico completo.
- Painel administrativo customizado.
- Permissoes complexas.
- Deploy publico obrigatorio.

Esses itens podem entrar depois que o MVP estiver pronto.

## Testes automatizados

Mesmo sendo um projeto de estudo, os testes fazem parte do MVP. A ideia nao e ter uma suite enorme no inicio, mas cobrir os fluxos que mostram maturidade tecnica:

- Cadastro cria usuario com sucesso.
- Cadastro rejeita senha fraca ou confirmacao diferente.
- Login retorna tokens com credenciais validas.
- Login rejeita credenciais invalidas.
- `/users/me/` exige autenticacao.
- Usuario autenticado consegue ver os proprios dados.
- Troca de senha exige senha atual correta.

## GitHub como vitrine

Neste momento, o projeto foi pensado para ficar bem apresentado no GitHub. Por isso, o README e os documentos em `docs/` devem permitir que outra pessoa entenda o objetivo, o escopo, as decisoes tecnicas e o caminho para rodar localmente.

Deploy publico fica como melhoria futura, depois que o MVP estiver implementado e testado.

## Descricao para portfolio

Secure Auth API e uma API REST de autenticacao criada com Django, Django REST Framework e JWT. O projeto implementa um fluxo completo de autenticacao com usuario customizado baseado em email, cadastro, login, refresh token, logout com blacklist, consulta do usuario autenticado e troca de senha.

O objetivo do projeto e demonstrar fundamentos importantes de backend para uma vaga de estagio: modelagem de usuario customizado, autenticacao segura, separacao de configuracoes por ambiente, uso de variaveis de ambiente, testes automatizados e documentacao clara para execucao local.

Principais destaques tecnicos:

- Usuario customizado com email como identificador principal.
- Autenticacao JWT com access token e refresh token.
- Logout com blacklist de refresh token.
- Endpoints privados protegidos por permissao.
- Validacao de senha com validadores nativos do Django.
- Respostas de erro padronizadas para validacao.
- Settings separados para desenvolvimento, teste e producao.
- Suite de testes com pytest cobrindo os fluxos principais.

## Seguranca

Este projeto trata seguranca como requisito central, nao como ajuste final. As decisoes planejadas incluem:

- Senhas armazenadas com os mecanismos nativos do Django.
- Segredos carregados por variaveis de ambiente.
- `DEBUG=False` em producao.
- CORS restrito por ambiente.
- Rate limiting em endpoints sensiveis.
- Mensagens de erro que nao revelem informacoes desnecessarias.

Veja a lista completa em [requisitos de seguranca](docs/SECURITY_REQUIREMENTS.md).
