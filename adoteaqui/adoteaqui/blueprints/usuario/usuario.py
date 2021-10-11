from flask import Blueprint


bp = Blueprint('usuario', __name__, url_prefix='/usuario', template_folder='templates')


@bp.route('/')
def root():
    return 'Hello from usuario'


def init_app(app):
    app.register_blueprint(bp)