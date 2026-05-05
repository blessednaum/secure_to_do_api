from extensions import db

#db tables
class User(db.Model):
    user_id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(225), nullable=False)

#relationship
    tasks = db.relationship('Task', backref='user', lazy=True)
#task table
class Task(db.Model):
    task_id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(225), nullable=False)
    date_created = db.Column(db.String(225), nullable=False)

#foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)