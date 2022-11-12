from field import Field
from block import Block

class ConstraintsController:

    BLOCKWIDTH=10
    BLOCKHEIGHT=3

    UNASSIGNED=None
    EMPTY=0
    SINGLE_FENCE=1
    DOUBLE_FENCE=2
    BENCH=3
    WATER=4
    SMALL_WALL=5
    BIG_WALL=6
    BREAKABLE_WALL=7

    def __init__(self, entropy=8):
        self.entropy = entropy
        self.counter = [0 for i in range(entropy)] # Counter how many elements of each kind were placed

    def getEntropy(entropy) -> int:
        return entropy

    def checkBounds(self, x, y) -> bool:
        if ((x < self.BLOCKWIDTH and x > 0) and (y < self.BLOCKHEIGHT and y > 0)):
            return True
        else:
            return False

    def applySingleFenceContstraints(self, block : Block, field : Field):
        self.counter[field.getValue()] += 1
        
        if (self.checkBounds(field.x + 1, field.y)): 
            block.removeOptions(field.x + 1, field.y, [self.DOUBLE_FENCE])
        
        if (self.checkBounds(field.x - 1, field.y)):
            block.removeOptions(field.x + 1, field.y, [self.DOUBLE_FENCE])

        row = block.getRow(field.x)
        count = 0
        for field in row:
            if (field.getValue() == self.SINGLE_FENCE or field.getValue() == self.DOUBLE_FENCE):
                count += 1

        if (count >= 2):
            for field in row:
                field.removeOptions([self.SINGLE_FENCE, self.DOUBLE_FENCE])
                

    def applyDoubleFenceContstraints(self, block : Block, field : Field):
        self.counter[field.getValue()] += 1
    
    def applyBenchContstraints(self, block : Block, field : Field):
        self.counter[field.getValue()] += 1
    
    def applyWaterContstraints(self, block : Block, field : Field):
        self.counter[field.getValue()] += 1

    def applySmallWallContstraints(self, block : Block, field : Field):
        self.counter[field.getValue()] += 1
    
    def applyBigWallContstraints(self, block : Block, field : Field):
        self.counter[field.getValue()] += 1

    def applyBreakableWallContstraints(self, block : Block, field : Field):
        self.counter[field.getValue()] += 1

        