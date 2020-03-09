from datetime import datetime
from todo import db

class User(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    username = db.Column(db.String(25),nullable=False)
    password = db.Column(db.String(20), nullable=False)
    tasks = db.relationship('Task', backref='owner', lazy=True)

class Task(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    task_title = db.Column(db.String(50),nullable=False)
    task_desc = db.Column(db.String(120), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.INTEGER,db.ForeignKey('user.id'), nullable=False)