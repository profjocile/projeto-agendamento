from flask import Blueprint

bp = Blueprint("agendamentos", __name__)

@bp.route("/")
def index():
    return "Barbearia: agendamentos (em construção)"