from extensions import db

#db tables
class User(db.Model):
    user_id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(225), nullable=False)