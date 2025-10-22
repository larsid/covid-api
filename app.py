import os
from threading import Lock
from flask_cors import CORS
from flask import Flask, jsonify, request
from flask.wrappers import Request as FlaskRequest

from api.controllers import (
    CreateUserController, GetAllUsersController, GetSickestUsersController,
    GetUserByIDController, RemoveUserController, UpdateUserController
)
from api.helpers import parse_request
from api.infra import UsersRepository
from api.protocols import Controller


app        = Flask(__name__)
cors       = CORS(app, origins=['*'])
repository = UsersRepository()
lock       = Lock()


def make_response(controller: Controller, request: FlaskRequest):
    response = controller.handle(parse_request(request))
    return jsonify(response.body), response.status_code


@app.route('/', methods=['GET'])
def index():
    return jsonify({'data': 'Ok'}), 200


@app.route('/users/<int:id>', methods=['GET'])
def get_user(id: int):
    controller = GetUserByIDController(id, repository)
    return make_response(controller, request)


@app.route('/users', methods=['GET'])
def get_users():
    controller = GetAllUsersController(repository)
    return make_response(controller, request)


@app.route('/users/sickest/<int:limit>', methods=['GET'])
def get_sickest_users(limit: int):
    controller = GetSickestUsersController(limit, repository)
    return make_response(controller, request)


@app.route('/users', methods=['POST'])
def create_user():
    with lock:
        controller = CreateUserController(repository)
        return make_response(controller, request)


@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id: int):
    controller = UpdateUserController(id, repository)
    return make_response(controller, request)
    
    
@app.route('/users/<int:id>', methods=['DELETE'])
def remove_user(id: int):
    controller = RemoveUserController(id, repository)
    return make_response(controller, request)
    


if(__name__=='__main__'):
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)), debug=False)