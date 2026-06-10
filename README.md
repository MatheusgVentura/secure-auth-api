# Django Secure Auth API

API REST de autenticacao segura em desenvolvimento, criada como projeto de estudo bem feito para praticar backend e fortalecer portfolio para vaga de estagio.

O foco e entregar primeiro um MVP pequeno, completo e bem documentado com **Python**, **Django**, **Django REST Framework** e **JWT**. Depois disso, o projeto pode evoluir com melhorias incrementais.

## Status do projeto

Este repositorio esta na fase inicial de preparacao. No momento, existem os arquivos de configuracao e planejamento, mas o projeto Django ainda nao foi criado.

Itens ja presentes:

- `requirements.txt` com dependencias iniciais.
- `.env.example` com variaveis locais esperadas.
- `.gitignore` para arquivos sensiveis e artefatos locais.
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

## Seguranca

Este projeto trata seguranca como requisito central, nao como ajuste final. As decisoes planejadas incluem:

- Senhas armazenadas com os mecanismos nativos do Django.
- Segredos carregados por variaveis de ambiente.
- `DEBUG=False` em producao.
- CORS restrito por ambiente.
- Rate limiting em endpoints sensiveis.
- Mensagens de erro que nao revelem informacoes desnecessarias.

Veja a lista completa em [requisitos de seguranca](docs/SECURITY_REQUIREMENTS.md).
