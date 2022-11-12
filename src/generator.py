from src.constraints_controller import ConstraintsController
from src.field import Field
from src.block import Block

class Generator:
    def __init__(self, constraintsController : ConstraintsController):
        self.constraintsController = constraintsController
        self.block = Block()
        
    def updateOptions(self, field : Field) -> None:
        match field.getValue():
            case self.EMPTY:
                return
            case self.constraintsController.SINGLE_FENCE:
                self.constraintsController.applySingleFenceContstraints(self, self.self.block, field)
            case self.constraintsController.DOUBLE_FENCE:
                self.constraintsController.applyDoubleFenceContstraints(self, self.block, field)
            case self.constraintsController.BENCH:
                self.constraintsController.applyBenchContstraints(self, self.block, field)
            case self.constraintsController.WATER:
                self.constraintsController.applyWaterContstraints(self, self.block, field)
            case self.constraintsController.SMALL_WALL:
                self.constraintsController.applySmallWallContstraints(self, self.block, field)
            case self.constraintsController.BIG_WALL:
                self.constraintsController.applyBigWallContstraints(self, self.block, field)
            case self.constraintsController.BREAKABLE_WALL:
                self.constraintsController.applyBreakableWallContstraints(self, self.block, field)
                
    def fillBlock(self):
        end = False
        while end == False:
            end = True
            field = self.block.getLeastEntropyField()
            if (field != self.constraintsController.UNASSIGNED):
                end = False
                field.chooseOption()
                self.updateOptions(field)