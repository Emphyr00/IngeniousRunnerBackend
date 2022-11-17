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
        
        connection.saveRun('test', 1, 5, 1, 5, 1)
        connection.saveRun('test', 1, 7, 5, 1, 1)
        connection.saveRun('test', 2, 1, 6, 7, 7)
        connection.saveRun('test', 1, 2, 1, 1, 7)
        connection.saveRun('test', 2, 3, 4, 1, 2)
        connection.saveRun('test', 4, 1, 5, 1, 0)
        connection.saveRun('test', 1, 7, 1, 3, 7)
        
        model = MultipleRegression('test')
        
        model.trainModelForUser()
        
        user = connection.getUserByName('test')
        
        self.assertEqual(user[0], 1)
        self.assertEqual(user[1], 'test')
        
        model.getModel()
        
        self.assertTrue(model.predict(1, 2, 3, 4, 5) > 0)
        
    def test_addToQueue(self):
        connection = DatabaseConnection()
        connection.refreshDatabase()
        connection.saveUser('test')
        
        self.assertTrue(connection.addToQueue('test'))
        
    # def test_getQueue_empty(self):
    #     connection = DatabaseConnection()
    #     connection.refreshDatabase()
    #     connection.saveUser('test')
        
    #     self.assertEqual(connection.getQueue() == [])
        
    # def test_getQueue_not_empty(self):
    #     connection = DatabaseConnection()
    #     connection.refreshDatabase()
    #     connection.saveUser('test')
        
    #     connection.addToQueue('test')
    #     connection.addToQueue('test2')
    #     connection.addToQueue('test4')
        
    #     value = connection.getQueue()[0]
        
    #     self.assertEqual(value[0], 1)
    #     self.assertEqual(value[1], 'test')
        