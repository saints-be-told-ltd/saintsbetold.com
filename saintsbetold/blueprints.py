from flask import Blueprint, render_template, current_app

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


# Sitemap

@blueprints.route('/sitemap.xml')
def sitemap():
    pages = [rule for rule in current_app.url_map.iter_rules() if rule.arguments.__len__() == 0]
    return render_template('sitemap.xml', pages=pages)
