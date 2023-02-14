from main import bp


@bp.route('/', methods = ['GET'])
def get_all_tasks():
    tasks = db.session.execute(db.select(Task).order_by(Task.created_at)).scalars()

    return tasks
