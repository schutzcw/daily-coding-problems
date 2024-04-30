from binary_tree import BinaryTree, Node, create_tree
from queue import Queue
from typing import Optional


class UnivalTree(BinaryTree[int]):
    
    def count_unival_top_down(self) -> int:
        """Does a root-down approach. A better approach would be to start with with the leaves and
        work your way up. There's a lot of repeated checks here.

        Returns:
            int: The unival count.
        """
        node_queue: Queue[int] = Queue()
        node_queue.put_nowait(self.root)
        count = 0
        while not node_queue.empty():
            node = node_queue.get()
            count += UnivalTree._is_unival(node)
            if node.left is not None:
                node_queue.put_nowait(node.left)
            if node.right is not None:
                node_queue.put_nowait(node.right)
        return count

    @staticmethod
    def _is_unival(tree: Optional[Node[int]] = None) -> int:
        """Check if a tree is unival or not.

        Args:
            tree (Node[int]): The root of the tree.

        Returns:
            int: 1 if the tree is unival. Else 0.
        """
        
        if tree is None:
            return 0
        
        if (tree.left is not None) and (tree.left.value != tree.value):
            return 0
        
        if (tree.right is not None) and (tree.right.value != tree.value):
            return 0
            
        LEFT = 1 if tree.left is None else UnivalTree._is_unival(tree.left)
        RIGHT = 1 if tree.right is None else UnivalTree._is_unival(tree.right)
    
        return min(LEFT, RIGHT)


    def count_unival_bottom_up(self) -> int:
        """Does a leaves up approach to checking if a tree is unival or not.

        Returns:
            int: The unival count.
        """
        leaves = self.get_leaves()
        queue = Queue()
        for leaf in leaves:
            queue.put_nowait(leaf)

        count = 0
        while not queue.empty():
            node = queue.get()
            if node is None:
                continue

            if node.is_leaf():
                node.unival = True
                queue.put_nowait(node.parent)
                count += 1
            elif not hasattr(node, "visited"):
                LEFT = node.left
                RIGHT = node.right
                VAL = node.value
                
                # have to wait for both child nodes to be explored. THis complicates things. I'm
                # just pushing to the back of the queue again for now.
                if not hasattr(LEFT, "unival") or not hasattr(RIGHT, "unival"):
                    queue.put_nowait(node)
                    continue

                node.visited = True
        
                LEFT_UNIVAL = (LEFT is None) or LEFT.unival
                RIGHT_UNIVAL = (RIGHT is None) or RIGHT.unival
                UNIVAL = LEFT_UNIVAL and RIGHT_UNIVAL and LEFT.value == VAL and RIGHT.value == VAL
                count += UNIVAL
                if UNIVAL:
                    node.unival = True
                    queue.put_nowait(node.parent)      
                else:
                    node.unival = False  
        
        return count
        

def create_test_tree() -> UnivalTree:

    n30: Node[int] = Node(1)
    n31: Node[int] = Node(1)
    n20: Node[int] = Node(1)
    n21: Node[int] = Node(0)

    n10: Node[int] = Node(1)
    n11: Node[int] = Node(0)

    n00: Node[int] = Node(0)

    n00.left = n10
    n00.right = n11

    n10.parent = n00

    n11.parent = n00
    n11.left = n20
    n11.right = n21

    n20.parent = n11
    n20.left = n30
    n20.right = n31

    n21.parent = n11

    n30.parent = n20
    n31.parent = n20

    return UnivalTree(root=n00, node_count=7, depth=4)
    
if __name__ == "__main__":

    tree = create_test_tree()
    tree.printTree()
    print(f"Unival Count: {tree.count_unival_top_down()}")
    print(f"Unival Count: {tree.count_unival_bottom_up()}")
    