# Design Inicial da API

Este documento e uma referencia dos endpoints planejados para o MVP da API. Ele descreve contratos esperados antes da implementacao e deve ser atualizado quando o codigo real for criado.

## Escopo

Incluido no MVP:

- Health check.
- Cadastro de usuario.
- Login com JWT.
- Refresh de access token.
- Logout.
- Recuperacao de senha.
- Dados do usuario autenticado.
- Troca de senha.

Fora do MVP:

- Recuperacao de senha.
- Verificacao de email.
- Login social.
- Frontend.
- Administracao de usuarios por painel ou API.
- Atualizacao de perfil.
- Permissoes complexas.

## Padroes gerais

Base URL planejada:

```txt
/api/v1/
```

Documentacao local:

```txt
/api/docs/
/api/redoc/
/api/schema/
```

Formato de requisicao e resposta:

```txt
Content-Type: application/json
```

Autenticacao para endpoints privados:

```txt
Authorization: Bearer <access_token>
```

Campos de senha nunca devem aparecer em respostas.

## Resumo dos endpoints

| Metodo | Rota | Acesso | Objetivo |
| --- | --- | --- | --- |
| `GET` | `/api/v1/health/` | Publico | Verificar se a API esta online. |
| `POST` | `/api/v1/auth/register/` | Publico | Criar uma conta de usuario. |
| `POST` | `/api/v1/auth/login/` | Publico | Autenticar usuario e emitir tokens. |
| `POST` | `/api/v1/auth/token/refresh/` | Publico | Gerar novo access token. |
| `POST` | `/api/v1/auth/password-reset/` | Publico | Solicitar recuperacao de senha por email. |
| `POST` | `/api/v1/auth/password-reset/confirm/` | Publico | Confirmar recuperacao e definir nova senha. |
| `POST` | `/api/v1/auth/logout/` | Privado | Invalidar refresh token. |
| `GET` | `/api/v1/users/me/` | Privado | Consultar o usuario autenticado. |
| `POST` | `/api/v1/auth/change-password/` | Privado | Trocar a propria senha. |

## Endpoints publicos

### Health check

```http
GET /api/v1/health/
```

Verifica se a API esta online.

Resposta `200 OK`:

```json
{
  "status": "ok"
}
```

### Cadastro de usuario

```http
POST /api/v1/auth/register/
```

Cria uma nova conta de usuario.

Requisicao:

```json
{
  "username": "matheus",
  "email": "matheus@example.com",
  "password": "SenhaForte123!",
  "password_confirm": "SenhaForte123!"
}
```

Resposta `201 Created`:

```json
{
  "id": 1,
  "username": "matheus",
  "email": "matheus@example.com"
}
```

Regras planejadas:

- `email` deve ser unico.
- `email` deve ser normalizado antes de salvar.
- `password` e `password_confirm` devem ser iguais.
- A senha deve passar pelos validadores configurados no Django.
- A resposta nao deve incluir senha, hash de senha ou tokens.

### Login

```http
POST /api/v1/auth/login/
```

Autentica o usuario e retorna tokens JWT.

Requisicao:

```json
{
  "email": "matheus@example.com",
  "password": "SenhaForte123!"
}
```

Resposta `200 OK`:

```json
{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}
```

Regras planejadas:

- A autenticacao deve usar email e senha.
- A mensagem de erro nao deve revelar se o email existe.
- O endpoint deve ter throttling/rate limiting.

### Refresh token

```http
POST /api/v1/auth/token/refresh/
```

Gera um novo access token a partir de um refresh token valido.

Requisicao:

```json
{
  "refresh": "jwt_refresh_token"
}
```

Resposta `200 OK`:

```json
{
  "access": "new_jwt_access_token"
}
```

Regras planejadas:

- Refresh tokens invalidos, expirados ou em blacklist devem ser rejeitados.
- O endpoint deve ter throttling/rate limiting.

### Solicitar recuperacao de senha

```http
POST /api/v1/auth/password-reset/
```

Solicita instrucoes de recuperacao de senha por email.

Requisicao:

```json
{
  "email": "matheus@example.com"
}
```

Resposta `200 OK`:

```json
{
  "detail": "Se o email estiver cadastrado, enviaremos instrucoes para redefinir a senha."
}
```

Regras:

- A resposta deve ser generica para nao revelar se o email existe.
- O email so deve ser enviado para usuarios ativos cadastrados.
- O endpoint deve ter throttling/rate limiting.

### Confirmar recuperacao de senha

```http
POST /api/v1/auth/password-reset/confirm/
```

Redefine a senha usando `uid` e `token` recebidos por email.

Requisicao:

```json
{
  "uid": "uid_recebido",
  "token": "token_recebido",
  "new_password": "NovaSenha123!",
  "new_password_confirm": "NovaSenha123!"
}
```

Resposta `200 OK`:

```json
{
  "detail": "Senha redefinida com sucesso."
}
```

Regras:

- `uid` e `token` devem ser validos.
- `new_password` e `new_password_confirm` devem ser iguais.
- A nova senha deve passar pelos validadores configurados.
- A senha deve ser salva usando os mecanismos nativos do Django.

## Endpoints autenticados

### Usuario autenticado

```http
GET /api/v1/users/me/
```

Retorna os dados do usuario autenticado pelo access token.

Resposta `200 OK`:

```json
{
  "id": 1,
  "username": "matheus",
  "email": "matheus@example.com"
}
```

Regras planejadas:

- O usuario so deve acessar os proprios dados.
- A resposta nao deve incluir campos internos de permissao por padrao.

### Trocar senha

```http
POST /api/v1/auth/change-password/
```

Permite que um usuario autenticado troque a propria senha.

Requisicao:

```json
{
  "current_password": "SenhaAntiga123!",
  "new_password": "NovaSenha123!",
  "new_password_confirm": "NovaSenha123!"
}
```

Resposta `200 OK`:

```json
{
  "detail": "Senha alterada com sucesso."
}
```

Regras planejadas:

- `current_password` deve ser validada antes da troca.
- `new_password` e `new_password_confirm` devem ser iguais.
- A nova senha deve passar pelos validadores configurados.
- A senha deve ser salva usando os mecanismos nativos do Django.

### Logout

```http
POST /api/v1/auth/logout/
```

Invalida o refresh token informado.

Requisicao:

```json
{
  "refresh": "jwt_refresh_token"
}
```

Resposta `200 OK`:

```json
{
  "detail": "Logout realizado com sucesso."
}
```

Regras planejadas:

- O refresh token deve ser adicionado a blacklist quando esse recurso estiver configurado.
- O access token atual continua valido ate expirar, a menos que outra estrategia seja implementada.

## Padrao de erros

Erros de validacao devem retornar os detalhes dentro da chave `errors`.

Erro de validacao `400 Bad Request`:

```json
{
  "errors": {
    "email": ["Este campo e obrigatorio."]
  }
}
```

Erros de autenticacao devem usar mensagem generica para nao revelar se o email existe.

Erro de autenticacao `401 Unauthorized`:

```json
{
  "detail": "Credenciais invalidas."
}
```

Erro de permissao `403 Forbidden`:

```json
{
  "detail": "Voce nao tem permissao para executar esta acao."
}
```

## Decisoes iniciais

- Manter rotas versionadas desde o inicio.
- Priorizar um MVP pequeno, completo e facil de revisar.
- Usar JSON em todos os endpoints.
- Exigir JWT no header `Authorization` para endpoints privados.
- Nao expor dados sensiveis em respostas ou mensagens de erro.
- Deixar atualizacao de perfil, recuperacao de senha e login social para depois do MVP.
