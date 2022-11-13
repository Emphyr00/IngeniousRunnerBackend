import unittest
from src.block import Block
from src.field import Field
from src.generator import Generator
from src.constraints_controller import ConstraintsController

class GeneratorTest (unittest.TestCase):
    def test_fillBlock(self):
        generator = Generator(ConstraintsController())
        self.assertIsInstance(generator.fillBlock(), Block)
        
       
        print('')
        
        for x in range(10):
            row = str(generator.block.getField(x, 0).getValue()) + ' | ' + str(generator.block.getField(x, 1).getValue()) + ' | ' + str(generator.block.getField(x, 2).getValue())
            print(row)
