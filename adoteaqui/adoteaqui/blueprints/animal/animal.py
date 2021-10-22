from flask import Blueprint, render_template


bp = Blueprint('animal', __name__, url_prefix='/animal', template_folder='templates')

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
#     return 'Hello from animal'

@bp.route('/cadastroAnimal')
def cadastroAnimal():
    return render_template('cadastrarAnimal.html', estados=Estados)

@bp.route('/pets')
def pets():
    return render_template('listaAnimais.html')

def init_app(app):
    app.register_blueprint(bp)