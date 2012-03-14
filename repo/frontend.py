from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

frontend = Blueprint('frontend', __name__, 
					 template_folder='templates', static_folder='static')

@frontend.route('/')
def index():
	return render_template('index.html')

@frontend.route('/create', defaults={'id': None })
@frontend.route('/edit/<id>')
def create(id):
	return render_template('create.html')