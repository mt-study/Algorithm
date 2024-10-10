"""
题目:https://leetcode.cn/problems/longest-substring-without-repeating-characters/?envType=study-plan-v2&envId=top-interview-150
完成时间：2024.10.10
解题思路：
心得：滑块窗口方法

"""


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    a=0
    b=1
    maxlength=1

    while b<len(s):
        if s[b] in s[a:b]:
            a+=1
        else:
            b+=1
            maxlength=max(maxlength,b-a)

    return maxlength
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))