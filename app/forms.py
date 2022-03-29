from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class input(FlaskForm):
    cityName=StringField('City Name', validators=[DataRequired()])
    submit = SubmitField("Submit")