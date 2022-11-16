from threading import Thread
from collections import deque
from app.machine_learning.multiple_regression import MultipleRegression
from app.worker.repeat_timer import RepeatTimer
from app.database.database_connection import DatabaseConnection
import time
import asyncio


class Worker:
    def __init__(self):
        self.running = False
        self.deamon = None
        self.databaseConnection = DatabaseConnection()
    
    async def start (self):
        print('QUEUE START')
        while self.running:
            print('QUEUE LOOP')
            await asyncio.sleep(5)
            item = self.databaseConnection.getQueue()
            if (item != []):
                MultipleRegression().trainModelForUser(item[0][1])
                
        return
        
    def stop(self):
        self.running = False
    
    def addToQueue(self, userName):
        self.databaseConnection.addToQueue(userName)
        


        
        
    
        
        
       
        
        
            