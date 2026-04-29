from flask import Flask, request, Blueprint
#create task endpoint
#empty dictionary
tasks= {
   1:{ 
    "title": "flask basics",
    "message": "am learning flask basics then create an application with it",
    "date_added": "22-4-2026"

  },
  2:{ 
    "title": "delete endpoint",
    "message": "am practicing on how to create a delete endpoint",
    "date_added": "23-4-2026"

  },
}
#blueprint
bp_task= Blueprint('bp_task', __name__)
#route
@bp_task.route('/tasks', methods=['POST'])
#FUNCTION
def create_task():

  #convert request to json
  data= request.get_json()
#check for empty data
  if not data:
   return {"message": "empty data not allowed"}
  #receive details
  task_id=data.get("id")
  title = data.get("title")
  message= data.get("message")
  date_created= data.get("date_created") 

  #check if task exists
  if task_id in tasks:
     return {"message": "the title already exists"}
  #save task
  tasks[id]= {
     "title": title,
     "message": message,
     "date_created": date_created
  }
  return {"message": "task added successfully"}

#get all tasks
@bp_task.route('/all', methods=['GET'])
def get_all():
  if not tasks:
    return {"message": "no tasks found"}
  return tasks

#get task by id
#route
@bp_task.route('/tasks/<int:id>', methods=['GET'])
#function
def fetch(id):
  # check if task id exist
  if id not in tasks:
    return {"message": "invalid task id"}
  # return the task
  return tasks[id]

#update task
@bp_task.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
  # convert request to json
  data= request.get_json()

  #receive details
  title= data.get("title")
  message = data.get("message")
  date_created= data.get("date_created")

  #check if task exists
  if id not in tasks:
    return {"message": "invalid task "}
  #update task
  tasks[id]= {
    "title": title,
    "message": message,
    "date_created": date_created
  }
  return {"message": "task updated successfully"}

#delete task
@bp_task.route('/task/<int:id>', methods=['DELETE'])
def delete_task(id):
  
  #check if task exists
  if not tasks[id]:
    return {"message": "the task does not exist"}
  tasks.__delitem__(id)
  return {" message": "task deleted successfully"}