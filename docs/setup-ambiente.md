# Setup do ambiente

O projeto usa [uv](https://docs.astral.sh/uv/) para gerenciar Python, ambiente virtual e dependências. Não há `requirements.txt`: as dependências ficam em `pyproject.toml` e o `uv.lock` garante versões reproduzíveis.

## Pré-requisitos

- [uv](https://docs.astral.sh/uv/getting-started/installation/) instalado
- Git

O uv instala a versão correta do Python automaticamente (definida em `.python-version`).

## Primeira vez (criando o projeto)

```bash
uv init barbearia && cd barbearia

# Dependências de produção
uv add flask flask-sqlalchemy flask-migrate flask-login flask-wtf python-dotenv

# Dependências de desenvolvimento
uv add --dev pytest
```

## Clonando um projeto existente

```bash
git clone <url-do-repositorio> barbearia
cd barbearia
uv sync                          # cria .venv e instala tudo do uv.lock
cp .env.example .env             # edite o SECRET_KEY
```

## Banco de dados (SQLite + migrações)

```bash
uv run flask --app main db init                    # apenas na primeira vez do projeto
uv run flask --app main db migrate -m "inicial"
uv run flask --app main db upgrade
```

O arquivo do banco é criado em `instance/barbearia.db`.

## Rodando a aplicação

```bash
uv run flask --app main run --debug
```

Disponível em `http://127.0.0.1:5000`. Não é preciso ativar o `.venv`: o `uv run` já usa o ambiente correto.

## Testes

```bash
uv run pytest
```

## Variáveis de ambiente

O Flask carrega o `.env` automaticamente quando `python-dotenv` está instalado.

| Variável | Descrição | Exemplo |
|---|---|---|
| `SECRET_KEY` | Chave de sessão e CSRF (obrigatória em produção) | `gerar-valor-aleatorio` |

Gerar uma chave: `uv run python -c "import secrets; print(secrets.token_hex(32))"`

## Fluxo de migrações

Ao alterar `app/models.py`:

```bash
uv run flask --app main db migrate -m "descrição da mudança"
uv run flask --app main db upgrade
```

Revise o arquivo gerado em `migrations/versions/` antes do `upgrade`.

## Gerenciando dependências

| Ação | Comando |
|---|---|
| Adicionar pacote | `uv add <pacote>` |
| Adicionar pacote de dev | `uv add --dev <pacote>` |
| Remover pacote | `uv remove <pacote>` |
| Atualizar o lock | `uv lock --upgrade` |
| Sincronizar ambiente | `uv sync` |

Sempre faça commit do `pyproject.toml` e do `uv.lock`.

## Problemas comuns

| Sintoma | Solução |
|---|---|
| `No such table` | Rode `uv run flask --app main db upgrade` |
| `Could not locate a Flask application` | Confira se o `main.py` expõe a variável `app` e use `--app main` |
| `ModuleNotFoundError` | Rode `uv sync` |
| Banco corrompido em desenvolvimento | Apague `instance/barbearia.db` e rode `db upgrade` |

## Convenção de commits

Formato: `tipo: descrição (IDs)`

```
feat: cria tela de agendamento (RF03)
fix: corrige conflito de horário no fim do expediente (RF04, RN01)
docs: atualiza regras de negócio
test: adiciona testes de disponibilidade (RF04)
```
