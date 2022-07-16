from distutils.log import debug

from numpy import true_divide
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'"
#  debug done