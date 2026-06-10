# Modelo de Dados

Este documento e uma referencia das decisoes iniciais sobre os modelos de dados da API. Ele deve ser atualizado quando os models reais forem criados ou alterados.

## Decisao principal

O projeto deve usar um modelo de usuario customizado desde o inicio.

Modelo planejado:

```txt
accounts.User
```

Motivos:

- Permite usar email como identificador principal de autenticacao.
- Evita migracoes complexas caso o projeto precise customizar usuarios no futuro.
- Mantem campos de perfil sob controle do projeto.
- Demonstra uma pratica importante em projetos Django com autenticacao propria.

## Usuario

Modelo planejado:

```txt
User
```

Tabela planejada:

```txt
accounts_user
```

Campos iniciais:

| Campo | Tipo | Obrigatorio | Regra/observacao |
| --- | --- | --- | --- |
| `id` | `BigAutoField` | Sim | Identificador unico. |
| `email` | `EmailField` | Sim | Deve ser unico e normalizado. |
| `username` | `CharField` | Sim | Nome publico ou apelido. |
| `password` | `CharField` | Sim | Gerenciado pelos mecanismos nativos do Django. |
| `is_active` | `BooleanField` | Sim | Indica se a conta pode autenticar. |
| `is_staff` | `BooleanField` | Sim | Permite acesso ao Django admin. |
| `is_superuser` | `BooleanField` | Sim | Permissoes administrativas globais. |
| `date_joined` | `DateTimeField` | Sim | Data de criacao da conta. |
| `last_login` | `DateTimeField` | Nao | Ultimo login registrado. |

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

## Regras de dados

### Email

- Deve ser obrigatorio.
- Deve ser unico.
- Deve ser normalizado antes de salvar.
- Deve ser usado como identificador principal de login.

### Username

- Deve ser obrigatorio na primeira versao.
- Pode ser unico ou apenas validado para exibicao; essa decisao deve ser confirmada na implementacao.
- Nao deve substituir o email como campo de login.

### Senha

- Nao deve ser armazenada em texto puro.
- Deve ser definida com `set_password`.
- Deve ser validada com os validadores configurados no Django.
- Nao deve ser retornada por serializers ou logs.

## Manager customizado

Como o projeto usara email como identificador principal, sera necessario criar um manager customizado.

Responsabilidades planejadas:

- Criar usuario comum com email e senha.
- Criar superusuario com permissoes administrativas.
- Normalizar email.
- Validar campos obrigatorios.
- Garantir `is_staff=True` e `is_superuser=True` para superusuarios.

## Relacao com JWT

O JWT deve representar a identidade do usuario cadastrado no banco.

Informacoes planejadas no token:

- Identificador do usuario.
- Tipo do token.
- Data de expiracao.

Informacoes que nao devem ser colocadas no token:

- Senha.
- Hash de senha.
- Dados sensiveis.
- Informacoes extensas de perfil.

## Campos futuros possiveis

Campos que podem ser adicionados depois:

| Campo | Motivo possivel |
| --- | --- |
| `first_name` | Nome real do usuario. |
| `last_name` | Sobrenome do usuario. |
| `phone` | Contato, caso alguma funcionalidade precise. |
| `avatar` | Imagem de perfil. |
| `email_verified` | Controle de verificacao de email. |
| `created_at` | Data tecnica de criacao. |
| `updated_at` | Data tecnica da ultima atualizacao. |

Esses campos nao entram necessariamente na primeira versao. A prioridade inicial e manter o modelo pequeno e seguro.

## Modelos futuros possiveis

Conforme o projeto evoluir, podem existir outros modelos:

| Modelo | Objetivo | Criar quando |
| --- | --- | --- |
| `UserProfile` | Guardar dados extras do usuario. | Campos de perfil crescerem alem do usuario base. |
| `LoginAttempt` | Registrar tentativas de login. | Houver necessidade de auditoria ou bloqueio por abuso. |
| `PasswordResetToken` | Controlar recuperacao de senha. | Recuperacao de senha for implementada. |
| `AuditLog` | Registrar eventos sensiveis. | A API precisar de trilha de auditoria. |

Esses modelos devem ser criados apenas quando a funcionalidade correspondente for implementada.

## Criterios de pronto

O modelo de usuario inicial estara pronto quando:

- `AUTH_USER_MODEL` apontar para `accounts.User` antes da primeira migration.
- O login usar `email` como `USERNAME_FIELD`.
- Usuario comum e superusuario puderem ser criados corretamente.
- Senhas forem sempre salvas com hash.
- Testes cobrirem criacao de usuario, criacao de superusuario e unicidade de email.

## Decisoes iniciais

- Usar usuario customizado desde o primeiro commit de codigo Django.
- Usar email como identificador principal de login.
- Manter o modelo inicial pequeno.
- Evitar armazenar dados sensiveis desnecessarios.
- Usar os mecanismos nativos do Django para senha e permissoes.
