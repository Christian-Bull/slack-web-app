from flask import render_template, flash, redirect, url_for
from app import app, PyMongo, models, slack
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
        channel_id = models.get_channel_id(form.channel.data)

        # if thers's a name get the id
        if form.name.data != '':
            user_id = models.get_user_id(form.name.data)

            # if a null userid was return
            if user_id == None:
                return render_template('query.html',
                                       title=app.config['WORKSPACE'],
                                       workspace=app.config['WORKSPACE'],
                                       form=form,
                                       message="User doesn't exists"
                                       )

        # get headers
        headers, data = slack.get_pins(channel_id, user_id, form.name.data)

        return render_template('query-results.html',
                               title=app.config['WORKSPACE'],
                               workspace=app.config['WORKSPACE'],
                               user=form.name.data,
                               headers=headers,
                               data=data
                               )

    return render_template('query.html',
                           title=app.config['WORKSPACE'],
                           workspace=app.config['WORKSPACE'],
                           form=form
                           )
