from flask import render_template, flash
from app import app
from app.forms import searchQuery

@app.route('/')
@app.route('/index')
def index():
    form = searchQuery()
    return render_template(
        'index.html', 
        title=app.config['WORKSPACE'], 
        workspace=app.config['WORKSPACE'], 
        form=form
    )

@app.route('/about')
def about():
    return render_template('about.html', 
        title=app.config['WORKSPACE'], 
        workspace=app.config['WORKSPACE']
    )
