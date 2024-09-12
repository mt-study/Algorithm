"""
题目:https://leetcode.cn/problems/maximum-depth-of-binary-tree/?envType=study-plan-v2&envId=top-interview-150
完成时间：2024.9.12
解题思路：递推算法，出口是节点不存在
心得：如何去构建一个二叉树是重中之重，但是此题没有思路，gpt的代码，需要重新写以后
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def gettree(data):
    """
    type root: TreeNode
    rtype: int
    """
    root=TreeNode(data[0])
    a=[root]
    i=1
    while i<len(data):
        node=a.pop(0)
        if data[i] is not None:
            node.left=TreeNode(data[i])
            a.append(node.left)
        i+=1
        if data[i] is not None:
            node.right=TreeNode(data[i])
            a.append(node.right)
        i+=1
    return root

def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    return max(maxDepth(root.left),maxDepth(root.right))+1
print(maxDepth(gettree([3,9,20,None,None,15,7])))

