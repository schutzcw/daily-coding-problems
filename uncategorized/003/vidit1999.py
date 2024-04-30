class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f'Node({repr(self.val)}, {repr(self.left)}, {repr(self.right)})'

serialize = repr
deserialize = eval

node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))
print(deserialize(serialize(node)).left.left.val == 'left.left')