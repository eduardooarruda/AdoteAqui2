from flask import Blueprint, render_template
# from .entidades import Usuario
# from ...ext.database import db


bp = Blueprint('usuario', __name__, url_prefix='/usuario', template_folder='templates')


Estados ={
    'Acre':'AC',
    'Alagoas': 'AL',
    'Amapá': 'AP',
    'Amazonas': 'AM',
    'Bahia': 'BA',
    'Ceará': 'CE',
    'Distrito Federal': 'DF',
    'Espírito Santo': 'ES',
    'Goiás': 'GO',
    'Maranhão': 'MA',
    'Mato Grosso do Sul':'MS',
    'Minas Gerais': 'MG',
    'Pará': 'PA',
    'Paraíba': 'PB',
    'Paraná': 'PR',
    'Pernambuco': 'PE',
    'Piauí': 'PI',
    'Rio de Janeiro': 'RJ',
    'Rio Grande do Norte': 'RN',
    'Rio Grande do Sul': 'RS',
    'Rondônia': 'RO',
    'Roraima': 'RR',
    'Santa Catarina': 'SC',
    'São Paulo': 'SP',
    'Sergipe': 'SE',
    'Tocantins': 'TO'
}
# @bp.route('/')
# def root():
#     return 'Hello from usuario'

@bp.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', Estados=Estados)

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/atualizarPerfil')
def atualizarPerfil():
    return render_template('GerenciamentoUsuario.html')

@bp.route('/perfilUsuario')
def perfilUsuario():
    return render_template('paginaUsuario.html')

def init_app(app):
    app.register_blueprint(bp)
