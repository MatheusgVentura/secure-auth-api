# Requisitos de Seguranca

Este documento lista os cuidados de seguranca planejados para a API. Ele serve como checklist tecnico e tambem como evidencia de boas praticas para o portfolio.

## Autenticacao

- Senhas devem ser armazenadas usando o sistema de hash do Django.
- A API deve usar JWT para autenticacao.
- Access tokens devem ter tempo de vida curto.
- Refresh tokens devem ter tempo de vida maior que access tokens.
- Logout deve invalidar o refresh token quando a blacklist estiver configurada.
- Endpoints autenticados devem exigir o header `Authorization: Bearer <token>`.

## Senhas

- Senhas fracas devem ser rejeitadas.
- A senha deve ter tamanho minimo configurado.
- A senha nao deve ser semelhante aos dados do usuario.
- A senha nao deve ser inteiramente numerica.
- A confirmacao de senha deve ser validada em cadastro e troca de senha.

## Permissoes

- Dados do usuario autenticado so devem ser acessados pelo proprio usuario.
- Endpoints privados devem usar permissoes explicitas.
- Endpoints publicos devem ser limitados ao necessario, como cadastro, login e health check.

## Protecao contra abuso

- Login deve ter rate limiting/throttling.
- Cadastro deve ter rate limiting/throttling.
- Refresh token deve ter rate limiting/throttling.
- Tentativas repetidas de login devem ser tratadas com cuidado para reduzir brute force.

## Configuracao

- Segredos devem ficar em variaveis de ambiente.
- O arquivo `.env` nao deve ser versionado.
- O projeto deve incluir um `.env.example` sem valores sensiveis.
- `DEBUG` deve ser desativado em producao.
- `ALLOWED_HOSTS` deve ser configurado por ambiente.
- Configuracoes de CORS devem ser restritas aos dominios permitidos.

## Respostas e mensagens

- Mensagens de erro de login nao devem revelar se o email existe.
- Erros devem ser claros para o cliente, mas sem expor detalhes internos.
- Tracebacks nao devem ser exibidos em producao.

## Banco de dados

- Migrations devem ser versionadas.
- Dados sensiveis nao devem aparecer em fixtures publicas.
- O projeto deve evitar logs com senhas, tokens ou dados sensiveis.

## Testes de seguranca planejados

- Cadastro rejeita senha fraca.
- Login rejeita credenciais invalidas.
- Usuario nao autenticado nao acessa endpoints privados.
- Usuario autenticado acessa apenas os proprios dados.
- Refresh token invalido nao gera novo access token.
- Logout invalida o refresh token quando blacklist estiver ativa.
