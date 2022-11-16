import unittest
import codecs
from app.database.database_connection import DatabaseConnection
from app.machine_learning.multiple_regression import MultipleRegression
import pickle
import base64
import math
import numpy as np

class DatabaseTest (unittest.TestCase):
    def test_create (self):
        connection = DatabaseConnection()
        self.assertTrue(connection.refreshDatabase())
        
    def test_saveUser(self):
        connection = DatabaseConnection()
        connection.refreshDatabase()
        
        self.assertTrue(connection.saveUser('test'))
        
    def test_getUserByName(self):
        connection = DatabaseConnection()
        connection.refreshDatabase()
        connection.saveUser('test')
        
        user = connection.getUserByName('test')
        
        self.assertEqual(user[0], 1)
        self.assertEqual(user[1], 'test')
        
    def test_saveRun(self):
        connection = DatabaseConnection()
        connection.refreshDatabase()
        connection.saveUser('test')
        
        self.assertTrue(connection.saveRun('test', 1, 1, 1, 1, 1))
        
    def test_getAllRunsByUser(self):
        connection = DatabaseConnection()
        connection.refreshDatabase()
        connection.saveUser('test')
        connection.saveRun('test', 1, 1, 1, 1, 1)
        
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
        connection.refreshDatabase()
        connection.saveUser('test')
        connection.saveRun('test', 1, 1, 1, 1, 1)
        
        self.assertTrue(connection.saveRun('test', 1, 1, 1, 1, 1))
    
    def test_getAllRunsByUser_duplicate(self):
        connection = DatabaseConnection()
        connection.refreshDatabase()
        connection.saveUser('test')
        connection.saveRun('test', 1, 1, 1, 1, 1)
        connection.saveRun('test', 1, 1, 1, 1, 1)
        
        runs = connection.getAllRunsByUser('test')
        
        self.assertEqual(runs[0][0], 1)
        self.assertEqual(runs[0][1], 1)
        self.assertEqual(runs[0][2], 1)
        self.assertEqual(runs[0][3], 1)
        self.assertEqual(runs[0][4], 1)
        self.assertEqual(runs[0][5], 1)
        self.assertEqual(runs[0][6], 1)
        self.assertEqual(runs[0][7], 2)
        
    def test_getUserByName_use_model(self):
        connection = DatabaseConnection()
        connection.refreshDatabase()
        connection.saveUser('test')
        
        model = MultipleRegression()
        
        model.run()
        
        pickle_string = model.serialize()
        
        self.assertTrue(connection.updateUserModel('test', pickle_string))
        user = connection.getUserByName('test')
        
        self.assertEqual(user[0], 1)
        self.assertEqual(user[1], 'test')
        
        model = pickle.loads(base64.b64decode(user[2]))
        
        self.assertEqual(round((model.predict(np.array([[3, 5, 2, 1, 3]]))[0]), 2), round(0.65, 2))
        
    def test_addToQueue(self):
        connection = DatabaseConnection()
        connection.refreshDatabase()
        connection.saveUser('test')
        
        self.assertTrue(connection.addToQueue('test'))
        
    def test_getQueue_empty(self):
        connection = DatabaseConnection()
        connection.refreshDatabase()
        connection.saveUser('test')
        
        self.assertEqual(connection.getQueue() == [])
        
    def test_getQueue_not_empty(self):
        connection = DatabaseConnection()
        connection.refreshDatabase()
        connection.saveUser('test')
        
        connection.addToQueue('test')
        connection.addToQueue('test2')
        connection.addToQueue('test4')
        
        value = connection.getQueue()[0]
        
        self.assertEqual(value[0], 1)
        self.assertEqual(value[1], 'test')
        