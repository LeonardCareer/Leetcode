# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder2(self, root: TreeNode) -> list[list[int]]:
        result = []
        from collections import deque
        q = deque()
        q.append(root)

        while q:
            level = []
            length = len(q)
            for i in range(length):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.append(level)
        return result


    def levelOrder(self, root: list[TreeNode]) -> list[list[int]]:
        next_level = []
        if root:
            next_level.append(root)
        result = []
        while next_level:
            values = [x.val for x in next_level]
            result.append(values)
            temp = []
            for x in next_level:
                if x.left != None:
                    temp.append(x.left)
                if x.right != None:
                    temp.append(x.right)
            next_level = temp
        return result


test = Solution()
input1 = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7,  None, None)))
print(test.levelOrder2(input1))