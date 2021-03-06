from flask import render_template
from app import app
from app.errors import bp

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html', workspace="subwayparanoia"), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html', workspace="subwayparanoia"), 500