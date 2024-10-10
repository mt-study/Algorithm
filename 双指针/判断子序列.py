"""
题目:https://leetcode.cn/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150
完成时间：2024.10.10
解题思路：快慢指针方法
心得：

"""


def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if not s:
        return True
    a=0
    b=0
    while a<len(s) and b<len(t):

        if s[a] == t[b]:
            a += 1
            b += 1
        else:
            b+=1
        if a==len(s):
            return True
    return False

print(isSubsequence("axc", "ahbgdc"))
print(isSubsequence("", "ahbgdc"))