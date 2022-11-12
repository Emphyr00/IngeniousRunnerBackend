import random

class Field:
    def __init__(self, x : int, y : int):
        self.options = list(range(1, 7))
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

    def removeOptions(self, optionsToRemove : list) -> bool:
        if (self.getValue() == None):
            return False

        options = self.getOptions()

        for option in optionsToRemove:
            if (option in options):
                options.remove(option)
        
        self.overwritteOptions(options)

        return True
    
    def limitToOption (self, optionTolimit : int) -> bool:
        if (self.getValue() == None):
            return False
        
        options = self.getOptions()

        if (optionTolimit in options):
            options = [ optionTolimit ]
        else:
            options = []

        self.overwritteOptions(options)

        return True