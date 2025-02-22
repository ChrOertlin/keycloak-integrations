# app/views/pages.py
from flask import Blueprint, render_template

blueprint = Blueprint('pages', __name__, template_folder='templates')


@blueprint.route('/')
def index():
    return render_template('index.html')