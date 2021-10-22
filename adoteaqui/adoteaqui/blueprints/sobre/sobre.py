from flask import Blueprint, render_template


bp = Blueprint('sobre', __name__, url_prefix='/sobre', template_folder='templates')


# @bp.route('/')
# def root():
#     return 'Hello from sobre'

@bp.route('/')
def sobre():
    return render_template('sobre.html')

def init_app(app):
    app.register_blueprint(bp)