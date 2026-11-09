# Requisitos funcionais

**Prioridade:** Alta = MVP · Média = fase 2 · Baixa = fase 3

| ID | Requisito | Ator | Prioridade | Status |
|---|---|---|---|---|
| RF01 | O cliente deve poder se cadastrar e fazer login | Cliente | Alta | Pendente |
| RF02 | O cliente deve visualizar os serviços com duração e preço | Cliente | Alta | Pendente |
| RF03 | O cliente deve escolher serviço, barbeiro, data e horário disponível | Cliente | Alta | Pendente |
| RF04 | O sistema deve impedir dois agendamentos no mesmo horário para o mesmo barbeiro | Sistema | Alta | Pendente |
| RF05 | O cliente deve poder cancelar seus agendamentos | Cliente | Alta | Pendente |
| RF06 | O barbeiro deve visualizar sua agenda diária e semanal | Barbeiro | Alta | Pendente |
| RF07 | O admin deve gerenciar serviços, barbeiros e horários de trabalho | Admin | Alta | Pendente |
| RF08 | O cliente deve poder remarcar agendamentos | Cliente | Média | Pendente |
| RF09 | O barbeiro/admin deve bloquear horários (folga, almoço) | Barbeiro/Admin | Média | Pendente |
| RF10 | O sistema deve enviar confirmação e lembrete (e-mail ou WhatsApp) | Sistema | Média | Pendente |
| RF11 | O cliente deve consultar seu histórico de atendimentos | Cliente | Baixa | Pendente |
| RF12 | O admin deve visualizar relatórios (atendimentos, faltas, faturamento) | Admin | Baixa | Pendente |

## Histórias de usuário do MVP

### HU-01: Agendar horário (RF03, RF04)
**Como** cliente, **quero** escolher um horário livre com meu barbeiro preferido, **para** não perder tempo esperando na barbearia.

**Critérios de aceite**
- Só aparecem horários livres, respeitando a duração do serviço.
- Após confirmar, o agendamento aparece em "Meus agendamentos".
- Se o horário for ocupado por outra pessoa durante o processo, o cliente recebe mensagem clara e escolhe outro.

### HU-02: Cancelar agendamento (RF05)
**Como** cliente, **quero** cancelar um agendamento, **para** liberar o horário quando não puder comparecer.

**Critérios de aceite**
- O cancelamento só é permitido dentro do prazo definido em RN03.
- O horário volta a ficar disponível imediatamente.

### HU-03: Ver agenda do dia (RF06)
**Como** barbeiro, **quero** ver minha agenda do dia, **para** me organizar para os atendimentos.

**Critérios de aceite**
- Lista ordenada por horário, com cliente, serviço e duração.
- Mostra apenas agendamentos PENDENTE ou CONFIRMADO.

## Requisitos não funcionais

| ID | Requisito |
|---|---|
| RNF01 | Interface responsiva, pensada primeiro para celular |
| RNF02 | Senhas armazenadas com hash (werkzeug/bcrypt) |
| RNF03 | Proteção contra CSRF, XSS e SQL injection |
| RNF04 | Páginas principais carregam em até 2 s em conexão 4G |
| RNF05 | Conformidade com a LGPD (consentimento e exclusão de dados) |
| RNF06 | Backup diário do banco de dados |
| RNF07 | Testes automatizados cobrindo as regras de agendamento |
