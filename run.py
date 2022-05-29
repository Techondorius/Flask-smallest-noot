import sys
sys.dont_write_bytecode = True

from flask import Flask, Blueprint
from flask_cors import CORS
from directory import noot

app = Flask(__name__)
CORS(app)
app.register_blueprint(noot.app)

if __name__ == '__main__':
    app.run()