"""
题目：https://leetcode.cn/problems/kth-smallest-element-in-a-bst/?envType=study-plan-v2&envId=top-interview-150
作者：Jack
完成时间：2024/10/24 10:01
解题思路：利用到了中序遍历，也用到了栈的思想，访问左节点，然后左节点没有出栈，出栈节点查看是否是制定大小的数值，然后再入栈这个节点的右节点
心得：
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_(root,index=0):
    if index>len(root)-1:
        return None

    node=TreeNode(root[index])
    node.left=build_(root,2*index+1)
    node.right=build_(root,2*index+2)

    return node
def kthSmallest(root, k):
    """
    :type root: Optional[TreeNode]
    :type k: int
    :rtype: int
    """
    l=[]

    while root or l:

        while root:
            l.append(root)
            root=root.left
        root=l.pop()
        k-=1

        if k==0:
            return root.val

        root=root.right

print(kthSmallest(build_([5,3,6,2,4,None,None,1]),3))
# print(kthSmallest(build_([3,1,4,None,2]),1))