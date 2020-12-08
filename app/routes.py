from flask import render_template, flash, redirect, url_for
from app import app, PyMongo, models
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
    if form.validate_on_submit():
        id = models.get_channel_id(form.channel.data)
        
        return render_template('query-results.html',
                               channel_id=id,
                               title=app.config['WORKSPACE'],
                               workspace=app.config['WORKSPACE']
                               )
    return render_template('query.html',
                           title=app.config['WORKSPACE'],
                           workspace=app.config['WORKSPACE'],
                           form=form
                           )
