from binary_tree import create_tree, BinaryTree, Node
from queue import Queue
from typing import Dict, List, NamedTuple, TypeVar


T = TypeVar("T")


class BVNode(NamedTuple):
    """Encapsulates bottom view info"""
    node: Node
    distance: int   # bottom view distance


def bottom_view(tree: BinaryTree[T]) -> List[T]:
    """_summary_

    Args:
        tree (BinaryTree[T]): _description_

    Returns:
        List[T]: _description_
    """

    if tree.root is None:
        return []

    bv_map: Dict[int, Node] = {}
    que = Queue()
    que.put(BVNode(tree.root, 0))
    while not que.empty():
        bvn = que.get()
        bv_map[bvn.distance] = bvn.node
        if bvn.node.left is not None:
            que.put(BVNode(bvn.node.left, bvn.distance - 1))
        if bvn.node.right is not None:
            que.put(BVNode(bvn.node.right, bvn.distance + 1))

    bottom_view = [bv_map[k].value for k in bv_map]
    bottom_view.sort()
    print(bottom_view)


def test_case():
    """ Run test case provided by problem. """
    bt = BinaryTree()
    vals = [5, 3, 7, 1, 4, 6, 9, 0, 8]
    for v in vals:
        bt.add(v)
    bt.printTree(extra=False)

    bottom_view(bt)


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
    bottom_view(tree)


if __name__ == "__main__":
    #test_case()
    main()