from app.field import Field
from app.block import Block

class ConstraintsController:
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

    def getEntropy(self) -> int:
        return self.entropy

    def applySingleFenceContstraints(self, block : Block, field : Field):
        self.counter[field.getValue()] += 1
        if (self.counter[field.getValue()] > 10):
            block.removeAllOptions([field.getValue()])
        
        # remove double fence from next field
        if (block.checkBounds(field.x + 1, field.y)): 
            block.removeOptions(field.x + 1, field.y, [self.DOUBLE_FENCE])
        
        # remove double fence from previous field
        if (block.checkBounds(field.x - 1, field.y)):
            block.removeOptions(field.x + 1, field.y, [self.DOUBLE_FENCE])

        # remove any fence from row if more then 2 are present
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
        if (self.counter[field.getValue()] > 5):
            block.removeAllOptions([field.getValue()])
        
        # remove double fence from next field
        if (block.checkBounds(field.x + 1, field.y)): 
            block.removeOptions(field.x + 1, field.y, [self.DOUBLE_FENCE])
        
        # remove double fence from previous field
        if (block.checkBounds(field.x - 1, field.y)):
            block.removeOptions(field.x + 1, field.y, [self.DOUBLE_FENCE])
    
        # remove double fence from all fields in row
        row = block.getRow(field.x)
        for field in row:
            field.removeOptions([self.DOUBLE_FENCE])

        # remove single from row if more then 2 are present
        count = 0
        for field in row:
            if (field.getValue() == self.SINGLE_FENCE or field.getValue() == self.DOUBLE_FENCE):
                count += 1

        if (count >= 2):
            for field in row:
                field.removeOptions([self.SINGLE_FENCE])
    
    def applyBenchContstraints(self, block : Block, field : Field):
        self.counter[field.getValue()] += 1

        row = block.getRow(field.x)

        for field in row:
            field.removeOptions([ self.BIG_WALL, self.BREAKABLE_WALL ])
    
    def applyWaterContstraints(self, block : Block, field : Field):
        self.counter[field.getValue()] += 1
        
        row = block.getRow(field.x)
        
        for field in row:
            field.removeOptions([ self.BENCH, self.WATER, self.SMALL_WALL, self.BIG_WALL ])
        
        if (block.checkBounds(field.x + 1, field.y)): 
            block.removeOptions(field.x + 1, field.y, [self.SMALL_WALL, self.BIG_WALL, self.BREAKABLE_WALL])

    def applySmallWallContstraints(self, block : Block, field : Field):
        self.counter[field.getValue()] += 1

        row = block.getRow(field.x)

        for field in row:
            field.removeOptions([ self.WATER, self.SMALL_WALL ])
    
    def applyBigWallContstraints(self, block : Block, field : Field):
        self.counter[field.getValue()] += 1
        
        if (block.checkBounds(field.x - 1, field.y)): 
            block.removeOptions(field.x - 1, field.y, [self.WATER])

        row = block.getRow(field.x)
        
        countNone=0
        countBigWall=0
        for field in row:
            field.removeOptions([ self.BENCH, self.WATER, self.SMALL_WALL ])
            if (field.getValue() == None):
                 countNone += 1
            if (field.getValue() == self.BIG_WALL):
                 countBigWall += 1
        
        # Wall row
        if (countBigWall == 2):
            for field in row:
                field.limitToOption(self.BREAKABLE_WALL)

        # target wall row
        if (countNone >= 2):
            for field in row:
                field.removeOptions([self.SINGLE_FENCE, self.DOUBLE_FENCE, self.SMALL_WALL, self.WATER, self.BENCH])
                  

    def applyBreakableWallContstraints(self, block : Block, field : Field):
        self.counter[field.getValue()] += 1

        row = block.getRow(field.x)

        countWalls=0
        for field in row:
            if (field.getValue() == self.BIG_WALL or field.getValue() == self.BREAKABLE_WALL):
                countWalls += 1
            # dont want to have water bench or small wall same row
            field.removeOptions([ self.BENCH, self.WATER, self.SMALL_WALL ])

        # two walls are there add another breakable or big
        if (countWalls >= 2):
            field.removeOptions([ self.SINGLE_FENCE, self.DOUBLE_FENCE ])


        