import threading
from log import get_logger

logger = get_logger(__name__)

class ThreadManager:
    def __init__(self):
        self.threads = {}

    def create_thread(self, name, target, args=(), should_be_stopped=True):
        event = threading.Event()
        thread = threading.Thread(target=target, args=(event, *args))
        thread.start()
        self.threads[name] = {
            'thread': thread,
            'event': event, 
            'should_be_stopped': should_be_stopped
        }

    def get_thread(self, name):
        return self.threads.get(name)

    def is_thread_set(self, name):
        thread_info = self.get_thread(name)
        if thread_info:
            return thread_info['event'].is_set()
        return False

    def stop_all_threads(self):
        for name, thread_info in self.threads.items():
            if thread_info['should_be_stopped']:
                logger.info(f"Stopping thread: {name}")
                thread_info['event'].set()
                thread_info['thread'].join()
            else:
                logger.info(f"Not stopping thread: {name}")
