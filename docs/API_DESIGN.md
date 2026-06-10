# Design Inicial da API

Este documento e uma referencia dos endpoints planejados para a primeira versao da API. Ele descreve contratos esperados antes da implementacao e deve ser atualizado quando o codigo real for criado.

## Escopo

Incluido neste design:

- Health check.
- Cadastro de usuario.
- Login com JWT.
- Refresh de access token.
- Logout.
- Dados do usuario autenticado.
- Atualizacao basica do usuario autenticado.
- Troca de senha.

Fora deste design inicial:

- Recuperacao de senha.
- Verificacao de email.
- Login social.
- Administracao de usuarios por painel ou API.

## Padroes gerais

Base URL planejada:

```txt
/api/v1/
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
| `POST` | `/api/v1/auth/logout/` | Privado | Invalidar refresh token. |
| `GET` | `/api/v1/users/me/` | Privado | Consultar o usuario autenticado. |
| `PATCH` | `/api/v1/users/me/` | Privado | Atualizar dados basicos do usuario autenticado. |
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

### Atualizar usuario autenticado

```http
PATCH /api/v1/users/me/
```

Atualiza dados basicos do usuario autenticado.

Requisicao:

```json
{
  "username": "matheusventura"
}
```

Resposta `200 OK`:

```json
{
  "id": 1,
  "username": "matheusventura",
  "email": "matheus@example.com"
}
```

Regras planejadas:

- A primeira versao deve permitir apenas campos explicitamente liberados.
- Alteracao de email deve ser avaliada separadamente, porque pode exigir verificacao.
- Alteracao de senha deve ocorrer somente no endpoint de troca de senha.

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

Erro de validacao `400 Bad Request`:

```json
{
  "errors": {
    "email": ["Este campo e obrigatorio."]
  }
}
```

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
- Priorizar autenticacao e seguranca na primeira versao.
- Usar JSON em todos os endpoints.
- Exigir JWT no header `Authorization` para endpoints privados.
- Nao expor dados sensiveis em respostas ou mensagens de erro.
