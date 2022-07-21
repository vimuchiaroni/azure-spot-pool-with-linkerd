from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response
from os import environ
import requests as r 


app_name = 'client-api'
app = Flask(app_name)
app.debug = True
cart_service_url=environ['CART_SERVICE_URL']

@app.route('/create/cart', methods=['POST'])
def create_cart():
    request_data = request.get_json()
    
    _return = r.post(f'{cart_service_url}/api/create/cart', json=request_data)
    
    if 200 == _return.status_code:
    

        response = {
                'status': 'SUCCESS',
                'message': _return.content,
                }
        statusCode = 200

    else:
        response = {
                'status': 'FAILED',
                'message': _return.content,
                }
        statusCode = 500

    return make_response(_return.content, statusCode)

@app.route('/get/carts')
def get_carts():
    param = request.args.get('email')
    _return = r.get(f'{cart_service_url}/api/cart?email={param}')
    return make_response(_return.content, _return.status_code)

@app.route('/retries/upstream/cart/<retries_quantity>')
def retries_upstream_cart(retries_quantity):
    _return = r.get(f'{cart_service_url}/api/retries/{retries_quantity}')
    return make_response(_return.content, _return.status_code)
