from copy import deepcopy
from typing import Generic, Optional, TypeVar, Union

T = TypeVar("T")



class Node(Generic[T]):
    val: T
    prev: "Node[T]"
    next: "Node[T]"

    def __init__(self,
                 val: T,
                 prev: Optional["Node[T]"] = None, 
                 next: Optional["Node[T]"] = None) -> None:
        self.val = val
        self.prev = prev
        self.next = next

    def __str__(self) -> str:
        _prev = "None" if self.prev is None else self.prev.val
        _next = "None" if self.next is None else self.next.val
        return f"Node(val={self.val}, prev={_prev}, next={_next})"



class DoublyLinkedList(Generic[T]):


    head = Optional[Node[T]]


    def __init__(self) -> None:
        self.head = None
        self.tail = None


    def add_back(self, node: Union[T, Node[T]]) -> None:
        """Add the node to the back of the DoublyLinkedList

        Args:
            node (Union[T, Node[T]]): The node, or value, that we want to add to the back of the
                list.
        """
        if not isinstance(node, Node):
            node = Node(node)
        
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def add_front(self, node: Union[T, Node[T]]) -> None:
        """Add the node to the front of the DoublyLinkedList

        Args:
            node (Union[T, Node[T]]): The node, or value, that we want to add to the front of the
                list.
        """

        if not isinstance(node, Node):
            node = Node(node)

        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node


    def is_empty(self) -> bool:
        """Check if the DoublyLinkedList is empty.

        Returns:
            bool: True is the list is empty.
        """
        return self.head is None

    def size(self) -> int:
        if self.is_empty():
            return 0

        size = 1
        head = self.head
        while head.next is not None:
            size +=1 
            head = head.next
        return size


    def __str__(self) -> str:
        """String representation of the DoublyLinkedList

        Returns:
            str: The representation of the DoublyLinkedList
        """
        result = []
        node = self.head
        while node:
            result.append(str(node.val))
            node = node.next
        return ' <-> '.join(result)


    def remove_first(self, node: Union[T, Node[T]]) -> bool:
        """Remove the first node in the list that matches `node`'s value

        Args:
            node (Union[T, Node[T]]): The node or node value to remove.

        Returns:
            bool: True if a node was removed. Otherwise False.
        """
        if isinstance(node, Node):
            val = node.val
        else:
            val = node
        
        if self.head.val == val:
            self.head.next.prev = None
            self.head = self.head.next
            return True

        node = self.head.next
        while node is not None:
            if node.val == val:
                node.prev.next = node.next
                if node.next is not None:
                    node.next.prev = node.prev
                return True

        return False


    def remove_last(self, node: Union[T, Node[T]]) -> bool:
        """Remove the last node in the list that matches `node`'s value

        Args:
            node (Union[T, Node[T]]): The node or node value to remove.

        Returns:
            bool: True if a node was removed. Otherwise False.
        """
        raise NotImplementedError()


    @classmethod
    def create_list(cls, num: int, seed: Optional[int] = None) -> "DoublyLinkedList[int]":
        import random
        import time

        if seed is None:
            seed = int(time.time())
        print(f"seed: {seed}")
        random.seed(seed)

        dll = cls()
        for _ in range(num):
            dll.add_back(random.randrange(0,100))
        return dll


if __name__ == "__main__":
    dll = DoublyLinkedList.create_list(10)
    print(dll)
