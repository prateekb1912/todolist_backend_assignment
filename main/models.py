from datetime import datetime

from main import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    status = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Task {self.description} >"
