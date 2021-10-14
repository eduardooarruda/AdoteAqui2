from flask import Blueprint, redirect, url_for, request, flash
from ...ext.database import db
from ..usuario.entidades import Usuario
from ...ext.bcrypt import bcrypt

bp = Blueprint('autenticacao', __name__, url_prefix='/autenticacao')


# @bp.route('/')
# def root():
#     return 'Hello from autenticacao'

@bp.post('/cadastrarUsuario')
def cadastrarUsuario():

    if Usuario.query.filter_by(username=request.form['username']).first() is not None:
        flash('Este nome de usuário já existe!')
        return redirect(url_for('usuario.cadastro'))

    usuario = Usuario()
    usuario.username = request.form['username']
    usuario.nome = request.form['nome']
    usuario.senha = bcrypt.generate_password_hash(request.form['senha'])
    usuario.telefone = request.form['telefone']
    usuario.email = request.form['email']

    db.session.add(usuario)
    db.session.commit()

    flash('Cadastro feito com sucesso!')
    return redirect(url_for('usuario.login'))

def init_app(app):
    app.register_blueprint(bp)