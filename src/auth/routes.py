from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token 
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId 
from src.extensions import mongo

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    users = mongo.db.users
    email = request.json.get('email')
    password = request.json.get('password')

    if users.find_one({'email': email}):
        return jsonify({'msg': 'User already exists'}), 400

    hashed_password = generate_password_hash(password)
    users.insert_one({'email': email, 'password': hashed_password})

    return jsonify({'msg': 'User created successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    email = request.json.get('email')
    password = request.json.get('password')

    user = users.find_one({'email': email})

    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity=str(user['_id']))
        return jsonify({'token': access_token}), 200

    return jsonify({'msg': 'Bad credentials'}), 401