# Roadmap do Projeto

Este roadmap organiza a evolucao do projeto em fases pequenas. Ele ajuda a implementar, testar e apresentar a API com clareza.

## Como usar este roadmap

- Marque um item como concluido apenas quando ele estiver implementado, testado quando aplicavel e documentado.
- Se uma decisao mudar durante a implementacao, atualize tambem os documentos relacionados em `docs/`.
- Mantenha as fases pequenas para facilitar revisao e commits.

## Legenda

- `[x]` Concluido.
- `[ ]` Pendente.

## Fase 1 - Setup inicial

Objetivo: deixar o repositorio pronto para receber o projeto Django.

- [ ] Criar ambiente virtual Python.
- [x] Definir dependencias iniciais no `requirements.txt`.
- [x] Criar arquivo `.env.example`.
- [x] Criar arquivo `.gitignore`.
- [x] Documentar setup local inicial.
- [ ] Criar projeto Django com `django-admin startproject config .`.
- [ ] Criar app principal de usuarios/autenticacao.
- [ ] Configurar variaveis de ambiente no Django.
- [ ] Configurar banco de dados inicial.

Criterio de pronto:

- Dependencias instalam sem erro.
- `.env.example` cobre as variaveis usadas pelo projeto.
- `manage.py` existe e o projeto Django inicia localmente.

## Fase 2 - Base da API

Objetivo: criar a estrutura minima da API antes da autenticacao completa.

- [ ] Configurar apps instalados.
- [ ] Configurar Django REST Framework.
- [ ] Configurar rotas principais.
- [ ] Configurar versionamento inicial em `/api/v1/`.
- [ ] Criar endpoint de health check.
- [ ] Padronizar respostas de sucesso e erro.
- [ ] Configurar serializadores iniciais.

Criterio de pronto:

- `GET /api/v1/health/` responde com sucesso.
- Rotas da API ficam abaixo de `/api/v1/`.
- Erros basicos retornam JSON.

## Fase 3 - Modelo de usuario

Objetivo: criar a base de usuarios antes dos endpoints de autenticacao.

- [ ] Criar modelo customizado `accounts.User`.
- [ ] Configurar `AUTH_USER_MODEL`.
- [ ] Usar email como `USERNAME_FIELD`.
- [ ] Criar manager customizado.
- [ ] Criar migrations iniciais.
- [ ] Validar criacao de usuario comum.
- [ ] Validar criacao de superusuario.

Criterio de pronto:

- Usuario comum pode ser criado com email e senha.
- Superusuario pode ser criado pelo comando `createsuperuser`.
- Email e unico e normalizado.
- Senhas sao salvas com hash.

## Fase 4 - Autenticacao

Objetivo: implementar os fluxos principais de autenticacao da API.

- [ ] Criar cadastro de usuario.
- [ ] Criar login com JWT.
- [ ] Criar refresh token.
- [ ] Criar endpoint para dados do usuario autenticado.
- [ ] Criar atualizacao basica do usuario autenticado.
- [ ] Criar logout com blacklist de refresh token.
- [ ] Criar troca de senha para usuario autenticado.

Criterio de pronto:

- Fluxo cadastro -> login -> acesso privado funciona.
- Refresh token gera novo access token valido.
- Logout invalida refresh token quando blacklist estiver ativa.
- Troca de senha exige senha atual correta.

## Fase 5 - Seguranca

Objetivo: reforcar os controles de seguranca dos endpoints e configuracoes.

- [ ] Validar senha forte.
- [ ] Configurar permissoes por usuario autenticado.
- [ ] Configurar CORS.
- [ ] Configurar rate limiting/throttling.
- [ ] Proteger endpoints sensiveis contra brute force.
- [ ] Garantir que segredos nao fiquem no codigo-fonte.
- [ ] Configurar ambientes de desenvolvimento e producao separadamente.
- [ ] Revisar mensagens de erro para nao revelar dados sensiveis.

Criterio de pronto:

- Endpoints privados rejeitam usuarios anonimos.
- Usuario autenticado acessa apenas os proprios dados.
- Login e cadastro possuem limite de uso.
- `DEBUG` pode ser desligado por ambiente.

## Fase 6 - Qualidade

Objetivo: aumentar confianca com testes e ferramentas de manutencao.

- [ ] Criar testes automatizados para cadastro.
- [ ] Criar testes automatizados para login.
- [ ] Criar testes automatizados para refresh token.
- [ ] Criar testes automatizados para logout.
- [ ] Criar testes automatizados para permissoes.
- [ ] Criar testes automatizados para troca de senha.
- [ ] Configurar cobertura de testes.
- [ ] Configurar lint/formatacao.

Criterio de pronto:

- Fluxos principais possuem testes.
- Testes rodam localmente com um comando documentado.
- Regras de seguranca planejadas possuem ao menos testes basicos.

## Fase 7 - Documentacao e portfolio

Objetivo: transformar a API em um projeto facil de entender, executar e demonstrar.

- [ ] Adicionar Swagger/OpenAPI.
- [x] Documentar instalacao local inicial.
- [x] Documentar variaveis de ambiente iniciais.
- [x] Documentar exemplos planejados de requisicao e resposta.
- [x] Documentar modelo de dados planejado.
- [x] Documentar requisitos de seguranca.
- [ ] Atualizar README com comandos reais depois que o Django existir.
- [ ] Adicionar exemplos de uso com `curl` ou cliente HTTP.
- [ ] Preparar descricao final do projeto para portfolio.

Criterio de pronto:

- Uma pessoa consegue entender o objetivo do projeto pelo README.
- Uma pessoa consegue rodar o projeto seguindo o setup.
- Endpoints implementados aparecem na documentacao.

## Fase 8 - Deploy

Objetivo: publicar a API em ambiente acessivel para demonstracao.

- [ ] Configurar Docker.
- [ ] Criar `docker-compose.yml`.
- [ ] Configurar banco de dados para ambiente de deploy.
- [ ] Configurar variaveis de ambiente no deploy.
- [ ] Configurar `ALLOWED_HOSTS` e CORS para o dominio publico.
- [ ] Publicar API em uma plataforma de hospedagem.
- [ ] Validar endpoints em ambiente publico.

Criterio de pronto:

- API responde em ambiente publico.
- Variaveis sensiveis ficam fora do repositorio.
- Health check e endpoints principais foram testados no deploy.
