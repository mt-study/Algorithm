"""
题目:https://leetcode.cn/problems/minimum-absolute-difference-in-bst/description/?envType=study-plan-v2&envId=top-interview-150
完成时间：2024.9.23
解题思路：暴力破解法，先遍历获取所有数据，后排序，后计算
心得：
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def insert_into_bst(root: TreeNode, val: int) -> TreeNode:
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root
def Preorder_traversal(root):
    if not root:
        return []
    if not root.left and not root.right:
        return [root.val]
    l = Preorder_traversal(root.left)
    r = Preorder_traversal(root.right)
    return [root.val]+l+r
def getMinimumDifference(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    p=Preorder_traversal(root)
    p.sort()
    min=abs(p[0]-p[1])
    for i in range(len(p)-2):
        if abs(p[i]-p[i+1])<min:
            min=abs(p[i]-p[i+1])
    return min
    print(getnode(root))

values = [4, 2, 6, 1, 3]
root = None
for value in values:
    root = insert_into_bst(root, value)
print(getMinimumDifference(root))
