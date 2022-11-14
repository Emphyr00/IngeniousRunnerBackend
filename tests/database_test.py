import unittest
import codecs
from database.database_connection import DatabaseConnection
from src.multiple_regression import MultipleRegression
import pickle
import base64
import numpy as np

class DatabaseTest (unittest.TestCase):
    def test_create (self):
        connection = DatabaseConnection()
        self.assertTrue(connection.refreshDatabase())
        
    def test_saveUser(self):
        connection = DatabaseConnection()
        self.assertTrue(connection.saveUser('test'))
        
    def test_getUserByName(self):
        connection = DatabaseConnection()
        user = connection.getUserByName('test')
        
        self.assertEqual(user[0], 1)
        self.assertEqual(user[1], 'test')
        
    def test_saveRun(self):
        connection = DatabaseConnection()
    
        self.assertTrue(connection.saveRun('test', 1, 1, 1, 1, 1))
        
    def test_getAllRunsByUser(self):
        connection = DatabaseConnection()
        
        runs = connection.getAllRunsByUser('test')
        
        self.assertEqual(runs[0][0], 1)
        self.assertEqual(runs[0][1], 1)
        self.assertEqual(runs[0][2], 1)
        self.assertEqual(runs[0][3], 1)
        self.assertEqual(runs[0][4], 1)
        self.assertEqual(runs[0][5], 1)
        self.assertEqual(runs[0][6], 1)
        self.assertEqual(runs[0][7], 1)
        
    def test_saveRun_duplicate(self):
        connection = DatabaseConnection()
        self.assertTrue(connection.saveRun('test', 1, 1, 1, 1, 1))
    
    def test_getAllRunsByUser_duplicate(self):
        connection = DatabaseConnection()
        
        runs = connection.getAllRunsByUser('test')
        
        self.assertEqual(runs[0][0], 1)
        self.assertEqual(runs[0][1], 1)
        self.assertEqual(runs[0][2], 1)
        self.assertEqual(runs[0][3], 1)
        self.assertEqual(runs[0][4], 1)
        self.assertEqual(runs[0][5], 1)
        self.assertEqual(runs[0][6], 1)
        self.assertEqual(runs[0][7], 2)
        
    def test_updateUserModel(self):
        connection = DatabaseConnection()
        
        model = MultipleRegression()
        
        model.run()
        
        pickle_string = str(model.serialize())
        
        pickle_string = pickle_string[1:]
        
        print(pickle_string)
        
        connection.updateUserModel('test', pickle_string)
        
        
    def test_getUserByName_use_model(self):
        connection = DatabaseConnection()
        user = connection.getUserByName('test')
        
        self.assertEqual(user[0], 1)
        self.assertEqual(user[1], 'test')
        
        model = pickle.loads(base64.b64decode(user[2]))
        
        self.assertEqual((model.predict(np.array([[3, 5, 2, 1, 3]]))[0]), 0.6507436894402281)
        