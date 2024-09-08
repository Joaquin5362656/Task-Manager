from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson.objectid import ObjectId
from src.extensions import mongo

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()
    status = request.args.get('status')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))

    query = {'user_id': ObjectId(user_id)}
    if status:
        query['status'] = status

    tasks_cursor = mongo.db.tasks.find(query).skip((page - 1) * per_page).limit(per_page)
    tasks_list = [{'id': str(task['_id']), 'title': task['title'], 'status': task['status']} for task in tasks_cursor]

    return jsonify(tasks_list), 200

@tasks_bp.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    user_id = get_jwt_identity()
    title = request.json.get('title')
    status = request.json.get('status', 'pending')

    task = {
        'user_id': ObjectId(user_id),
        'title': title,
        'status': status
    }

    result = mongo.db.tasks.insert_one(task)
    return jsonify({'id': str(result.inserted_id)}), 201

@tasks_bp.route('/tasks/<task_id>', methods=['PUT'])
@jwt_required()
def update_task(task_id):
    user_id = get_jwt_identity()
    title = request.json.get('title')
    status = request.json.get('status')

    task = mongo.db.tasks.find_one({'_id': ObjectId(task_id), 'user_id': ObjectId(user_id)})
    if not task:
        return jsonify({'msg': 'Task not found'}), 404

    update_data = {}
    if title:
        update_data['title'] = title
    if status:
        update_data['status'] = status

    mongo.db.tasks.update_one({'_id': ObjectId(task_id)}, {'$set': update_data})

    return jsonify({'msg': 'Task updated'}), 200

@tasks_bp.route('/tasks/<task_id>', methods=['DELETE'])
@jwt_required()
def delete_task(task_id):
    user_id = get_jwt_identity()

    task = mongo.db.tasks.find_one({'_id': ObjectId(task_id), 'user_id': ObjectId(user_id)})
    if not task:
        return jsonify({'msg': 'Task not found'}), 404

    mongo.db.tasks.delete_one({'_id': ObjectId(task_id)})
    return jsonify({'msg': 'Task deleted'}), 200