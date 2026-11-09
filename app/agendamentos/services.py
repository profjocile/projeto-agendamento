from ..models import Agendamento

def horario_disponivel(barbeiro_id, inicio, fim):
    conflito = Agendamento.query.filter(
        Agendamento.barbeiro_id == barbeiro_id,
        Agendamento.status.in_(["PENDENTE", "CONFIRMADO"]),
        Agendamento.inicio < fim,
        Agendamento.fim > inicio,
    ).first()
    return conflito is None