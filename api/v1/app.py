#!/usr/bin/python3
"""app Module"""
from flask import Flask, jsonify, make_response
# from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
# app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
# cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(junk):
    """
    Removes the current SQLAlchemy Session
    """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """
    Returns the 404 error JSON string
    """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    h = getenv('HBNB_API_HOST', default='0.0.0.0')
    p = getenv('HBNB_API_PORT', default='5000')
    app.run(host=h, port=p, threaded=True)
