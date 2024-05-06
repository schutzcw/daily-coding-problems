from typing import Optional, TypeVar
T = TypeVar("T")

class Node():
    def __init__(self,
                 val: (T | None) = None, 
                 next: Optional["Node"] = None) -> None:
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        return f"Node(val={self.val})"

    def print(self) -> None:
        string = ""
        node = self
        while node.next is not None:
            string += f"{node.val} -> "
            node = node.next
        string += f"{node.val}"
        print(string if string != "" else "()")

class SinglyLinkedList(Node):
    pass


if __name__ == "__main__":
    sll = SinglyLinkedList(1, Node(2, Node(3, Node(4, Node(5)))))
    sll.print()

