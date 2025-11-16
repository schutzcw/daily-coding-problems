from typing import Generic, Optional, TypeVar
T = TypeVar("T")


class Node(Generic[T]):

    def __init__(self,
                 val: (T | None) = None, 
                 next: Optional["Node"] = None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"Node(val={self.val})"

class SinglyLinkedList(Generic[T]):
    
    def __init__(self, root: (Node[T] | None) = None) -> None:
        self._root = root
    
    def __repr__(self) -> str:
        return f"SinglyLinkedList(val={self._root.val})"
    
    def insert_front(self, val: T) -> None:
        tmp = self._root
        self._root = Node(val)
        self._root.next = tmp
    
    def insert_back(self, val: T) -> None:
        new_node = Node(val)
        if self._root is None:
            self._root = new_node
            return

        node = self._root
        while node.next is not None:
            node = node.next
        node.next = new_node
    
    def insert_at(self, index: int, val: T) -> None:
        if index == 0:
            self.insert_front(val)
            return

        prior_index = index - 1
        idx = 0
        node = self._root
        while idx < prior_index:
            if node is None:
                raise RuntimeError(f"Invalid index: {index}")
            node = node.next
            idx += 1

        if node is None:
            raise RuntimeError(f"Invalid index: {index}")

        new_node = Node(val)
        tmp = node.next
        node.next = new_node
        new_node.next = tmp

    def remove_front(self) -> (T | None):
        if self._root is None:
            return None
        temp = self._root
        self._root = self._root.next
        return temp.val

    def remove_back(self) -> (T | None):
        if self._root is None:
            return None

        node = self._root
        if node.next is None:
            self._root = None
            return node.val
     
        prev = node
        node = node.next
        while node.next is not None:
            prev = node
            node = node.next
        prev.next = None
        return node.val

    def remove_at(self, index: int) -> (T | None):
        if index < 0:
            raise RuntimeError("Index out of bounds")

        if index == 0:
            return self.remove_front()

        prev = self._root
        cur = self._root.next
        cur_idx = 1

        while cur_idx != index:
            if cur is None:
                raise RuntimeError("Index out of bounds")
            prev = cur
            cur = cur.next
            cur_idx += 1
        
        if cur is None:
            raise RuntimeError("Index out of bounds")
        
        prev.next = cur.next
        return cur.val

    def remove_value(self, val: T) -> int:
        """
        Remove the first occurrence of a given value

        Return (int): The index of the first occurrence if it exists, otherwise None.
        """
        if self._root is None:
            return None

        if self._root.val == val:
            self._root = self._root.next
            return 0
        
        prev = self._root
        cur = self._root.next
        idx = 1

        while cur is not None:
            if cur.val == val:
                prev.next = cur.next
                return idx
            prev = cur
            cur = cur.next
            idx += 1

        return None

    def get(self, index: int) -> T:
        if index < 0:
            raise RuntimeError("Index out of bounds")  
        cur_idx = 0
        cur = self._root
        while cur_idx < index:
            if cur is None:
                raise RuntimeError("Index out of bounds")
            cur_idx += 1
            cur = cur.next
        
        if cur is None:
            raise RuntimeError("Index out of bounds")
        return cur.val

    def find(self, val: T) -> (int | None):
        """Returns the index of the first occurrence of a value."""
        cur_idx = 0
        cur = self._root

        while cur is not None:
            if cur.val == val:
                return cur_idx
            cur = cur.next
            cur_idx += 1
        return None

    def size(self) -> int:
        sz = 0
        cur = self._root
        while cur is not None:
            cur = cur.next
            sz += 1
        return sz

    def is_empty(self) -> bool:
        return self._root is None

    def print(self) -> None:
        string = ""
        node = self._root
        while node.next is not None:
            string += f"{node.val} -> "
            node = node.next
        string += f"{node.val}"
        print(string if string != "" else "()")
    
    def to_array(self) -> list[T]:
        l = [None] * self.size()
        node = self._root
        for i in range(len(l)):
            l[i] = node.val
            node = node.next
        return l

    def reverse(self) -> None:
        if self._root is None:
            return

        prev = None
        node = self._root
        while node.next is not None:
            _next = node.next
            node.next = prev
            prev = node
            node = _next
        node.next = prev
        self._root = node


    def sort(self) -> None:
        pass

    def merge(self, other: "SinglyLinkedList") -> None:
        """Merges another SinglyLinkedList into this one"""
        pass

    def detect_cycle() -> bool:
        """Detect if there's a cycle in the linked list (Floyd's Cycle Detection Algorithm)"""
        pass

    def find_middle() -> Node[T]:
        """find the middle node"""
        pass


if __name__ == "__main__":
    sll = SinglyLinkedList[int]()
    sll.insert_back(1)
    sll.insert_back(2)
    sll.insert_back(3)
    sll.print()

    sll.insert_front(0)
    sll.print()

    sll.insert_back(6)
    sll.print()

    sll.insert_at(4,4)
    sll.print()
    sll.remove_front()
    sll.print()
    sll.remove_back()
    sll.print()
    sll.remove_at(3)
    sll.print()
    sll.remove_at(1)
    sll.print()
    sll.insert_back(1)
    sll.insert_back(2)
    sll.insert_back(3)
    sll.print()
    sll.remove_value(1)
    sll.print()
    sll.remove_value(2)
    sll.print()
    sll.remove_value(3)
    sll.print()
    sll.remove_value(3)
    sll.print()
    sll.insert_back(1)
    sll.insert_back(2)
    sll.insert_back(3)
    sll.insert_back(1)
    sll.insert_back(2)
    sll.insert_back(3)
    sll.print()
    print(sll.get(6))
    print(sll.get(0))
    print(sll.find(1))
    print(sll.find(7))
    sll.insert_back(4)
    sll.print()
    print(sll.find(4))
    print(sll.size())
    print(SinglyLinkedList().size())
    print(sll.to_array())
    sll.reverse()
    sll.print()
