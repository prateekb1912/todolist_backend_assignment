from flask import jsonify, request

from app import db
from app.main import bp
from app.models import Task

from logging import Logger
from datetime import datetime

logger = Logger(__name__)

def error_message():
    return jsonify({
        'error': 'Bad Request',
        'message': 'Please specify a title for the task'
    })

@bp.route('/', methods = ['GET'])
@bp.route('/tasks', methods = ['GET'])
def get_all_tasks():
    tasks = Task.query.order_by(Task.created_at.desc()).all()

    return [task.serialize() for task in tasks]

@bp.route('/', methods = ['POST'])
@bp.route('/tasks', methods = ['POST'])
def create_task():
    data = request.get_json()

    if 'title' not in data:
        return error_message()

    existing_task = Task.query.filter_by(title=data['title']).first()

    if existing_task:
        return jsonify({
            'error': 'Bad Request',
            'message': 'Task with same title already exists.'
        })

    current_time = datetime.now()

    new_task = Task(
        title = data['title'],
        created_at = current_time,
        last_updated = current_time
    )

    db.session.add(new_task)
    db.session.commit()

    return new_task.serialize()


@bp.route('/tasks/<int:id>', methods = ['GET'])
def get_task_by_id(id):
    task = Task.query.filter_by(id=id).first_or_404()
        
    return task.serialize()

@bp.route('/tasks/update/<int:id>', methods=['PUT'])
def update_task_by_id(id):
    data = request.get_json()

    if 'title' not in data:
        return error_message()

    same_title_task = Task.query.filter_by(title=data['title']).first()

    if same_title_task:
        return jsonify({
            'error': 'Bad Request',
            'message': 'Task with same title already exists.'
        })

    task = Task.query.filter_by(id=id).first_or_404()

    task.title = data['title']
    task.last_updated = datetime.now()

    db.session.commit()

    return task.serialize()

@bp.route('/tasks/delete/<int:id>', methods=['DELETE'])
def delete_task_by_id(id):
    task = Task.query.filter_by(id=id).first_or_404()

    db.session.delete(task)
    db.session.commit()

    return jsonify({
        'status': '200 OK',
        'message': 'Task has been deleted successfully'
    })


@bp.route('/tasks/status/<string:status>', methods = ['GET'])
def get_tasks_by_status(status):
    if status not in ['complete', 'incomplete']:
        return jsonify({
            'error': 'Bad Request',
            'message': 'Please specify correct status - complete/incomplete'
        })
    
    tasks = Task.query.filter_by(status = status).all()

    return [task.serialize() for task in tasks]

@bp.route('/tasks/status/update/<int:id>', methods = ['POST'])
def update_task_status(id):
    task = Task.query.filter_by(id=id).first_or_404()

    if task.status == 'incomplete':
        task.status = 'complete'
    else:
        task.status = 'incomplete'

    task.last_updated = datetime.now()

    db.session.commit()

    return task.serialize()