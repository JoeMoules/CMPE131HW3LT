from app import myobj
from flask import flash, redirect, render_template, Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os
class form(FlaskForm):
    cityName=StringField('City')
    submit=SubmitField("Submit")

name="Filler"
city_names=["Hanford", "Hanford 2: Electric Boogaloo"]
'''@myobj.route("/")

def home():
    input=form()
    return render_template('home.html',name=name, city_names=city_names, form=input)
'''
@myobj.route("/", methods=['GET', 'POST'])
def home():
    print("test")
    input=form()
    if input.validate_on_submit():
        print("test")
        flash(input.cityName.data)
        print("test")
    return render_template('home.html', name=name, city_names=city_names, form=input)