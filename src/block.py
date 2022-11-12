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
        return self.fields[x][y]

    def getRow(self, x : int) -> list[Field]:
        return self.fields[x]

    def fillBlock(self):
        end = False
        while end == False:
            end = True
            field = self.getLeastEntropyField()
            if (field != self.constraintsController.UNASSIGNED):
                end = False
                field.chooseOption()
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

    def updateOptions(self, field : Field) -> None:
        match field.getValue():
            case self.EMPTY:
                return
            case self.constraintsController.SINGLE_FENCE:
                self.constraintsController.applySingleFenceContstraints(self, field)
            case self.constraintsController.DOUBLE_FENCE:
                self.constraintsController.applyDoubleFenceContstraints(self, field)
            case self.constraintsController.BENCH:
                self.constraintsController.applyBenchContstraints(self, field)
            case self.constraintsController.WATER:
                self.constraintsController.applyWaterContstraints(self, field)
            case self.constraintsController.SMALL_WALL:
                self.constraintsController.applySmallWallContstraints(self, field)
            case self.constraintsController.BIG_WALL:
                self.constraintsController.applyBigWallContstraints(self, field)
            case self.constraintsController.BREAKABLE_WALL:
                self.constraintsController.applyBreakableWallContstraints(self, field)

    def removeOptions(self, x : int, y :int, optionsToRemove : list) -> bool:
        field = self.getField(x, y)

        return field.removeOptions(optionsToRemove)

    