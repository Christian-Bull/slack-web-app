from app import models
from flask_wtf import Form
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms import validators

class searchQuery(Form):
    channel = SelectField('channel', choices=models.get_distinct_channels())
    name = StringField('display name', [validators.optional()])
    results_limit = SelectField('results limit',
        [validators.optional()],
        choices=[i for i in range(26)]
    )
    submit = SubmitField('query')

