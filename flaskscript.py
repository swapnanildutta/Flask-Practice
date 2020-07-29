#from flask import Manager
from flask_script import Manager
from flask import Flask
from dynamicroute import app
manager= Manager(app)
#app=Flask(__name__)

@manager.command
def hello():
    print('hello')



if __name__=='__main__':
    manager.run()