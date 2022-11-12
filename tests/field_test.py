import unittest
from src.field import Field

class FieldTest (unittest.TestCase):
    def test_create(self):
        field = Field(0, 0)
        
        self.assertEqual(field.x, 0)
        
        self.assertEqual(field.y, 0)
    
    def test_getValue(self):
        field = Field(0, 0)
        
        self.assertEqual(field.getValue(), None)
        
    def test_getOptions(self):
        field = Field(0, 0)
        options = field.getOptions()
        
        for i in range(7):
            self.assertEqual(options[i], i+1)
        
    def test_getOptionsCount(self):
        field = Field(0, 0)
        
        self.assertEqual(field.getOptionsCount(), 7)
        
    def test_overwritteOptions(self):
        field = Field(0, 0)
        field.overwritteOptions([1, 2])
        
        self.assertEqual(field.getOptionsCount(), 2)
        
    def test_chooseOptions_with_all_available(self):
        field = Field(0, 0)
        value = field.chooseOption()
        
        self.assertIsInstance(value, int)
        
        self.assertTrue(value < 8 and value > 0 )
    
    def test_chooseOptions_with_none_available(self):
        field = Field(0, 0)
        field.overwritteOptions([])
        value = field.chooseOption()
        
        self.assertEqual(value, 0)
    
    def test_removeOptions_without_value(self):
        field = Field(0, 0)
        
        self.assertEqual(field.removeOptions([2, 3, 4, 5, 6, 7]), True)
        
        self.assertEqual(field.getOptions(), [1])
        
    def test_removeOptions_with_value(self):
        field = Field(0, 0)
        field.value = 1
        
        self.assertEqual(field.removeOptions([2, 3, 4, 5, 6, 7]), False)
        
        self.assertEqual(field.getOptions(), [1, 2, 3, 4, 5, 6, 7])
        
    def test_limitToOption_without_value(self):
        field = Field(0, 0)
        
        self.assertEqual(field.limitToOption(1), True)
        
        self.assertEqual(field.getOptions(), [1])
        
    def test_limitToOption_with_value(self):
        field = Field(0, 0)
        field.value = 1
        
        self.assertEqual(field.limitToOption(1), False)
        
        self.assertEqual(field.getOptions(), [1, 2, 3, 4, 5, 6, 7])