from flask import Flask, render_template
import os
from flask_socketio import SocketIO
import sys;print(sys.version)
from app.generator import Generator
from app.field import Field
from app.block import Block
from app.constraint_controllers.constraints_controller import ConstraintsController

app = Flask(__name__)
socketio = SocketIO(app)

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
    