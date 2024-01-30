from binary_tree import create_tree, BinaryTree

from typing import List, Optional, TypeVar

T = TypeVar("T")


def get_cousins(tree: BinaryTree[T], value: int) -> Optional[List[T]]:
    """ Given a tree and a value, return the cousins in the tree of the value.

    Args:
        tree (BinaryTree): The tree to search over
        value (int): The value whose cousins we're looking for

    Returns:
        Optional[List[T]]: The list of cousins if any exist. If none exist, then return None.
    """

    if tree.root is None:
        print(None)
    
    if not tree.search(value):
        print(None)
    
    # Do a breadth first search and print all nodes in the nodes
    # list if the value is in the list
    nodes = [tree.root]
    while len(nodes) > 0:
        vals = [node.value for node in nodes]
        if value in vals:
            vals.remove(value)
            vals.sort()
            return vals
        new_nodes = []
        while len(nodes) > 0:
            node = nodes.pop()
            if node.left is not None:
                new_nodes.append(node.left)
            if node.right is not None:
                new_nodes.append(node.right)
        nodes = new_nodes
    return None


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

    tree.printTree(tree.root)
    print(tree.list())
    value = tree.random_value()
    print(f"random value: {value}")
    cousins = get_cousins(tree, value)
    print(f"cousins: {cousins}")

    # print(f"search(7): {tree.search(7)}")
    # print(f"search(6): {tree.search(6)}")
    # node = tree.find(1)
    # if node is not None:
    #     print(f"parent: {node.parent}")
    #     print(f"left: {node.left}")
    #     print(f"right: {node.right}")

if __name__ == "__main__":
    main()