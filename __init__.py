from flask import Flask, render_template
import os
from flask_socketio import SocketIO, join_room, leave_room, send, emit
from app.generator import Generator
from app.field import Field
from app.block import Block
from app.database.database_connection import DatabaseConnection
from flask_cors import CORS, cross_origin
from app.constraint_controllers.constraints_controller import ConstraintsController

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)

@app.route('/')
def home():
    generator = Generator(ConstraintsController('test'))
    generator.fillBlock()
    string = """"""
    for x in range(10):
        row = str(generator.block.getField(x, 0).getValue()) + ' | ' + str(generator.block.getField(x, 1).getValue()) + ' | ' + str(generator.block.getField(x, 2).getValue())
        string += "[" + row + "] "
    return string
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
    socketio.run(app)
    
@socketio.on('save_run')
def onBlock(data):
    databaseConnection = DatabaseConnection()
    databaseConnection.saveRun(data['username'], data['top_field'], data['bottom_field'], data['left_field'], data['right_field'], data['center_field'])

@socketio.on('request_block')
def onBlock(data):
    generator = Generator(ConstraintsController(data['username']))
    generator.fillBlock()
    
    emit('block', generator.block.toArray(), to=data['username'])

@socketio.on('join')
def onJoin(data):
    username = data['username']
    join_room(username)
    send('user has entered the room.', to=username)

@socketio.on('leave')
def onLeave(data):
    username = data['username']
    leave_room(username)
    send('user has left the room.', to=username)