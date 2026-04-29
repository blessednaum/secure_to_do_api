from flask import Flask
from config import Config
from extensions import db
from routes.users import bp_user
from routes.tasks import bp_task

#initialize app
app= Flask(__name__)

#use the settings in the config
app.config.from_object(Config)
#connect app to db
db.init_app(app)
# register blueprints
app.register_blueprint(bp_user)
app.register_blueprint(bp_task)
#commands for creating the table
with app.app_context():
    db.create_all()  
#run application
if __name__ =='__main__':
    app.run(debug=True)