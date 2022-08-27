# config
from flask import Flask

app = Flask(__name__)

# index route
@app.route('/')
def index():
    return 'Hello, this is PetFax!'

# pets index route
@app.route('/pets')
def pets():
    return 'These are our incredible pets available for adoption!'
