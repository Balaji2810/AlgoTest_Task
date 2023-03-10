import os
import pymongo
from flask import Flask, jsonify,render_template
from pymongo import MongoClient
from flask_cors import CORS



from api import api

app = Flask(__name__)

app.url_map.strict_slashes = False
app.register_blueprint(api)




CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)