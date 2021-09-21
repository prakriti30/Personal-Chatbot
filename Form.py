from wtforms import StringField, validators
from flask_wtf import FlaskForm


class TopicForm(FlaskForm):
    query = StringField('Query', [validators.length(min=2, max=50)])
