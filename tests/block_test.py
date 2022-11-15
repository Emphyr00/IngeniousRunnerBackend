import unittest
from app.block import Block
from app.field import Field
from app.constraint_controllers.constraints_controller import ConstraintsController

class BlockTest (unittest.TestCase):
    def test_create(self):
        block = Block()
        self.assertEqual(len(block.fields), 10)
        self.assertEqual(len(block.fields[0]), 3)
        
    def test_getField(self):
        block = Block()
        self.assertIsInstance(block.getField(0, 0), Field)
        
    def test_get_row_correct(self):
        block = Block()
        row = block.getRow(0)
        self.assertIsInstance(row, list)
        self.assertEqual(len(row), 3)
        
    def test_get_row_not_correct(self):
        block = Block()
        row = block.getRow(15)
        self.assertEqual(row, None)
    
    def test_getLeastEntropyField_all_same_entropy(self):
        block = Block()
        field = block.getLeastEntropyField()
        
        self.assertIsInstance(field, Field)
    
    def test_getLeastEntropyField_predictible_outcome(self):
        block = Block()
        block.getField(5, 2).options = [1]
        block.getField(6, 2).options = [1, 2]
        
        field = block.getLeastEntropyField()
        
        self.assertEqual(field.x, 5)
        self.assertEqual(field.y, 2)
        
    def test_removeOptions(self):
        block = Block()
        
        self.assertEqual(block.removeOptions(0, 0, [1, 2, 3]), True)
    
        self.assertCountEqual([4, 5, 6, 7], block.getField(0, 0).options)
        
    def test_removeAllOptions(self):
        block = Block()
        
        block.removeAllOptions([1, 2, 3, 4, 5, 6])
        
        for x in range(10):
            for y in range(3):
                self.assertCountEqual(block.getField(x, y).options, [7])