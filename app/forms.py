from app import models
from flask_wtf import Form
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms import validators

class searchQuery(Form):
    channel = SelectField('channel', choices=models.getDistinctChannels())
    name = StringField('name', [validators.optional()])
    submit = SubmitField('query')