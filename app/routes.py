from app import myobj
from flask import flash, render_template

name="Filler"
city_names=["Hanford", "Hanford 2: Electric Boogaloo"]
@myobj.route("/")

def home():
    return render_template('home.html',name=name, city_names=city_names)
