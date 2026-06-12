# Documentacao do Secure Auth API

Esta pagina funciona como ponto de entrada para estudar, desenvolver e acompanhar o projeto no Obsidian ou no GitHub.

## Comece por aqui

- [README do projeto](../README.md): visao geral, tecnologias, comandos e exemplos de uso.
- [Guia de setup local](SETUP_GUIDE.md): preparacao e execucao do ambiente de desenvolvimento.
- [Roadmap](ROADMAP.md): progresso do MVP e proximas melhorias.

## Referencia tecnica

- [Design da API](API_DESIGN.md): endpoints, payloads e padroes de resposta.
- [Modelo de dados](DATABASE_MODEL.md): estrutura e regras do usuario customizado.
- [Requisitos de seguranca](SECURITY_REQUIREMENTS.md): controles e cuidados de autenticacao, permissao e configuracao.

## Mapa do projeto

```text
config/          Configuracoes e URLs principais do Django
apps/accounts/   Usuario, autenticacao e endpoints de conta
tests/           Testes automatizados
docs/            Documentacao tecnica e planejamento
```

## Fluxo de trabalho sugerido

1. Consulte o [roadmap](ROADMAP.md) antes de iniciar uma tarefa.
2. Confira o documento tecnico relacionado a mudanca.
3. Implemente a funcionalidade e seus testes.
4. Execute as verificacoes de qualidade descritas no [README](../README.md#qualidade-de-codigo).
5. Atualize a documentacao e o roadmap quando necessario.

## Documentos futuros

Conforme o projeto crescer, esta documentacao pode receber:

- Explicacao do fluxo completo de autenticacao JWT.
- Registros de decisoes arquiteturais (ADRs).
- Guia de deploy em producao.
- Modelo de ameacas da API.
- Guia de contribuicao.
