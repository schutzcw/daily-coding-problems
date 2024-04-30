from binary_tree import create_tree, BinaryTree
from queue import Queue
from typing import TypeVar


T = TypeVar("T")


def second_largest(tree: BinaryTree[T]) -> T:
    """Given a binary tree, print the second largest value

    Args:
        tree (BinaryTree[T]): The binary tree to search

    Returns:
        T: The second largest value
    """

    que = Queue()
    que.put(tree.root)
    max_val = None
    second_max_val = None
    while not que.empty():
        node = que.get()
        if (max_val is None) or (node.value >= max_val):
            second_max_val = max_val
            max_val = node.value
        elif (second_max_val is None) or (node.value > second_max_val):
           second_max_val = node.value

        if node.left is not None:
            que.put(node.left)
        if node.right is not None:
            que.put(node.right)
    
    print(f"Max value: {max_val}")
    print(f"Second max value: {second_max_val}")
    return second_largest


def main():
    """ """

    seed = -1
    import random
    import time
    if seed == -1:
        seed = int(time.time())
        print(f"seed: {seed}")
        random.seed(seed)
    else:
        random.seed(seed)

    tree = create_tree(40)

    tree.printTree(extra=False)
    second_largest(tree)

    _list = tree.list()
    _list.sort(reverse=True)
    print(_list)


if __name__ == "__main__":
    main()
