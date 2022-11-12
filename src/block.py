from src.field import Field

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

    def getField(self, x : int, y: int) -> Field: 
        return self.fields[x][y]

    def getRow(self, x : int) -> list[Field] | None:
        if (not self.checkBounds(x, 0)):
            return None
        return self.fields[x]

    def checkBounds(self, x, y) -> bool:
        if ((x < self.BLOCKWIDTH and x >= 0) and (y < self.BLOCKHEIGHT and y >= 0)):
            return True
        else:
            return False

        
    def getLeastEntropyField(self) -> Field | None:
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

    def removeOptions(self, x : int, y : int, optionsToRemove : list) -> bool:
        if (not self.checkBounds(x, 0)):
            return False

        return self.getField(x, y).removeOptions(optionsToRemove)

    def removeAllOptions(self, options : list[int]): 
        for x in range(10):
            for y in range(3):
                self.getField(x, y).removeOptions(options)