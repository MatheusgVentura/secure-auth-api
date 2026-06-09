# Roadmap do Projeto

Este documento organiza a evolucao do projeto em fases pequenas, para facilitar a implementacao, os testes e a apresentacao no portfolio.

## Fase 1 - Setup inicial

- [ ] Criar ambiente virtual Python
- [ ] Instalar Django
- [ ] Instalar Django REST Framework
- [ ] Criar projeto Django
- [ ] Criar app principal de usuarios/autenticacao
- [ ] Configurar variaveis de ambiente
- [ ] Configurar banco de dados inicial
- [x] Criar arquivo `.env.example`
- [x] Criar arquivo `.gitignore`

## Fase 2 - Base da API

- [ ] Configurar rotas principais da API
- [ ] Configurar versionamento inicial, como `/api/v1/`
- [ ] Criar endpoint de health check
- [ ] Padronizar respostas de sucesso e erro
- [ ] Configurar serializadores iniciais

## Fase 3 - Autenticacao

- [ ] Criar cadastro de usuario
- [ ] Criar login com JWT
- [ ] Criar refresh token
- [ ] Criar endpoint para dados do usuario autenticado
- [ ] Criar logout com blacklist de refresh token
- [ ] Criar troca de senha para usuario autenticado

## Fase 4 - Seguranca

- [ ] Validar senha forte
- [ ] Configurar permissoes por usuario autenticado
- [ ] Configurar CORS
- [ ] Configurar rate limiting/throttling
- [ ] Proteger endpoints sensiveis contra brute force
- [ ] Remover segredos do codigo-fonte
- [ ] Configurar ambiente de desenvolvimento e producao separadamente

## Fase 5 - Qualidade

- [ ] Criar testes automatizados para cadastro
- [ ] Criar testes automatizados para login
- [ ] Criar testes automatizados para refresh token
- [ ] Criar testes automatizados para permissoes
- [ ] Configurar cobertura de testes
- [ ] Configurar lint/formatacao

## Fase 6 - Documentacao e portfolio

- [ ] Adicionar Swagger/OpenAPI
- [ ] Documentar instalacao local
- [ ] Documentar variaveis de ambiente
- [ ] Documentar exemplos de requisicao e resposta
- [ ] Adicionar prints ou exemplos de uso no README
- [ ] Preparar descricao final do projeto para portfolio

## Fase 7 - Deploy

- [ ] Configurar Docker
- [ ] Criar `docker-compose.yml`
- [ ] Configurar banco de dados para ambiente de deploy
- [ ] Configurar variaveis de ambiente no deploy
- [ ] Publicar API em uma plataforma de hospedagem
- [ ] Validar endpoints em ambiente publico
