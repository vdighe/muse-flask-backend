from flask import Flask, jsonify, g
from flask_cors import CORS

from resources.songs import song # import the song object

import models

DEBUG = True
PORT = 8000

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)

@app.before_request
def before_request():
    """Connect to DB before each request"""
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response

CORS(song, origins=['http://localhost:3000'], supports_credentials=True) # adding this line

app.register_blueprint(song, url_prefix='/api/v1/songs') # adding this line


# The default URL ends in / ("my-website.com/").
@app.route('/')
def index():
    return 'hi'

@app.route('/json')    
def muse():
    return jsonify(name='Vaishali', age='30')

# Run the app when the program starts!
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)