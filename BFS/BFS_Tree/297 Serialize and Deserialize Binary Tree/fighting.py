# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        result = []

        def dfs(node):
            if node == None:
                result.append("N")
                return None
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(result)
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        

    def deserialize(self, data):
        values = data.split(",")

        self.i = 0
        def dfs():
            if values[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(values[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
        

# test = Codec()
# input1 = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7,  None, None)))
# print(test.deserialize(test.serialize(input1)))


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))