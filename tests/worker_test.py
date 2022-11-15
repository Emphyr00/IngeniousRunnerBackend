import unittest
from app.worker.worker import Worker
from app.database.database_connection import DatabaseConnection
import time
import threading

class WorkerTest (unittest.TestCase):
    def test_run(self):
        worker = Worker()
        
        connection = DatabaseConnection()
        connection.refreshDatabase()
        connection.saveUser('alfa')
        connection.saveUser('beta')
        
        self.assertTrue(connection.saveRun('alfa', 1, 5, 1, 5, 1))
        self.assertTrue(connection.saveRun('alfa', 1, 7, 5, 1, 1))
        self.assertTrue(connection.saveRun('alfa', 2, 1, 6, 1, 3))
        self.assertTrue(connection.saveRun('alfa', 1, 2, 1, 1, 1))
        self.assertTrue(connection.saveRun('alfa', 2, 3, 4, 1, 2))
        self.assertTrue(connection.saveRun('alfa', 4, 1, 5, 1, 1))
        self.assertTrue(connection.saveRun('alfa', 1, 7, 1, 3, 1))
        
        self.assertTrue(connection.saveRun('beta', 1, 5, 1, 5, 1))
        self.assertTrue(connection.saveRun('beta', 5, 7, 5, 1, 3))
        self.assertTrue(connection.saveRun('beta', 2, 1, 6, 3, 3))
        self.assertTrue(connection.saveRun('beta', 1, 3, 1, 1, 1))
        self.assertTrue(connection.saveRun('beta', 2, 3, 4, 1, 7))
        self.assertTrue(connection.saveRun('beta', 4, 1, 5, 2, 1))
        self.assertTrue(connection.saveRun('beta', 1, 7, 1, 4, 1))
        
        worker.processTask('alfa')
        worker.processTask('beta')
        
        time.sleep(20)

        self.assertTrue(True)
    