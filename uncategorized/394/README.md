Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given a binary tree and an integer k, return whether there exists a root-to-leaf path that sums up to k.

For example, given k = 18 and the following binary tree:

    8
   / \
  4   13
 / \   \
2   6   19
Return True since the path 8 -> 4 -> 6 sums to 18.



Start with root
20

If root.left is not none, "add_left" - add space to top level, add new line with forward dash

 20
/

"add_left" equivalent to the number of digits in the left node (i.e. 2 for 10):

   20
  /
 15
/

DFS(node):
    