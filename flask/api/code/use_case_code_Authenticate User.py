from flask import Blueprint, request, json
from data_classes import AuthManager

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/auth', methods=['POST'])
def authenticate():
    data = json.loads(request.data)
    username = data.get('username')
    password = data.get('password')

    auth_manager = AuthManager(domain='example.com', client_id='123', client_secret='abc')
    access_token = auth_manager.authenticate(username, password)

    if access_token:
        return json.dumps({'accessToken': access_token})
    else:
        return json.dumps({'error': 'Invalid credentials'}), 401