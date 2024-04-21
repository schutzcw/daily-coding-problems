from typing import Any, Callable
import logger


logger = logger.basicConfig()


def func1():
    print("function1 called")

    
def func2():
    print("function2 called")


class Scheduler():
    """
    """
    
    def schedule(func: Callable[..., Any], time_ms: int) -> None:
        """ """
        # trigger_time = time.time() + time_ms
        # add (trigger_time, func) to a a SortedMap
        # in a while loop, check if front of sorted map trigger time is less than current time,
        # if so, pop and run
        
if __name__ == "__main__":