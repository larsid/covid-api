import os
from flask import request, jsonify
from app import server, db
from app.models import User


@server.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Connected'}), 200


@server.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id: int):
    user = User.query.get(user_id)
    if(user is None):
        return jsonify({'message': 'User not found'}), 404

    return jsonify({'message': user.json()}), 200


@server.route('/users', methods=['GET'])
def get_users():
    users = [user.json() for user in User.query.all()]
    return jsonify({'message': users}), 200


@server.route('/users', methods=['POST'])
def create_user():
    user = User(**request.json).create()
    return jsonify({'id': user.id}), 200


@server.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id: int):
    user = User.query.get(user_id)
    if(user is None):
        return jsonify({'message': 'User not found'}), 404
    
    try:
        user.update(request.json)
    except:
        return jsonify({'message': 'Bad Request'}), 503
    return jsonify({'message': 'User updated'}), 200
    

@server.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):
    user = User.query.get(user_id)
    if(user is None):
        return jsonify({'message': 'User not found'}), 404
    
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted'}), 200
    


if(__name__=='__main__'):
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))