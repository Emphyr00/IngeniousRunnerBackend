from flask import Flask, render_template, request
import os
import json
# from flask_socketio import SocketIO, join_room, leave_room, send, emit
from app.generator import Generator
from app.field import Field
from app.block import Block
from app.database.database_connection import DatabaseConnection
from flask_cors import CORS, cross_origin
from app.constraint_controllers.constraints_controller import ConstraintsController
from app.constraint_controllers.constraints_controller_ml_hard import ConstraintsControllerMlHard


def create_app():
    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    
    @app.route('/')
    def home():
        generator = Generator(ConstraintsController('test'))
        generator.fillBlock()
        string = """"""
        for x in range(10):
            row = str(generator.block.getField(x, 0).getValue()) + ' | ' + str(generator.block.getField(x, 1).getValue()) + ' | ' + str(generator.block.getField(x, 2).getValue())
            string += "[" + row + "] "
        return string
    
    @app.route('/api/block', methods=['GET'])
    @cross_origin()
    def getBlock():
        if (not request.args.get('username')):
            generator = Generator(ConstraintsController(''))
            generator.fillBlock()
            return { "block": json.dumps(generator.block.toArray()) }
        else:
            generator = Generator(ConstraintsControllerMlHard(request.args.get('username')))
            generator.fillBlock()
            return { "block": json.dumps(generator.block.toArray()) }, 200
      
    @app.route('/api/user', methods=['POST'])
    @cross_origin()
    def postUser():
        databaseConnection = DatabaseConnection()
        user = databaseConnection.getUserByName(request.json['username'])
        
        if (user == []):
            databaseConnection.saveUser(request.json['username'])
            
        return { "user": json.dumps(databaseConnection.getUserByName(request.json['username'])) }, 200
    
    @app.route('/api/run', methods=['POST'])
    @cross_origin()
    def postRun():
        databaseConnection = DatabaseConnection()
        user = databaseConnection.getUserByName(request.json['username'])
        
        if (user == []):
            return { "errro": "NO USER" }, 409
        
        databaseConnection.saveRun(request.json['username'], request.json['top_field'], request.json['bottom_field'], request.json['left_field'], request.json['right_field'], request.json['center_field'])
            
        return { "OK": "Saved" }, 200
      
        
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
    # socketio.run(app)
    
# @socketio.on('save_run')
# def onBlock(data):
#     print("save_run")
#     databaseConnection = DatabaseConnection()
#     databaseConnection.saveRun(data['username'], data['top_field'], data['bottom_field'], data['left_field'], data['right_field'], data['center_field'])

# @socketio.on('request_block')
# def onBlock(data):
#     print("request_block")
#     generator = Generator(ConstraintsController(data['username']))
#     generator.fillBlock()
    
#     emit('block', generator.block.toArray(), to=data['username'])

# @socketio.on('join')
# def onJoin(data):
#     print("join")
#     username = data['username']
#     join_room(username)
#     send('user has entered the room.', to=username)

# @socketio.on('leave')
# def onLeave(data):
#     print("leave")
#     username = data['username']
#     leave_room(username)
#     send('user has left the room.', to=username)
    

    
