from datetime import datetime
import enum

from app import db

class TaskCompletionStatus(str, enum.Enum):
    complete = 'complete'
    incomplete = 'incomplete'

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    status = db.Column(
        db.Enum(TaskCompletionStatus),
        default = TaskCompletionStatus.incomplete,
        nullable = False
    )

    def __repr__(self):
        return f"<Task {self.title} >"

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'created_at': self.created_at,
            'completion_status': self.status
        }
