from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from crud_helpers import retrieve_json_package, HelperException

frontend = Blueprint('frontend', __name__, 
					 template_folder='templates', static_folder='static')

@frontend.route('/')
def index():
	return render_template('index.html')

@frontend.route('/create', defaults={'id': None })
@frontend.route('/edit/<id>')
def create(id):
	return render_template('create.html')

@frontend.route('/view/<string:id>')
def view(id):
	try:
		return render_template("view.html", 
			packageData=retrieve_json_package(id))
	except HelperException as e:
		abort(404)

@frontend.route('/404', defaults={'e': 'Page not Found'})
@frontend.app_errorhandler(404)
def notfound(e):
	return render_template('notfound_template.html'), 404