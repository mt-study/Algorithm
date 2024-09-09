"""
题目:https://leetcode.cn/problems/summary-ranges/description/?envType=study-plan-v2&envId=top-interview-150
解题思路：暴力破解
完成时间：24.9.9
心得：学会了python的入栈和出栈，pop和append操作

"""


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    l=[]
    u=['(',')','{','}','[',']']

    for i in s:
        if i in u[0::2]:
            l.append(i)
        elif i in u[1::2]:
            if len(l)==0:
                return False
            t=u[1::2].index(i)

            if l[len(l)-1]==u[0::2][t]:
                l.pop()
            else:
                return False
    if len(l)==0:
        return True
    else:
        return False
s = "(]"
print(isValid(s))

