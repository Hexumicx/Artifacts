import threading
import queue
import time

from cooldown import resolve_cooldown

from Move import move
from Fight import fight_rest, fight_loop
from Gather import gather_loop


class Character:
    def __init__(self, name):
        self.name = name
        self.location = (0, 0)
        self.action_queue = queue.Queue()
        self.stop_flag = threading.Event()
        self.thread = threading.Thread(target=self.background_loop, daemon=True)
        self.start()

    def background_loop(self):
        while True:
            if self.stop_flag.is_set():
                print(f"Stopping background thread for {self.name}")
                break

            if self.action_queue.empty():
                time.sleep(10)
                
            front = self.action_queue.get()
            func, args = front['function'], front['args'] 
            args['char'] = self.name 
            result = self.do_action(func, args)
            resolve_cooldown(result)

    def add_action(self, func, args):
        self.action_queue.put({
            'function': func,
            'args': args
        })
    
    def stop(self):
        self.stop_flag.set()
        self.thread.join()

    def start(self):
        print(f"Starting background thread for {self.name}")
        self.thread.start()

    def do_action(self, func, args):
        if func == "move":
            return move(**args)
        elif func == "fight":
            return fight_loop(**args)
        elif func == "gather":
            return gather_loop(**args)