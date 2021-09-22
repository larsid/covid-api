from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import ProductionConfig


config = ProductionConfig

server = Flask(__name__)
server.config.from_object(config)
db = SQLAlchemy(server)