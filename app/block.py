from app.field import Field

# 0 none
# 1 single fence
# 2 double fence
# 3 bench
# 4 water
# 5 small wall
# 6 big wall
# 7 hitable wall

class Block:
    BLOCKWIDTH=10
    BLOCKHEIGHT=3
    
    def __init__(self):
        self.fields = [[Field(x, y) for y in range(3)] for x in range(10)]

    def getField(self, x : int, y: int): 
        return self.fields[x][y]

    def getRow(self, x : int):
        if (not self.checkBounds(x, 0)):
            return None
        return self.fields[x]

    def checkBounds(self, x, y):
        if ((x < self.BLOCKWIDTH and x >= 0) and (y < self.BLOCKHEIGHT and y >= 0)):
            return True
        else:
            return False

        
    def getLeastEntropyField(self):
        least = 10
        field = None
        for x in range(10):
            for y in range(3):
                if (self.getField(x, y).getValue() == None):
                    count = self.getField(x, y).getOptionsCount()
                    if (count < least):
                        least = count
                        field = self.getField(x, y)
        return field

    def removeOptions(self, x : int, y : int, optionsToRemove : list):
        if (not self.checkBounds(x, 0)):
            return False

        return self.getField(x, y).removeOptions(optionsToRemove)

    def removeAllOptions(self, options): 
        for x in range(10):
            for y in range(3):
                self.getField(x, y).removeOptions(options)
                
    def toArray(self):
        block = []
        for i in range(0, 10):
            row = []
            row.append(self.getField(i, 0).getValue())
            row.append(self.getField(i, 1).getValue())
            row.append(self.getField(i, 2).getValue())
            block.append(row)
            
        return block