from ...ext.database import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(30), nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    estado = db.Column(db.String(30), nullable=False)
    cidade = db.Column(db.String(30), nullable=False)
    bairro = db.Column(db.String(30), nullable=False)
    rua = db.Column(db.String(30), nullable=False)
    numero = db.Column(db.Integer, nullable=False)

    facebook = db.Column(db.String(30))
    instagram = db.Column(db.String(30))
    whatsapp = db.Column(db.String(20))
    telegram = db.Column(db.String(20))
    # localizacao = db.relationship('Endereco', backref='usuario', lazy=True)


# class Endereco(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     estado = db.Column(db.String(30), nullable=False)
#     cidade = db.Column(db.String(30), nullable=False)
#     bairro = db.Column(db.String(30), nullable=False)
#     rua = db.Column(db.String(30), nullable=False)
#     numero = db.Column(db.Integer, nullable=False)
#     usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)