from collections import deque
from task import Task
from threading import Timer
from abc import ABC, abstractmethod

class Listener(ABC):
    @abstractmethod
    def start_task(self, task):
        pass

    @abstractmethod
    def end_task(self, task):
        pass

class Scheduler:
    _instance = None

    _task_queue = None
    _task_queue_capacity = 0

    _listeners = []

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        
        return cls._instance
    
    def __init__(self, capacity):
        if hasattr(self, "_initialized"):
            return
    
        self._taskQueue = deque(maxlen = capacity)
        self._taskQueueCapacity = capacity
        self._listeners = []
        self._initialized = True

    def get_capacity(self):
        return self._taskQueue.maxlen
    
    def get_tasks(self):
        return list(self._taskQueue)
    
    def add_task(self, t: Task):
        if len(self._taskQueue) != self._taskQueue.maxlen:
            self._taskQueue.append(t)
        else:
            print("The task queue is full. Task not added.")

    def add_listener(self, l):
        self._listeners.append(l)

    def run(self):
        next = self._pop_task()

        if next:
            self._signal_start(next)
            timer = Timer(5, lambda: self._signal_end(next))
            timer.start()
            timer.join()

        next = self._pop_task()

        while next:
            timer = Timer(2, lambda: self._signal_start(next))
            timer.start()
            timer.join()
            timer = Timer(5, lambda: self._signal_end(next))
            timer.start()
            timer.join()
            next = self._pop_task()
            
        print("All tasks complete.")

    def _signal_start(self, task):
        for listener in self._listeners:
            listener.start_task(task)

    def _signal_end(self, task):
        for listener in self._listeners:
            listener.end_task(task)

    def _pop_task(self):
        if len(self._taskQueue) == 0:
            return None
        else:
            return self._taskQueue.popleft()


