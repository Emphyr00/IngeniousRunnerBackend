import random

class Field:
    def __init__(self, x : int, y : int):
        self.options = list(range(0, 7))
        self.value = None
        self.x = x
        self.y = y
        
    def getValue(self):
        return self.value

    def getOptions(self):
        return self.options

    def getOptionsCount(self):
        return len(self.options)

    def overwritteOptions (self, newOptions):
        self.options = newOptions
    
    def chooseOption(self):
        if (len(self.options) == 0):
            self.value = 0
        else:
            self.value = random.choice(self.options)
        return self.value

    