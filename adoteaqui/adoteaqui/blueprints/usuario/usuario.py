from flask import Blueprint, render_template, request, redirect, flash, url_for
from .entidades import Usuario
from ...ext.database import db


bp = Blueprint('usuario', __name__, url_prefix='/usuario', template_folder='templates')


# @bp.route('/')
# def root():
#     return 'Hello from usuario'

@bp.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@bp.post('/cadastrarUsuario')
def cadastrarUsuario():
    usuario = Usuario()
    usuario.username = request.form['username']
    usuario.nome = request.form['nome']
    usuario.senha = request.form['senha']
    usuario.telefone = request.form['telefone']
    usuario.email = request.form['email']

    db.session.add(usuario)
    db.session.commit()

    flash('Cadastro feito com sucesso!')
    return redirect(url_for('usuario.login'))


@bp.route('/login')
def login():
    return render_template('login.html')

def init_app(app):
    app.register_blueprint(bp)