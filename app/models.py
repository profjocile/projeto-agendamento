from datetime import datetime

from flask_login import UserMixin

from .extensions import db, login_manager


class Usuario(UserMixin, db.Model):
    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefone = db.Column(db.String(20))
    senha_hash = db.Column(db.String(255), nullable=False)
    perfil = db.Column(db.String(20), nullable=False, default="cliente")


class Servico(db.Model):
    __tablename__ = "servico"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.String(255))
    duracao_min = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Numeric(8, 2), nullable=False)
    ativo = db.Column(db.Boolean, nullable=False, default=True)


class HorarioTrabalho(db.Model):
    __tablename__ = "horario_trabalho"

    id = db.Column(db.Integer, primary_key=True)
    barbeiro_id = db.Column(db.ForeignKey("usuario.id"), nullable=False)
    dia_semana = db.Column(db.Integer, nullable=False)  # 0 = segunda
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_fim = db.Column(db.Time, nullable=False)


class Bloqueio(db.Model):
    __tablename__ = "bloqueio"

    id = db.Column(db.Integer, primary_key=True)
    barbeiro_id = db.Column(db.ForeignKey("usuario.id"), nullable=False)
    inicio = db.Column(db.DateTime, nullable=False)
    fim = db.Column(db.DateTime, nullable=False)
    motivo = db.Column(db.String(100))


class Agendamento(db.Model):
    __tablename__ = "agendamento"

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.ForeignKey("usuario.id"), nullable=False)
    barbeiro_id = db.Column(db.ForeignKey("usuario.id"), nullable=False)
    servico_id = db.Column(db.ForeignKey("servico.id"), nullable=False)
    inicio = db.Column(db.DateTime, nullable=False)
    fim = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="CONFIRMADO")
    observacao = db.Column(db.String(255))
    criado_em = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    cliente = db.relationship("Usuario", foreign_keys=[cliente_id])
    barbeiro = db.relationship("Usuario", foreign_keys=[barbeiro_id])
    servico = db.relationship("Servico")


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Usuario, int(user_id))