# TODO: Work on testing random trees
# TODO: Create a recursive solution
# TODO: You can improve the run time by adding an if statement that checks 
#       whether or not a right/left child should even be added in the first place...

from binary_tree import create_tree, BinaryTree, Node
from queue import Queue
from typing import NamedTuple, TypeVar


T = TypeVar("T")


class MinMax(NamedTuple):
    """Encapsulates bottom view info"""
    min: int
    max: int


def sum_range(tree: BinaryTree[T], min_max: MinMax) -> T:
    """_summary_

    Args:
        tree (BinaryTree[T]): The tree that were investigating.
        min_max (MinMax): The min and max values in range

    Returns:
        T: The sum of all nodes in `tree` whose values in the range [min, max]
    """

    if tree.is_empty():
        return 0

    que = Queue()
    que.put(tree.root)
    _sum = 0
    while not que.empty():
        node = que.get()
        if (min_max.min <= node.value) and (node.value <= min_max.max):
            _sum += node.value
        if node.left is not None:
            que.put(node.left)
        if node.right is not None:
            que.put(node.right)
    print(f"Sum in range [{min_max.min},{min_max.max}]: {_sum}")
    return _sum



def test_case():
    """ Run test case provided by problem. """
    bt = BinaryTree()
    vals = [5, 3, 8, 2, 4, 6, 10]
    for v in vals:
        bt.add(v)
    bt.printTree(extra=False)

    sum_range(bt, MinMax(4,9))


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
    
    # TODO: Generate random min and max
    sum_range(tree, MinMax(4,9))


if __name__ == "__main__":
    test_case()
    #main()