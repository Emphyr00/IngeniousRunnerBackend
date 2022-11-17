import unittest
from app.block import Block
from app.field import Field
from app.constraint_controllers.constraints_controller import ConstraintsController

class ConstraintsControllerTest (unittest.TestCase):
    def test_create(self):
        cc = ConstraintsController('test')
        
        self.assertIsInstance(cc, ConstraintsController)
        
    def test_getEntropy(self):
        cc = ConstraintsController('test')

        self.assertEqual(cc.getEntropy(), 8)
        
    def test_chooseOptions_with_all_available(self):
        block = Block()
        cc = ConstraintsController('test')
        field = block.getField(0, 0)
        value = cc.chooseOption(field, block)
        
        self.assertIsInstance(value, int)
        
        self.assertTrue(value < 8 and value > 0 )
    
    def test_chooseOptions_with_none_available(self):
        block = Block()
        cc = ConstraintsController('test')
        field = block.getField(0, 0)
        field.overwritteOptions([])
        value = cc.chooseOption(field, block)
        
        self.assertEqual(value, 0)