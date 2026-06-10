# Roadmap do Projeto

Este roadmap organiza a evolucao do projeto em fases pequenas. O objetivo principal e entregar primeiro um MVP de estudo bem feito para GitHub e portfolio de estagio.

## Como usar este roadmap

- Marque um item como concluido apenas quando ele estiver implementado, testado quando aplicavel e documentado.
- Se uma decisao mudar durante a implementacao, atualize tambem os documentos relacionados em `docs/`.
- Mantenha as fases pequenas para facilitar revisao e commits.
- Nao adicione funcionalidades fora do MVP antes de fechar a primeira versao completa.

## Legenda

- `[x]` Concluido.
- `[ ]` Pendente.

## MVP planejado

O MVP deve conter exatamente:

1. Setup Django + Django REST Framework.
2. Usuario customizado com email como login.
3. Cadastro de usuario.
4. Login com JWT.
5. Refresh token.
6. Endpoint `/users/me/`.
7. Logout.
8. Troca de senha.
9. Testes basicos.
10. README caprichado.

## Fase 1 - Setup Django + DRF

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
- [ ] Configurar Django REST Framework.

Criterio de pronto:

- Dependencias instalam sem erro.
- `.env.example` cobre as variaveis usadas pelo projeto.
- `manage.py` existe e o projeto Django inicia localmente.
- Django REST Framework esta instalado e configurado.

## Fase 2 - Base da API

Objetivo: criar a estrutura minima da API antes da autenticacao completa.

- [ ] Configurar apps instalados.
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

Objetivo: criar usuario customizado com email como login antes dos endpoints de autenticacao.

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
- [ ] Criar logout com blacklist de refresh token.
- [ ] Criar troca de senha para usuario autenticado.

Criterio de pronto:

- Fluxo cadastro -> login -> acesso privado funciona.
- Refresh token gera novo access token valido.
- Logout invalida refresh token quando blacklist estiver ativa.
- Troca de senha exige senha atual correta.

## Fase 5 - Seguranca

Objetivo: reforcar os controles de seguranca necessarios para o MVP.

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

Objetivo: adicionar testes automatizados basicos para mostrar maturidade tecnica sem aumentar demais o escopo.

- [ ] Criar testes automatizados para cadastro.
- [ ] Criar testes automatizados para login.
- [ ] Criar testes automatizados para refresh token.
- [ ] Criar testes automatizados para logout.
- [ ] Criar testes automatizados para `/users/me/` autenticado e nao autenticado.
- [ ] Criar testes automatizados para troca de senha.
- [ ] Documentar como rodar os testes.

Criterio de pronto:

- Fluxos principais possuem testes.
- Testes rodam localmente com um comando documentado.
- Casos de sucesso e erro mais importantes estao cobertos.

## Fase 7 - README e portfolio no GitHub

Objetivo: transformar a API em um projeto facil de entender no GitHub, mesmo sem deploy publico.

- [x] Documentar instalacao local inicial.
- [x] Documentar variaveis de ambiente iniciais.
- [x] Documentar exemplos planejados de requisicao e resposta.
- [x] Documentar modelo de dados planejado.
- [x] Documentar requisitos de seguranca.
- [ ] Atualizar README com comandos reais depois que o Django existir.
- [ ] Adicionar exemplos de uso com `curl` ou cliente HTTP depois que os endpoints existirem.
- [ ] Explicar no README que o projeto e um estudo bem feito para estagio.
- [ ] Preparar descricao final do projeto para portfolio.

Criterio de pronto:

- Uma pessoa consegue entender o objetivo do projeto pelo README.
- Uma pessoa consegue rodar o projeto seguindo o setup.
- Endpoints implementados aparecem na documentacao.
- Testes automatizados sao citados no README.

## Depois do MVP - Melhorias futuras

Objetivo: evoluir o projeto apenas depois que a primeira versao pequena estiver pronta.

- [ ] Adicionar Swagger/OpenAPI.
- [ ] Configurar lint/formatacao.
- [ ] Configurar cobertura de testes.
- [ ] Configurar Docker.
- [ ] Criar `docker-compose.yml`.
- [ ] Implementar recuperacao de senha por email.
- [ ] Implementar verificacao de email.
- [ ] Avaliar atualizacao de perfil.
- [ ] Avaliar login social.
- [ ] Avaliar frontend.

## Depois do MVP - Deploy publico

Objetivo: publicar a API em ambiente acessivel para demonstracao, se isso fizer sentido depois da versao GitHub estar pronta.

- [ ] Configurar banco de dados para ambiente de deploy.
- [ ] Configurar variaveis de ambiente no deploy.
- [ ] Configurar `ALLOWED_HOSTS` e CORS para o dominio publico.
- [ ] Publicar API em uma plataforma de hospedagem.
- [ ] Validar endpoints em ambiente publico.

Criterio de pronto:

- API responde em ambiente publico.
- Variaveis sensiveis ficam fora do repositorio.
- Health check e endpoints principais foram testados no deploy.
