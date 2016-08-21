from flask import Blueprint, render_template

blueprints = Blueprint('page', __name__, template_folder='templates/pages')


# Homepage --------------------------------------------------------------------

@blueprints.route('/')
def home():
    return render_template('index.html')


# Legal Policy ----------------------------------------------------------------

@blueprints.route('/legal/privacy/')
def privacy():
    return render_template('legal/privacy.html')


@blueprints.route('/legal/terms/')
def terms():
    return render_template('legal/terms.html')
