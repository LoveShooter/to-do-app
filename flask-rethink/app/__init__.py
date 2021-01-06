from flask import Flask


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

from app import views