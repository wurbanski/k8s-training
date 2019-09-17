import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return os.uname()[1]


app.run(host='0.0.0.0')
