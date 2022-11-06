from field import Field
from block import Block

class ConstraintsController:

    UNASSIGNED=None
    EMPTY=0
    SINGLE_FENCE=1
    DOUBLE_FENCE=2
    BENCH=3
    WATER=4
    SMALL_WALL=5
    BIG_WALL=6
    BREAKEABLE_WALL=7

    def __init__(self, entropy=8):
        self.entropy = entropy
        self.counter = [0 for i in range(entropy)] # Counter how many elements of each kind were placed

    def getEntropy(entropy) -> int:
        return entropy

    def applySingleFenceContstraints(self, block : Block, field : Field):
        self.counter[field.getValue()] += 1

        # Top
        if (field.y == 0):
            
        # Middle
        elif (field.y == 1):

        # Bottom
        elif (field.y == 2):
            
    
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