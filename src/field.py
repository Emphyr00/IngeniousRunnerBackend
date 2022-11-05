import random

class Field:
    def __init__(self):
        self.options = list(range(1, 7))
        self.value = 0
        
    def getValue(self):
        return self.value

    def getOptions(self):
        return self.options

    def getOptionsCount(self):
        return len(self.options)

    def overwritteOptions (self, newOptions):
        self.options = newOptions
    
    def chooseOption(self):
        self.value = random.choice(self.options)
        return self.value

    