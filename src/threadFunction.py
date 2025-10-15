from threading import Thread
from typing import Callable
def threadFn(func = Callable[[], None]):
    '''Launch a new thread for a function.'''
    t = Thread(target=func)
    t.start()