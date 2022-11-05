from field import Field;
# 0 none
# 1 single fence
# 2 double fence
# 3 bench
# 4 water
# 5 small wall
# 6 big wall
# 7 hitable wall

class Block:
    def __init__(self):
        self.fields = [[Field()] * 3 for _ in range(10)]
        self.globalConstraints = list(range(1, 7))
        self.operations = 30,

    def getField(self, x : int, y: int) -> Field: 
        return self.array[x][y]

    def fillBlock(self):
        for opetations in range(self.operations): 
            option = self.getLeastRandomField().chooseOption()
            
        
    def getLeastRandomField(self) -> Field:
        least = 10
        field = None
        for x in range(10):
            for y in range(3):
                if (self.getField(x, y).getValue() == 0):
                    count = self.getField(x, y).getOptionsCount()
                    if (count < least):
                        least = count
                        field = self.getField(x, y)
        return field     

    def updateOptions(self, field, x, y):

