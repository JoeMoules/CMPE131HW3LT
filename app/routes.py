from app import myobj
from flask import flash, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

name="Filler"
city_names=["Hanford", "Hanford 2: Electric Boogaloo"]
@myobj.route("/", methods=['GET', 'POST'])

def home():
    form=input()
    if form.validate_on_submit():
        flash('{}' .format(input.cityName.data))
    return render_template('home.html',name=name, city_names=city_names, form=form)
