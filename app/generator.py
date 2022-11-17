from app.constraint_controllers.constraints_controller import ConstraintsController
from app.field import Field
from app.block import Block

class Generator:
    def __init__(self, constraintsController : ConstraintsController):
        self.constraintsController = constraintsController
        self.block = Block()
        
    def updateOptions(self, field : Field):
        value = field.getValue()
        
        if value == self.constraintsController.EMPTY:
            return
        if value == self.constraintsController.SINGLE_FENCE:
            self.constraintsController.applySingleFenceContstraints(self.block, field)
        if value == self.constraintsController.DOUBLE_FENCE:
            self.constraintsController.applyDoubleFenceContstraints(self.block, field)
        if value == self.constraintsController.BENCH:
            self.constraintsController.applyBenchContstraints(self.block, field)
        if value == self.constraintsController.WATER:
            self.constraintsController.applyWaterContstraints(self.block, field)
        if value == self.constraintsController.SMALL_WALL:
            self.constraintsController.applySmallWallContstraints(self.block, field)
        if value == self.constraintsController.BIG_WALL:
            self.constraintsController.applyBigWallContstraints(self.block, field)
        if value == self.constraintsController.BREAKABLE_WALL:
            self.constraintsController.applyBreakableWallContstraints(self.block, field)
                
    def fillBlock(self):
        end = False
        while end == False:
            end = True
            field = self.block.getLeastEntropyField()
            if (field != None and field.getValue() == self.constraintsController.UNASSIGNED):
                end = False
                fieldValue = self.constraintsController.chooseOption(field, self.block)

                field.value = fieldValue
                
                self.updateOptions(field)
                
        return self.block