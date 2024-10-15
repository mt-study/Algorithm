"""
题目:https://leetcode.cn/problems/average-of-levels-in-binary-tree/submissions/572870816/?envType=study-plan-v2&envId=top-interview-150
完成时间：2024.10.15
解题思路：弄一个字典保存每一层的数
心得：
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def build_(arr,index=0):
    if index>=len(arr) or arr[index]==None:
        return None

    root = TreeNode(arr[index])

    root.left = build_(arr,2*index+1)
    root.right = build_(arr,2*index+2)

    return root
def averageOfLevels( root):
    """
    :type root: TreeNode
    :rtype: List[float]
    """
    d={}
    def get_sum(root,l):
        if not root:
            return 0
        if not d.get(l):
            d[l]=[]
            d[l].append(root.val)

        else:
            d[l].append(root.val)
        get_sum(root.left,l+1)
        get_sum(root.right,l+1)
    get_sum(root,0)
    l=[]
    for i in d.items():
        l.append(sum(i[1])/len(i[1]))
    print(d)
    print(l)
    return l
root = [3,9,20,None,None,15,7]
p=build_(root)
print(averageOfLevels(p))