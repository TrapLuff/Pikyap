import time
import contextlib
from time import sleep
from contextlib import contextmanager

class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time.time() - self.start_time
        print(f"time: {elapsed_time} ")

@contextmanager
def cm_timer_2():
    start_time = time.time()
    try:
        yield  # Позволяем выполнить блок кода
    finally:
        elapsed_time = time.time() - start_time
        print(f"time: {elapsed_time} ")

if __name__ == '__main__':
    with cm_timer_1():
        sleep(5.5)

    with cm_timer_2():
        sleep(5.5)