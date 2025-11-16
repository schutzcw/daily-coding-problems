import math


class Quack():

    def __init__(self):
        self.front = []
        self.back  = []
        self.tmp   = []

    def push(self, val: int) -> None:
        """add a new item x to the left end of the list"""
        # add to the top of back stack
        self.front.append(val)

    def pop(self) -> int:
        """remove and return the item on the left end of the list"""
        if self.length() == 0:
            return None

        if len(self.front) > 0:
            return self.front.pop()

        if self.length() == 1:
            return self.back.pop()

        self._split(self.back, self.front)
        return self.front.pop()


    def pull(self) -> int:
        """remove the item on the right end of the list."""
        if self.length() == 0:
            return None

        if len(self.back) > 0:
            return self.back.pop()

        self._split(self.front, self.back)
        return self.back.pop()

    def print(self) -> None:
        for i in self.front[::-1]:
            print(i)
        for i in self.back:
            print(i)

    def length(self) -> int:
        return len(self.front) + len(self.back)

    def _debug(self) -> list[int]:
        return self.front[::-1] + self.back

    def _debug_print(self) -> None:
        print(20*"-")
        print(f"self.front: {self.front}")
        print(f"self.back: {self.back}")
        print(f"self.tmp: {self.tmp}")
        print(20*"-")

    def _split(self, src, dst) -> None:
        """ """
        if self.length() == 1:
            dst.append(src.pop())
            return

        num = math.ceil(len(src)/2)
        for _ in range(num):
            self.tmp.append(src.pop())
        for _ in range(len(src)):
            dst.append(src.pop())
        for _ in range(len(self.tmp)):
            src.append(self.tmp.pop())


def pop_test():
    q = Quack()
    q.push(1) # [1]
    q.push(2) # [2, 1]
    q.push(3) # [3, 2, 1]
    q.push(4) # [4, 3, 2, 1]
    q.push(5) # [5, 4, 3, 2, 1]
    q.push(6) # [6, 5, 4, 3, 2, 1]
    assert q._debug() == [6, 5, 4, 3, 2, 1]
    assert q.pop() == 6
    assert q.pop() == 5
    assert q.pop() == 4
    assert q.pop() == 3
    assert q.pop() == 2
    assert q.pop() == 1
    assert q.pop() is None

def pull_test():
    q = Quack()
    q.push(1) # [1]
    q.push(2) # [2, 1]
    q.push(3) # [3, 2, 1]
    q.push(4) # [4, 3, 2, 1]
    q.push(5) # [5, 4, 3, 2, 1]
    q.push(6) # [6, 5, 4, 3, 2, 1]
    assert q._debug() == [6, 5, 4, 3, 2, 1]
    assert q.pull() == 1
    assert q.pull() == 2
    assert q.pull() == 3
    assert q.pull() == 4
    assert q.pull() == 5
    assert q.pull() == 6
    assert q.pull() is None

def pull_pop_test():
    q = Quack()
    q.push(1) # [1]
    q.push(2) # [2, 1]
    q.push(3) # [3, 2, 1]
    q.push(4) # [4, 3, 2, 1]
    q.push(5) # [5, 4, 3, 2, 1]
    q.push(6) # [6, 5, 4, 3, 2, 1]
    q.push(7) # [6, 5, 4, 3, 2, 1]
    assert q._debug() == [7, 6, 5, 4, 3, 2, 1]
    assert q.pull() == 1 # [7, 6, 5, 4, 3, 2]
    assert q.pop()  == 7 # [6, 5, 4, 3, 2]
    assert q.pull() == 2 # [6, 5, 4, 3]
    assert q.pop()  == 6 # [5, 4, 3]
    assert q.pull() == 3 # [5, 4]
    assert q.pop()  == 5 # [4]
    assert q.pull() == 4
    assert q.pop() is None


def main() -> None:
    """
    description

    :param name:
    :return
    """

    print("pop_test")
    pop_test()
    print("pull_test")
    pull_test()
    print("pull_pop_test")
    pull_pop_test()

if __name__ == "__main__":
    main()
