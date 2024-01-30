import json
from typing import Any, Dict, Optional, Union

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def serialize(node: Node) -> str:
    ret = {"v": node.val, 
           "l": "", 
           "r": ""}
    if node.left is not None:
        ret["l"] = _serialize(node.left)
    if node.right is not None:
        ret["r"] = _serialize(node.right)
    return json.dumps(ret, indent=4)

def _serialize(node: Node) -> Dict[str, Any]:
    ret = {"v": node.val, 
           "l": "", 
           "r": ""}
    if node.left is not None:
        ret["l"] = _serialize(node.left)
    if node.right is not None:
        ret["r"] = _serialize(node.right)
    return ret

def deserialize(data: Union[str, Dict[str, Any]]) -> Optional[Node]:
    if isinstance(data, str):
        data = json.loads(data)

    if len(data) == 0:
        return None
    node = Node(data["v"], 
                deserialize(data["l"]) if data["l"] != "" else None,
                deserialize(data["r"]) if data["r"] != "" else None)
    return node

if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    string = serialize(node)
    assert deserialize(serialize(node)).left.left.val == 'left.left'
    print("success!")