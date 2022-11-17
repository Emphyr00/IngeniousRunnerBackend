import unittest
from app.block import Block
from app.field import Field
from app.constraint_controllers.constraints_controller_ml_hard import ConstraintsControllerMlHard
from app.database.database_connection import DatabaseConnection
from app.machine_learning.multiple_regression import MultipleRegression

class ConstraintsControllerTest (unittest.TestCase):
    def test_create(self):
        connection = DatabaseConnection()
        connection.refreshDatabase()
        
        connection.saveUser('test')
        
        connection.saveRun('test', 1, 5, 1, 5, 1)
        connection.saveRun('test', 1, 7, 5, 1, 1)
        connection.saveRun('test', 2, 1, 6, 1, 3)
        connection.saveRun('test', 1, 2, 1, 1, 1)
        connection.saveRun('test', 2, 3, 4, 1, 2)
        connection.saveRun('test', 4, 1, 5, 1, 4)
        connection.saveRun('test', 1, 7, 1, 3, 1)
        
        mr = MultipleRegression('test')
        
        mr.trainModelForUser()
        
        cc = ConstraintsControllerMlHard('test')
        
        self.assertIsInstance(cc, ConstraintsControllerMlHard)