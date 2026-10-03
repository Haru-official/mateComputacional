from flask import Blueprint, render_template

principal_bp = Blueprint('principal', __name__)

@principal_bp.route('/')
def index():
    return render_template('indexPantallaPrincipal.html')