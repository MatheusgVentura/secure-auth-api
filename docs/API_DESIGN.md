# Design Inicial da API

Este documento descreve os endpoints planejados para a primeira versao da API. A ideia e servir como guia antes da implementacao e ser atualizado conforme o projeto evoluir.

## Padrao geral

Base URL planejada:

```txt
/api/v1/
```

Formato principal:

```txt
Content-Type: application/json
```

Autenticacao:

```txt
Authorization: Bearer <access_token>
```

## Endpoints publicos

### Health check

```http
GET /api/v1/health/
```

Verifica se a API esta online.

Resposta esperada:

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

Corpo da requisicao:

```json
{
  "username": "matheus",
  "email": "matheus@example.com",
  "password": "SenhaForte123!",
  "password_confirm": "SenhaForte123!"
}
```

Resposta esperada:

```json
{
  "id": 1,
  "username": "matheus",
  "email": "matheus@example.com"
}
```

### Login

```http
POST /api/v1/auth/login/
```

Autentica o usuario e retorna tokens JWT.

Corpo da requisicao:

```json
{
  "email": "matheus@example.com",
  "password": "SenhaForte123!"
}
```

Resposta esperada:

```json
{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}
```

### Refresh token

```http
POST /api/v1/auth/token/refresh/
```

Gera um novo access token a partir de um refresh token valido.

Corpo da requisicao:

```json
{
  "refresh": "jwt_refresh_token"
}
```

Resposta esperada:

```json
{
  "access": "new_jwt_access_token"
}
```

## Endpoints autenticados

### Usuario autenticado

```http
GET /api/v1/users/me/
```

Retorna os dados do usuario autenticado.

Resposta esperada:

```json
{
  "id": 1,
  "username": "matheus",
  "email": "matheus@example.com"
}
```

### Atualizar usuario autenticado

```http
PATCH /api/v1/users/me/
```

Atualiza dados basicos do usuario autenticado.

Corpo da requisicao:

```json
{
  "username": "matheusventura"
}
```

Resposta esperada:

```json
{
  "id": 1,
  "username": "matheusventura",
  "email": "matheus@example.com"
}
```

### Trocar senha

```http
POST /api/v1/auth/change-password/
```

Permite que um usuario autenticado troque a propria senha.

Corpo da requisicao:

```json
{
  "current_password": "SenhaAntiga123!",
  "new_password": "NovaSenha123!",
  "new_password_confirm": "NovaSenha123!"
}
```

Resposta esperada:

```json
{
  "detail": "Senha alterada com sucesso."
}
```

### Logout

```http
POST /api/v1/auth/logout/
```

Invalida o refresh token informado.

Corpo da requisicao:

```json
{
  "refresh": "jwt_refresh_token"
}
```

Resposta esperada:

```json
{
  "detail": "Logout realizado com sucesso."
}
```

## Padrao de erros

Exemplo de erro de validacao:

```json
{
  "errors": {
    "email": ["Este campo e obrigatorio."]
  }
}
```

Exemplo de erro de autenticacao:

```json
{
  "detail": "Credenciais invalidas."
}
```

## Decisoes iniciais

- A primeira versao da API deve priorizar autenticacao e seguranca.
- Os endpoints devem usar JSON.
- Endpoints privados devem exigir JWT no header `Authorization`.
- O projeto deve manter rotas versionadas desde o inicio.
