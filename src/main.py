from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

from models.database import db 
from models.tabela import Tabela

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "data", "database.db")

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

from routes.rotas import rotas_bp
app.register_blueprint(rotas_bp)


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(
        debug=True,
        )