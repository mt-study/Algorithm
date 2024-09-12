"""
题目:https://leetcode.cn/problems/binary-tree-right-side-view/?envType=study-plan-v2&envId=top-interview-150
完成时间：2024.9.12
解题思路：抄写的，层比遍历
心得：啊啊啊，好难
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
def rightSideView(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root :
        return []
    q = []
    q.append(root)
    l=[]
    t=[]
    l.append(root.val)
    while q:
        a=len(q)
        for i in range(a):
            m=q.pop(0)
            if i==a-1:
                t.append(m.val)
            if  m.left:
                q.append(m.left)
            if  m.right:
                q.append(m.right)
    return t
print(rightSideView(gettree([1,2,3,None,5,None,4])))
print(rightSideView(gettree([1,2,None])))
print(rightSideView(gettree([1,2,3,4,None,None,None])))
print(rightSideView(gettree([1,None,3])))
# print(rightSideView(gettree([])))