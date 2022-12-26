import os
import pymongo
from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS
from flasgger import Swagger

from api import api

app = Flask(__name__)

app.url_map.strict_slashes = False
app.register_blueprint(api)


swagger = Swagger(app)

CORS(app)


if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)