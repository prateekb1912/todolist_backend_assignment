from flask import jsonify, request

from app import db
from app.main import bp
from app.models import Task

from logging import Logger


logger = Logger(__name__)

def error_message():
    return jsonify({
        'error': 'Bad Request',
        'message': 'Please specify a title for the task'
    })

@bp.route('/', methods = ['GET'])
def get_all_tasks():
    tasks = Task.query.order_by(Task.created_at.desc()).all()

    return [task.serialize() for task in tasks]

@bp.route('/', methods = ['POST'])
def create_task():
    data = request.get_json()

    if 'title' not in data:
        return error_message()

    new_task = Task(
        title=data['title']
    )

    db.session.add(new_task)
    db.session.commit()

    return new_task.serialize()


@bp.route('/tasks/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def task_by_id(id):
    task = Task.query.filter_by(id=id).first_or_404()

    if request.method == 'PUT':
        data = request.get_json()

        if 'title' not in data:
            return error_message()

        task.title = data['title']

        db.session.commit()

        return task.serialize()
    
    if request.method == 'DELETE':
        db.session.delete(task)
        db.session.commit()

        return jsonify({
            'status': '200 OK',
            'message': 'Task has been deleted successfully'
        })
        
    return task.serialize()


@bp.route('/tasks/status/<string:status>', methods = ['GET'])
def get_tasks_by_status(status):
    if status not in ['complete', 'incomplete']:
        return jsonify({
            'error': 'Bad Request',
            'message': 'Please specify correct status - complete/incomplete'
        })
    
    tasks = Task.query.filter_by(status = status).all()

    return [task.serialize() for task in tasks]

@bp.route('/tasks/update/<int:id>', methods = ['POST'])
def update_task_status(id):
    task = Task.query.filter_by(id=id).first_or_404()

    if task.status == 'incomplete':
        task.status = 'complete'
    else:
        task.status = 'incomplete'

    db.session.commit()

    return task.serialize()