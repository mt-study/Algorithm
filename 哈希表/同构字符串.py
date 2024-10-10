"""
题目:https://leetcode.cn/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150
完成时间：2024.10.11
解题思路：定义一个字典，用来存储对应关系，如果遇到没有存储的键，用来判断值是不是已经和其他键进行了匹配，如果匹配就直接返回错误
心得：

"""


def isIsomorphic( s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    d={}
    for i in range(len(s)):
        if not d.get(s[i]):
            if t[i] in d.values():
                return False
            d[s[i]] = t[i]
        else:
            if d[s[i]] != t[i]:
                return False

    return True



# print(isIsomorphic('abcd', 'abcd'))
# print(isIsomorphic('egg', 'add'))
# print(isIsomorphic('foo', 'bar'))
# print(isIsomorphic('paper', 'title'))
print(isIsomorphic('badc', 'baba'))