import unittest
from app.block import Block
from app.field import Field
from app.generator import Generator
from app.constraint_controllers.constraints_controller import ConstraintsController
from app.constraint_controllers.constraints_controller_ml_hard import ConstraintsControllerMlHard
from app.database.database_connection import DatabaseConnection
from app.machine_learning.multiple_regression import MultipleRegression


class GeneratorTest (unittest.TestCase):
    def test_fillBlock_random(self):
        generator = Generator(ConstraintsController('test'))
        self.assertIsInstance(generator.fillBlock(), Block)
        
        for x in range(10):
            row = str(generator.block.getField(x, 0).getValue()) + ' | ' + str(generator.block.getField(x, 1).getValue()) + ' | ' + str(generator.block.getField(x, 2).getValue())
            print(row)

    def test_fillBlock_ml(self):
        connection = DatabaseConnection()
        connection.refreshDatabase()
        
        connection.saveUser('test')
        
        connection.saveRun('test', 7, 7, 7, 7, 7)
        connection.saveRun('test', 6, 6, 6, 6, 6)
        connection.saveRun('test', 5, 5, 5, 5, 5)
        connection.saveRun('test', 4, 4, 4, 4, 4)
        connection.saveRun('test', 3, 3, 3, 3, 3)
        connection.saveRun('test', 2, 2, 2, 2, 2)
        connection.saveRun('test', 1, 1, 1, 1, 1)
        connection.saveRun('test', 0, 0, 0, 0, 0)
        connection.saveRun('test', 6, 6, 6, 6, 6)
        connection.saveRun('test', 6, 6, 6, 4, 1)
        connection.saveRun('test', 1, 6, 1, 1, 1)
        connection.saveRun('test', 1, 6, 1, 1, 1)
        connection.saveRun('test', 1, 6, 1, 3, 1)
        connection.saveRun('test', 1, 6, 1, 1, 1)
        connection.saveRun('test', 1, 3, 1, 1, 1)
        connection.saveRun('test', 1, 1, 1, 2, 2)
        connection.saveRun('test', 1, 2, 1, 1, 2)
        connection.saveRun('test', 1, 3, 7, 4, 2)
        connection.saveRun('test', 1, 1, 1, 2, 1)
        connection.saveRun('test', 1, 2, 1, 1, 1)
        connection.saveRun('test', 1, 5, 1, 1, 1)
        
        mr = MultipleRegression('test')
        
        mr.trainModelForUser()
        
        generator = Generator(ConstraintsControllerMlHard('test'))
        self.assertIsInstance(generator.fillBlock(), Block)
        
        for x in range(10):
            row = str(generator.block.getField(x, 0).getValue()) + ' | ' + str(generator.block.getField(x, 1).getValue()) + ' | ' + str(generator.block.getField(x, 2).getValue())
            print(row)

