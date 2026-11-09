from flask import Flask

from config import Config

from .extensions import db, login_manager, migrate


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from . import models  # noqa: F401  (registra as tabelas para o Migrate)
    from .agendamentos.routes import bp as agend_bp
    from .auth.routes import bp as auth_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(agend_bp)

    return app