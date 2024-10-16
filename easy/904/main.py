from typing import List, Tuple

import queue
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
data_structures_dir = os.path.abspath(os.path.join(current_dir, '../../data_structures'))
sys.path.append(data_structures_dir)

# Now you can import the module
from binary_tree import create_tree

def main():
    tree = create_tree(15)
    tree.printTree()

    q = queue.Queue()
    print(f"q.put({tree.root})")
    q.put(tree.root)
    while not q.empty():
        node = q.get()
        print(f"\tq.get() = {node}")
        children = []
        if node.left is not None:
            children.append(node.left)
        if node.right is not None:
            children.append(node.right)
        if len(children) == 0 and q.empty():
            print("HERE")
            print(node)
            sys.exit(0)
        else:
            for child in children:
                q.put(child)
                print(f"q.put({child})")
    

if __name__ == "__main__":
    main()