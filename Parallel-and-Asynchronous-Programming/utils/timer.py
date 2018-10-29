from contextlib import ContextDecorator
import time

class DecoTimer(ContextDecorator):
    """
    A timer that helps trace the execution time
    task_name (str) : name of the task
    """

    def __init__(self, task_name):
        self.task_name = task_name

    def __enter__(self):
        self.start_time = time.time()
        print(f'>>>>Starting Function {self.task_name}...')        
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.interval = self.end_time - self.start_time
        print(f'<<Finished function {self.task_name} in {self.interval} seconds')