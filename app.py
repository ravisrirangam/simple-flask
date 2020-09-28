import sys,os,os.path
import warnings
warnings.filterwarnings('ignore')
from ibm_ai_openscale import APIClient4ICP
from ibm_ai_openscale.engines import *
from ibm_ai_openscale.utils import *
from ibm_ai_openscale.supporting_classes import PayloadRecord, Feature
from ibm_ai_openscale.supporting_classes.enums import *

import pandas as pd
import requests
from ibm_ai_openscale.utils import get_instance_guid
from functools import wraps

from flask import Flask, jsonify, request, abort, Response
import json
import urllib3, requests
from flask_cors import CORS, cross_origin

def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
        headers = request.headers.get('Access-Control-Request-Headers')
        if headers:
            response.headers['Access-Control-Allow-Headers'] = headers
    return response


app = Flask(__name__)
CORS(app)

def limit_content_length(max_length):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            cl = request.content_length
            if cl is not None and cl > max_length:
                abort(413)
            return f(*args, **kwargs)
        return wrapper
    return decorator




@app.route('/')
def Welcome():
	return 'Welcome to OpenScale API app running on CP4D'

port = os.getenv('VCAP_APP_PORT', '5010')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
