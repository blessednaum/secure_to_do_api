from flask import  Flask, request,jsonify, Blueprint, current_app
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from models import User
from extensions import db
from config import Config
#blueprint
bp_user= Blueprint('bp_user', __name__)
#registration endpoint
#route
@bp_user.route('/register', methods=['POST'])
#FUNCTION
def register():
 
 #convert request to json
 data= request.get_json() 

 #receive user details
  
 username=data.get("username")
 password= data.get("password")
 #hash the password
 hashed_password=generate_password_hash(password)

#check if user exists
 existing_user =User.query.filter_by(username=username).first()
 if existing_user:
    return{"message": "the user already exists"}
 
 #save user if they dont exist
 new_user= User(
   
    username= username,
    password= hashed_password
 )
 #save to database
 db.session.add(new_user)
 db.session.commit()

 #response
 return {"message": "user registered successfully"}

#login endpoint
#route
@bp_user.route('/login', methods=['POST'])

#FUNCTION
def login():
   
#convert request to json
 data= request.get_json()

#receive user details
 username= data.get("username")
 password= data.get("password")

#check is user exists
 user= User.query.filter_by(username=username).first()
 if not user:
   return {"message": "user doesnot exist"}

#compare login details
 if not check_password_hash(user.password, password):
   return {"message": "invalid login credentials"}
 
 #generate token
 payload= {
    "user_id": user.user_id,
     "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)

 }
 token= jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm="HS256")
 
 return jsonify({ 
    "message": "you have logged in suceesfully",
   "token": token})
