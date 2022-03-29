from flask import Flask

myobj = Flask(__name__)
myobj.secret_key="TOP_SNEAKY"

from app import routes