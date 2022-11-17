from app.constraint_controllers.constraints_controller import ConstraintsController
from app.field import Field
from app.block import Block
from app.machine_learning.multiple_regression import MultipleRegression
import random

class ConstraintsControllerMlHard(ConstraintsController):
    def __init__(self, userName):
        self.counter = [0 for i in range(8)] # Counter how many elements of each kind were placed
        self.userName = userName
        self.model = MultipleRegression(userName)
        self.model.getModel()
        
    def chooseOption(self, fieldTarget : Field, block : Block):
        if (len(fieldTarget.getOptions()) == 0):
            return 0
        else:
            if (self.model.regr == None):
                return random.choice(fieldTarget.getOptions())
            # left, center, right, top, bottom
            fields = []
            row = block.getRow(fieldTarget.x)
            for field in row:
                if (field.getValue() == None):
                    fields.append(-1)
                else: 
                    fields.append(field.getValue())
                    
            if (block.checkBounds(fieldTarget.x + 1, fieldTarget.y)):
                if (block.getField(fieldTarget.x + 1, fieldTarget.y).getValue() == None):
                    fields.append(-1)
                else:
                    fields.append(block.getField(fieldTarget.x + 1, fieldTarget.y).getValue())
                
            else:
                fields.append(-1)
            
            if (block.checkBounds(fieldTarget.x - 1, fieldTarget.y)):
                if (block.getField(fieldTarget.x - 1, fieldTarget.y).getValue() == None):
                    fields.append(-1)
                else:
                    fields.append(block.getField(fieldTarget.x - 1, fieldTarget.y).getValue())
                
            else:
                fields.append(-1)
                
            emptyCount = 0
            for field in fields:
                if (field == -1):
                    emptyCount += 1
            
            # if more then 2 fields are not ussigned there is no point in running machine learning
            if (emptyCount > 3):
                return random.choice(fieldTarget.getOptions())
            
            else:
                topValue = -1
                topOption = -1
                options = fieldTarget.getOptions()
                for option in options:
                    fields[fieldTarget.y] = option
                    value = self.model.predict(left_field=fields[0], center_field=fields[1], right_field=fields[2], top_field=fields[3], bottom_field=fields[4])
                    if (value > topValue):
                        topOption = option
                        topValue = value
                
                # if the results from classifier are very poor we just want to get rundom element
                if (topValue <= 0):
                    return random.choice(fieldTarget.getOptions())
                else:
                    return topOption
                    
            