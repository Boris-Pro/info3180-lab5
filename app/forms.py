# Add any form classes for Flask-WTF here

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed

class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    poster = FileField('Movie Poster', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Only JPEG and PNG images are allowed.')])
