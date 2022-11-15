from threading import Thread
from collections import deque
from app.machine_learning.multiple_regression import MultipleRegression
from app.worker.repeat_timer import RepeatTimer
import asyncio

class Worker:
    def __init__(self):
       self.loop = asyncio.get_event_loop()
    
    def processTask(self, userName):
        return self.loop.run_until_complete(self.__async__trainModel(userName))
    
    async def __async__trainModel(self, userName):
        await asyncio.get_event_loop().create_task(MultipleRegression().trainModelForUser(userName))
        
        
    
        
        
       
        
        
            