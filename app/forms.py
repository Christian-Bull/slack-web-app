from flask_wtf import Form
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class searchQuery(Form):
    channel = StringField('channel', validators=[DataRequired()])
    name = StringField('name')
    submit = SubmitField('query')