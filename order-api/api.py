from os import environ
from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response

app_name = 'client-api'
app = Flask(app_name)
app.debug = True

carts = {}
retries = []
@app.route('/api/create/cart', methods=['POST'])
def create_cart():
    request_data = request.get_json()

    email = request_data['email']
    products = request_data['products']

    new_cart = {
        'email': email,
        'products': products
    }

    try:
        carts[email] = [new_cart]
  
        response = {
            'message': f'Cart for {email} created'
        }

        statusCode = 200
    except Exception as ex:
        print (ex)
        response = {
            'message': f'Cart for {email} failed: {ex}'
        }
        statusCode = 500

    return make_response(jsonify(response), statusCode)

@app.route('/api/carts')
def get_carts():
    return make_response(jsonify(carts), 200)

@app.route('/api/retries/<retries_quantity>')
def retry_route(retries_quantity:int):

    if  len(retries) < int(retries_quantity):
        response = {
            'message': f'Below retries of: {retries_quantity}'
        }
        retries.append("1")
        return make_response(jsonify(response), 500)
    else:
        response = {
            'message': f'Reached number of retries: {retries_quantity}'
        }
        retries.clear()
        return make_response(jsonify(response), 200)


