from typing import Iterable

class PeekableInterface(object):

    SENTINEL = "PEEKABLE_INTERFACE_SENTINEL"

    def __init__(self, iterator) -> None:
        self.orig_itr = iter(iterator)
        self.local_obj = []
        self.local_itr = iter(local_obj)

    def peek(self):
        

    def next(self):
        val = next(self.local_itr, SENTINEL)
        if val != SENTINEL:
            return val
        
        val = next(self.orig_itr)
        return val

    def hasNext(self) -> bool:
        if hasNext(self.local_itr):
            return True
        
        return hasNext(self.orig_itr)


if __name__ == "__main__":
    list_ = [1,2,3,4,5,6]
    test = PeekableInterface(list_)
    