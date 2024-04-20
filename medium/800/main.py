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


def rearrange(linked_list: SinglyLinkedList) -> SinglyLinkedList:
    """ """
    node = linked_list
    while (node.next is not None) and (node.next.next is not None):
        lower = node.next
        higher = node.next.next
        lower.next = higher.next
        node.next = higher
        higher.next = lower
        node = lower
    return linked_list
    
    

def main() -> None:
    sll = SinglyLinkedList(1, Node(2, Node(3, Node(4, Node(5)))))
    node = rearrange(sll)
    while node is not None:
        print(node.val, end="->")
        node = node.next
    print("None")

    

if __name__ == "__main__":
    main()