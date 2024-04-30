from singly_linked_list import Node, SinglyLinkedList
from typing import List


"""
NOTES: Can improve by using a dummy head node and then returning dummy.next. This
simplifies the logic and you don't have to maintain the list... You can also make carry
another OR condition in the while loop to simplify. There's also a divmod() function if
you want to leverage that...
"""
def add(list1: SinglyLinkedList, list2: SinglyLinkedList) -> SinglyLinkedList:
    """Add and return new singly linked list"""
    carry = 0
    nodes: List[Node] = []
    while (list1 is not None) or (list2 is not None):
        val1 = 0 if list1 is None else list1.val
        val2 = 0 if list2 is None else list2.val
        val = val1 + val2 + carry
        carry = int(val / 10)
        nodes.append(Node(val % 10))
        
        list1 = list1 if list1 is None else list1.next
        list2 = list2 if list2 is None else list2.next

    if carry > 0:
        nodes.append(Node(carry))

    for idx, node in enumerate(nodes):
        if (idx + 1) != len(nodes):
            node.next = nodes[idx+1]
    return nodes[0]


def main():
    print("Example 1:")
    sll1 = SinglyLinkedList(9, Node(9))
    sll1.print()
    sll2 = SinglyLinkedList(5, Node(2))
    sll2.print()
    result = add(sll1, sll2)
    result.print()

    print("Example 2:")
    sll1 = SinglyLinkedList(1)
    sll1.print()
    sll2 = SinglyLinkedList(9, Node(9))
    sll2.print()
    result = add(sll1, sll2)
    result.print()

if __name__ == "__main__":
    main()