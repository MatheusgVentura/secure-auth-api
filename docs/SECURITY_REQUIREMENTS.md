# Requisitos de Seguranca

Este documento lista requisitos de seguranca planejados para o MVP da API. Ele funciona como checklist tecnico para implementacao, revisao e apresentacao do projeto no GitHub.

## Principios

- Seguranca deve ser considerada desde o design da funcionalidade.
- Dados sensiveis nao devem ser expostos em respostas, logs, fixtures ou mensagens de erro.
- Endpoints privados devem negar acesso por padrao.
- Configuracoes devem variar por ambiente e nao ficar fixas no codigo-fonte.
- Testes automatizados basicos devem cobrir os fluxos sensiveis do MVP.

## Checklist por area

### Autenticacao

| Requisito | Obrigatorio | Evidencia esperada |
| --- | --- | --- |
| Usar JWT para autenticacao da API. | Sim | Configuracao do Simple JWT e endpoints de token. |
| Exigir `Authorization: Bearer <token>` em endpoints privados. | Sim | Testes de acesso autenticado e nao autenticado. |
| Access token ter vida curta. | Sim | Configuracao por `ACCESS_TOKEN_LIFETIME_MINUTES`. |
| Refresh token ter vida maior que access token. | Sim | Configuracao por `REFRESH_TOKEN_LIFETIME_DAYS`. |
| Logout invalidar refresh token. | Sim | Blacklist configurada e teste de logout. |
| Login nao revelar se o email existe. | Sim | Mensagem generica para credenciais invalidas. |

### Senhas

| Requisito | Obrigatorio | Evidencia esperada |
| --- | --- | --- |
| Armazenar senhas com hash do Django. | Sim | Uso de `set_password` ou fluxo nativo equivalente. |
| Rejeitar senhas fracas. | Sim | Validadores de senha configurados e testados. |
| Exigir confirmacao em cadastro. | Sim | Validacao de `password_confirm`. |
| Exigir confirmacao em troca de senha. | Sim | Validacao de `new_password_confirm`. |
| Validar senha atual antes da troca. | Sim | Teste para senha atual invalida. |
| Nunca retornar senha ou hash em serializers. | Sim | Campos sensiveis ausentes nas respostas. |

### Permissoes

| Requisito | Obrigatorio | Evidencia esperada |
| --- | --- | --- |
| Usuario acessa apenas os proprios dados. | Sim | Testes de isolamento por usuario. |
| Endpoints privados usam permissoes explicitas. | Sim | Classes de permissao configuradas nas views. |
| Endpoints publicos sao limitados ao necessario. | Sim | Apenas cadastro, login, refresh e health check sem JWT. |
| Dados administrativos nao aparecem em `/users/me/`. | Sim | Serializer publico sem `is_staff` e `is_superuser`. |

### Protecao contra abuso

| Requisito | Obrigatorio | Evidencia esperada |
| --- | --- | --- |
| Login com throttling/rate limiting. | Sim | Scope especifico para login. |
| Cadastro com throttling/rate limiting. | Sim | Scope especifico para cadastro. |
| Refresh token com throttling/rate limiting. | Sim | Scope especifico para refresh. |
| Tentativas repetidas de login tratadas com cuidado. | Sim | Testes ou configuracao de throttling. |

### Configuracao

| Requisito | Obrigatorio | Evidencia esperada |
| --- | --- | --- |
| Segredos em variaveis de ambiente. | Sim | Uso de `.env` local e `.env.example` ficticio. |
| `.env` fora do Git. | Sim | Regra no `.gitignore`. |
| `DEBUG=False` em producao. | Sim | Configuracao por ambiente. |
| `ALLOWED_HOSTS` configurado por ambiente. | Sim | Leitura por variavel de ambiente. |
| CORS restrito aos dominios permitidos. | Sim | Configuracao sem liberar origem ampla em producao. |

### Respostas e logs

| Requisito | Obrigatorio | Evidencia esperada |
| --- | --- | --- |
| Erros claros sem detalhes internos. | Sim | Padrao de resposta documentado e testado. |
| Tracebacks ocultos em producao. | Sim | `DEBUG=False` em producao. |
| Senhas e tokens fora dos logs. | Sim | Revisao de logs e excecoes. |
| Mensagens de login genericas. | Sim | Login invalido retorna resposta uniforme. |

### Banco de dados

| Requisito | Obrigatorio | Evidencia esperada |
| --- | --- | --- |
| Migrations versionadas. | Sim | Arquivos de migration no Git. |
| Dados sensiveis fora de fixtures publicas. | Sim | Fixtures revisadas antes de commit. |
| Email unico no usuario. | Sim | Constraint no modelo e teste. |
| Dados minimos armazenados. | Sim | Modelo inicial pequeno. |

## Variaveis de ambiente relacionadas

| Variavel | Papel |
| --- | --- |
| `SECRET_KEY` | Chave secreta do Django. Deve ser forte fora do ambiente local. |
| `DEBUG` | Deve ser `False` em producao. |
| `ALLOWED_HOSTS` | Define hosts aceitos pela aplicacao. |
| `DATABASE_URL` | Define conexao com banco por ambiente. |
| `ACCESS_TOKEN_LIFETIME_MINUTES` | Controla duracao do access token. |
| `REFRESH_TOKEN_LIFETIME_DAYS` | Controla duracao do refresh token. |

## Testes de seguranca planejados

- Cadastro rejeita senha fraca.
- Cadastro rejeita confirmacao de senha diferente.
- Login rejeita credenciais invalidas com mensagem generica.
- Usuario nao autenticado nao acessa endpoints privados.
- Usuario autenticado acessa apenas os proprios dados.
- Refresh token invalido nao gera novo access token.
- Logout invalida o refresh token quando blacklist estiver ativa.
- Troca de senha exige senha atual correta.
- Respostas publicas nao incluem senha, hash ou campos sensiveis.

## Criterios de pronto

Uma funcionalidade sensivel so deve ser considerada pronta quando:

- O comportamento esperado estiver implementado.
- O caso de sucesso tiver teste automatizado.
- Pelo menos um caso de erro relevante tiver teste automatizado.
- A documentacao de endpoint estiver atualizada.
- Nenhum segredo ou dado sensivel tiver sido adicionado ao repositorio.

## Fora do MVP

Os itens abaixo podem melhorar o projeto, mas nao devem bloquear a primeira versao:

- Recuperacao de senha por email.
- Verificacao de email.
- Login social.
- Permissoes complexas.
- Auditoria avancada.
- Deploy publico.
