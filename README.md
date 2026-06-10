# Django Secure Auth API

API REST de autenticacao segura em desenvolvimento, criada para praticar desenvolvimento backend com **Python**, **Django**, **Django REST Framework** e **JWT**.

O foco do projeto e construir uma base pequena, testavel e bem documentada para cadastro, login, refresh token, logout e acesso aos dados do usuario autenticado.

## Status do projeto

Este repositorio esta na fase inicial de preparacao. No momento, existem os arquivos de configuracao e planejamento, mas o projeto Django ainda nao foi criado.

Itens ja presentes:

- `requirements.txt` com dependencias iniciais.
- `.env.example` com variaveis locais esperadas.
- `.gitignore` para arquivos sensiveis e artefatos locais.
- Documentacao inicial em `docs/`.

Consulte o [roadmap](docs/ROADMAP.md) para acompanhar o que ja foi feito e o que ainda sera implementado.

## Objetivos

- Praticar criacao de APIs REST com Django REST Framework.
- Implementar autenticacao baseada em email e senha.
- Usar JWT com access token e refresh token.
- Aplicar boas praticas de seguranca desde o inicio.
- Manter documentacao clara o suficiente para estudo, manutencao e portfolio.

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

O projeto Django ainda sera criado. Quando isso acontecer, o guia de setup sera atualizado com os comandos para migrations, superusuario, testes e servidor local.

Leia o [guia de setup local](docs/SETUP_GUIDE.md) para instrucoes completas.

## Documentacao

| Documento | Tipo | Quando usar |
| --- | --- | --- |
| [Guia de setup local](docs/SETUP_GUIDE.md) | How-to | Para preparar o ambiente de desenvolvimento. |
| [Design inicial da API](docs/API_DESIGN.md) | Referencia | Para consultar endpoints, payloads e padroes de resposta planejados. |
| [Modelo de dados](docs/DATABASE_MODEL.md) | Referencia | Para entender o modelo de usuario planejado. |
| [Requisitos de seguranca](docs/SECURITY_REQUIREMENTS.md) | Referencia/checklist | Para validar decisoes de autenticacao, permissao e configuracao. |
| [Roadmap do projeto](docs/ROADMAP.md) | Planejamento | Para acompanhar as fases de implementacao. |

## Escopo inicial

Incluido na primeira versao planejada:

- Cadastro de usuario.
- Login com JWT.
- Refresh de access token.
- Logout com blacklist de refresh token.
- Endpoint para usuario autenticado.
- Troca de senha.
- Health check.
- Testes automatizados dos fluxos principais.

Fora do escopo inicial:

- Recuperacao de senha por email.
- Verificacao de email.
- Login social.
- Perfil publico completo.
- Painel administrativo customizado.

## Seguranca

Este projeto trata seguranca como requisito central, nao como ajuste final. As decisoes planejadas incluem:

- Senhas armazenadas com os mecanismos nativos do Django.
- Segredos carregados por variaveis de ambiente.
- `DEBUG=False` em producao.
- CORS restrito por ambiente.
- Rate limiting em endpoints sensiveis.
- Mensagens de erro que nao revelem informacoes desnecessarias.

Veja a lista completa em [requisitos de seguranca](docs/SECURITY_REQUIREMENTS.md).
