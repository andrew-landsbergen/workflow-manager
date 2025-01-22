from task import Task
from scheduler import Listener

class NotificationManager(Listener):
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        
        return cls._instance
    
    def __init__(self):
        if hasattr(self, "_initialized"):
            return
    
        self._initialized = True

    def start_task(self, task: Task):
        print("Task started")

    def end_task(self, task: Task):
        print("Task ended")