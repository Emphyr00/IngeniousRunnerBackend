from field import Field;
from constraints_controller import ConstraintsController
# 0 none
# 1 single fence
# 2 double fence
# 3 bench
# 4 water
# 5 small wall
# 6 big wall
# 7 hitable wall

class Block:
    def __init__(self, constraintsController : ConstraintsController):
        self.constraintsController = constraintsController
        self.fields = [[Field(x, y, self.constraintsController.getEntropy()) for y in range(3)] for x in range(10)]

    def getField(self, x : int, y: int) -> Field: 
        return self.array[x][y]

    def fillBlock(self):
        while end == False:
            end = True
            field = self.getLeastEntropyField()
            if (field != self.UNASSIGNED):
                end = False
                option = field.chooseOption()
                self.updateOptions(field)
        
    def getLeastEntropyField(self) -> Field | None:
        least = 10
        field = None
        for x in range(10):
            for y in range(3):
                if (self.getField(x, y).getValue() == self.UNASSIGNED):
                    count = self.getField(x, y).getOptionsCount()
                    if (count < least):
                        least = count
                        field = self.getField(x, y)
        return field     

    def updateOptions(self, field : Field):
        match field.getValue():
            case self.EMPTY:
                return True
            case self.SINGLE_FENCE:
                self.constraintsController.applySingleFenceContstraints(self, field)
            case self.DOUBLE_FENCE:
                self.constraintsController.applySingleFenceContstraints(self, field)
            case self.BENCH:
                self.constraintsController.applyBenchContstraints(self, field)
            case self.WATER:
                self.constraintsController.applyWaterContstraints(self, field)
            case self.SMALL_WALL:
                self.constraintsController.applySmallWallContstraints(self, field)
            case self.BIG_WALL:
                self.constraintsController.applyBigWallContstraints(self, field)
            case self.BRAKEABLE_WALL:
                self.constraintsController.applyBreakableWallContstraints(self, field)
    