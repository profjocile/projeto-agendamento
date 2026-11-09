# Setup do ambiente

## Pré-requisitos

- Python 3.11 ou superior
- Git

## Passo a passo

```bash
# 1. Clonar o repositório
git clone <url-do-repositorio> barbearia
cd barbearia

# 2. Criar e ativar o ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Configurar variáveis de ambiente
cp .env.example .env             # edite o SECRET_KEY

# 5. Criar o banco (SQLite) com as migrações
export FLASK_APP=run.py          # Windows: set FLASK_APP=run.py
flask db init                    # apenas na primeira vez do projeto
flask db migrate -m "inicial"
flask db upgrade

# 6. Rodar a aplicação
flask run --debug
```

A aplicação ficará disponível em `http://127.0.0.1:5000`.

## Variáveis de ambiente

| Variável | Descrição | Exemplo |
|---|---|---|
| `SECRET_KEY` | Chave de sessão e CSRF (obrigatória em produção) | `gerar-valor-aleatorio` |
| `FLASK_APP` | Ponto de entrada | `run.py` |

## Fluxo de migrações

Ao alterar `models.py`:

```bash
flask db migrate -m "descrição da mudança"
flask db upgrade
```

Revise sempre o arquivo gerado em `migrations/versions/` antes do `upgrade`.

## Testes

```bash
pytest
```

## Problemas comuns

| Sintoma | Solução |
|---|---|
| `No such table` | Rode `flask db upgrade` |
| `Could not locate a Flask application` | Defina `FLASK_APP=run.py` |
| Banco corrompido em desenvolvimento | Apague `instance/barbearia.db` e rode `flask db upgrade` |

## Convenção de commits

Formato: `tipo: descrição (IDs)`

```
feat: cria tela de agendamento (RF03)
fix: corrige conflito de horário no fim do expediente (RF04, RN01)
docs: atualiza regras de negócio
test: adiciona testes de disponibilidade (RF04)
```
