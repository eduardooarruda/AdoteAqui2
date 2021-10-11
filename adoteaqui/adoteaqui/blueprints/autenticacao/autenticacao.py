from flask import Blueprint


bp = Blueprint('autenticacao', __name__, url_prefix='/autenticacao')


@bp.route('/')
def root():
    return 'Hello from autenticacao'


def init_app(app):
    app.register_blueprint(bp)