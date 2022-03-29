from flask import Flask

myobj = Flask(__name__)
myobj.config.from_mapping(
    SECRET_KEY="test"
)

from app import routes