from flask import Flask, request, Blueprint
from models import Task
from utils.auth import get_current_user
from extensions import db


#blueprint
bp_task= Blueprint('bp_task', __name__)

#route
@bp_task.route('/tasks', methods=['POST'])
#FUNCTION
def create_task():
#get logged user
 user_id =get_current_user()

 #check if user exists
 if not user_id:
   return {"message": "unauthorised user"}, 404
  
  #if user exists receive their details
 data=request.get_json()

 task = Task(
        title=data.get("title"),
        message=data.get("message"),
        date_created= data.get("date_created"),
        user_id=user_id ) #from the token
#save to db
 db.session.add(task)
 db.session.commit()
 return {"message": "task created succcessfully"}
   
# #get task by id
@bp_task.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):

#check is user is logged in
 user_id= get_current_user()
 if not user_id:
  return {"message": "unauthorised user"}
 #if user exists
 task = Task.query.get(id)
 #check if task exixts
 if not task:
  return {"message": "task does not exist"}
 #check if existing task belongs to that user
 if task.user_id !=user_id:
  return {"message": "forbidden"}
 #if task belongs to user
 return {
  "id": task.task_id,
  "title": task.title,
  "message": task.message,
  "date": task.date_created
 }

# #update task
@bp_task.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
 #check if user is logged in 
 user_id = get_current_user()
 if not user_id:
  return {"message": "unauthorised user"}
#get task
 task= Task.query.get(id)
#check if task exists
 if not task:
  return {"messsage": "task does not exist"}
 
 #if task exists compare if it belongs to the logged in user
 if task.user_id != user_id:
  return {"message": "forbiden"}
 #update the task
 data= request.get_json()
 task.title = data.get("title", task.title)
 task.message = data.get("message", task.message)
 task.date_created = data.get("date_created", task.date_created)

#save changes to db
 db.session.commit()

 return {"message": "task updated successfully"}
# #delete task
@bp_task.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
 #check if user is logged in 
 user_id= get_current_user()
 if not user_id:
   return {"message": "unauthorised user"}
 # check if task exists
 task=Task.query.get(id)
 if not task:
   return {"message": "task does not exist"}
 #compare if existing task belongs to the logged in user
 if task.user_id !=user_id:
   return {"message": "forbidden"}

#if true delete
 db.session.delete(task)
 db.session.commit()
 return {"message": "task deleted successfully"}