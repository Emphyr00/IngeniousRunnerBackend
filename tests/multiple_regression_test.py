import unittest
from app.machine_learning.multiple_regression import MultipleRegression
from app.database.database_connection import DatabaseConnection

class MultipleRegressionTest (unittest.TestCase):
    def test_trainModelForUser(self):
        connection = DatabaseConnection()
        connection.refreshDatabase()
        connection.saveUser('test')
        
        self.assertTrue(connection.saveRun('test', 1, 5, 1, 5, 1))
        self.assertTrue(connection.saveRun('test', 1, 7, 5, 1, 1))
        self.assertTrue(connection.saveRun('test', 2, 1, 6, 1, 3))
        self.assertTrue(connection.saveRun('test', 1, 2, 1, 1, 1))
        self.assertTrue(connection.saveRun('test', 2, 3, 4, 1, 2))
        self.assertTrue(connection.saveRun('test', 4, 1, 5, 1, 1))
        self.assertTrue(connection.saveRun('test', 1, 7, 1, 3, 1))
        
        mr = MultipleRegression()
        
        self.assertTrue(mr.trainModelForUser('test'))