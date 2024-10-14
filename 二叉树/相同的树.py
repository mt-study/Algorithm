"""
题目:https://leetcode.cn/problems/same-tree/?envType=study-plan-v2&envId=top-interview-150
完成时间：2024.10.14
解题思路：直接无敌嵌套递归
心得：
"""
class LinkNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bulid_(arr,index=0):

    if index>=len(arr) :
        return None
    root=LinkNode(arr)

    root.left=bulid_(arr,2*index+1)
    root.right=bulid_(arr,2*index+2)

    return root


def isSameTree(p,q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if not p and not q:
        return True
    if not p and  q:
        return False
    if p and not q:
        return False
    if not p.left and p.left:
        return False
    if not p.right and p.right:
        return False
    if p.val!=q.val:
        return False
    return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)

print(isSameTree(bulid_([1,2,1]),bulid_([1,1,3])))