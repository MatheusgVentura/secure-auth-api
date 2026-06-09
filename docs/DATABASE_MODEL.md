# Modelo de Dados

Este documento descreve as decisoes iniciais sobre os modelos de dados da API. Ele deve ser atualizado conforme novos recursos forem implementados.

## Decisao principal

O projeto deve usar um modelo de usuario customizado desde o inicio.

Modelo planejado:

```txt
accounts.User
```

Motivos:

- Facilita usar email como campo principal de autenticacao.
- Evita migracoes complexas caso o projeto precise customizar usuarios no futuro.
- Permite adicionar campos de perfil de forma controlada.
- Demonstra uma pratica importante em projetos Django com autenticacao propria.

## Usuario

Modelo planejado:

```txt
User
```

Campos iniciais:

| Campo | Tipo | Obrigatorio | Observacao |
| --- | --- | --- | --- |
| id | BigAutoField | Sim | Identificador unico |
| email | EmailField | Sim | Deve ser unico |
| username | CharField | Sim | Nome publico ou apelido |
| password | CharField | Sim | Gerenciado pelo Django |
| is_active | BooleanField | Sim | Indica se a conta esta ativa |
| is_staff | BooleanField | Sim | Permite acesso ao admin |
| is_superuser | BooleanField | Sim | Permissoes administrativas |
| date_joined | DateTimeField | Sim | Data de criacao da conta |
| last_login | DateTimeField | Nao | Ultimo login registrado |

## Campo principal de login

Campo principal planejado:

```txt
email
```

Isso significa que o usuario devera fazer login com email e senha, nao com username e senha.

Configuracao esperada no modelo:

```python
USERNAME_FIELD = "email"
REQUIRED_FIELDS = ["username"]
```

## Regras de unicidade

- `email` deve ser unico.
- `username` pode ser unico na primeira versao ou apenas validado para exibicao.
- Emails devem ser normalizados antes de salvar.

## Tabela de usuarios

Nome planejado da tabela:

```txt
accounts_user
```

## Manager customizado

Como o projeto usara email como identificador principal, sera necessario criar um manager customizado.

Responsabilidades planejadas:

- Criar usuario comum com email e senha.
- Criar superusuario com permissoes administrativas.
- Normalizar email.
- Validar campos obrigatorios.

## Relacao com JWT

O JWT deve representar a identidade do usuario cadastrado no banco.

Informacoes planejadas no token:

- Identificador do usuario
- Tipo do token
- Data de expiracao

Informacoes que nao devem ser colocadas no token:

- Senha
- Dados sensiveis
- Informacoes extensas de perfil

## Possiveis campos futuros

Campos que podem ser adicionados depois:

- `first_name`
- `last_name`
- `phone`
- `avatar`
- `email_verified`
- `created_at`
- `updated_at`

Esses campos nao entram necessariamente na primeira versao. A prioridade inicial e manter o modelo simples e seguro.

## Modelos futuros possiveis

Conforme o projeto evoluir, podem existir outros modelos:

| Modelo | Objetivo |
| --- | --- |
| UserProfile | Guardar dados extras do usuario |
| LoginAttempt | Registrar tentativas de login |
| PasswordResetToken | Controlar recuperacao de senha |
| AuditLog | Registrar eventos sensiveis |

Esses modelos devem ser criados apenas quando a funcionalidade correspondente for implementada.

## Decisoes iniciais

- Usar `CustomUser` desde o primeiro commit de codigo Django.
- Usar email como identificador principal de login.
- Manter o modelo inicial pequeno.
- Evitar armazenar dados sensiveis desnecessarios.
- Usar os mecanismos nativos do Django para senha e permissoes.
