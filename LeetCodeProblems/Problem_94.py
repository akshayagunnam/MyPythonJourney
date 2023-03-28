#Given the root of a binary tree, return the inorder traversal of its nodes' values.
class Solution:
        def inorderTraversal (self, root: Optional [TreeNode]) -> List[int]:
            def left (node) :
                while node:
                    yield node
                    node = node.left
            stack = list (left (root))
            while node := stack.pop () if stack else None:
                yield node.val
                stack += left (node.right)
            return stack
