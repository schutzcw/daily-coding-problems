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

class SinglyLinkedList(Node):
    pass


if __name__ == "__main__":
    sll = SinglyLinkedList(1, Node(2, Node(3, Node(4, Node(5)))))
    node = sll
    while node is not None:
        print(node.val)
        node = node.next
    print(sll)
    print(node)


