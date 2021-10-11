from flask import Blueprint, render_template
from .entidades import Usuario

bp = Blueprint('usuario', __name__, url_prefix='/usuario', template_folder='templates')


@bp.route('/')
def root():
    return 'Hello from usuario'

@bp.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


@bp.route('/login')
def login():
    return render_template('login.html')

def init_app(app):
    app.register_blueprint(bp)