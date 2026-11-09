# Visão geral

## 1. Objetivo

Sistema web para agendamento de horários em uma barbearia, permitindo que clientes marquem, cancelem e remarquem atendimentos, e que barbeiros e administradores gerenciem a agenda.

## 2. Problema atual

- Agendamentos feitos por caderno, WhatsApp ou presencialmente.
- Conflitos de horário e esquecimentos.
- Clientes sem visibilidade de horários livres.
- Pouco controle sobre faltas e histórico de atendimentos.

## 3. Solução proposta

Aplicação web responsiva (uso majoritário pelo celular) em Flask, com banco SQLite, onde o cliente vê horários livres em tempo real e o sistema impede automaticamente conflitos.

## 4. Atores

| Ator | Descrição | Principais ações |
|---|---|---|
| **Cliente** | Pessoa que agenda atendimentos | Cadastrar-se, agendar, cancelar, remarcar, ver histórico |
| **Barbeiro** | Profissional que atende | Ver agenda diária/semanal, bloquear horários |
| **Administrador** | Dono ou gerente | Gerenciar serviços, barbeiros, horários de trabalho e relatórios |

## 5. Escopo do MVP

**Dentro do escopo**
- Cadastro e login de clientes
- Catálogo de serviços (nome, duração, preço)
- Agendamento com escolha de serviço, barbeiro, data e horário
- Cancelamento de agendamento pelo cliente
- Agenda do barbeiro
- Gestão básica de serviços e barbeiros pelo admin

**Fora do escopo (por enquanto)**
- Pagamento online
- Programa de fidelidade
- Integração com WhatsApp e Google Calendar
- Aplicativo móvel nativo
- Múltiplas unidades da barbearia

## 6. Premissas e restrições

- Uma única barbearia, poucos acessos simultâneos (justifica o uso de SQLite).
- Horário de funcionamento definido por barbeiro.
- A troca futura de banco (PostgreSQL/MySQL) deve ser simples via SQLAlchemy.

## 7. Glossário

| Termo | Definição |
|---|---|
| **Agendamento** | Reserva de um serviço com um barbeiro em data e hora específicas |
| **Serviço** | Atendimento oferecido (corte, barba etc.) com duração e preço |
| **Horário disponível** | Intervalo livre dentro do expediente do barbeiro, sem conflito e sem bloqueio |
| **Bloqueio** | Período em que o barbeiro não atende (almoço, folga) |
| **Falta** | Cliente não compareceu ao agendamento confirmado |
