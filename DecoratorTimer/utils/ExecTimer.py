import time
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class ExecTimer(object):

    def __init__(self, task_name):
        self.logger = logging.getLogger(self.__class__.__name__)
        print(self.__class__.__name__)
        self.task_name = task_name
        self.start_time = time.time()

    def __enter__(self):
        logging.info(f'>>>>Starting {self.task_name}...')        
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.interval = self.end_time - self.start_time
        logging.info(f'<<Finished {self.task_name} in {self.interval} seconds')        

    def get_time_since_start(self):
        return time.time() - self.start_time

