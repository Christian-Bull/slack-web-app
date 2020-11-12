from flask import render_template, redirect
from app import app, PyMongo
from app.forms import searchQuery

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', 
        title=app.config['WORKSPACE'], 
        workspace=app.config['WORKSPACE']
    )

@app.route('/about')
def about():
    return render_template('about.html', 
        title=app.config['WORKSPACE'], 
        workspace=app.config['WORKSPACE']
    )

@app.route('/query', methods=['GET', 'POST'])
def query():
    form = searchQuery()
    return render_template('query.html',
        title=app.config['WORKSPACE'], 
        workspace=app.config['WORKSPACE'],
        form=form
    )
