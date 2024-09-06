"""
题目:https://leetcode.cn/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150
解题思路：暴力破解
完成时间：24.9.6
心得：学习列表删除操作，以及列表元素统计

"""
import collections

def canConstruct( ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    # 我的算法

    magazine =list(magazine)

    for s in ransomNote:
        if s not in magazine:
            return False
        magazine.remove(s)
    return True
# 官方算法
    # if len(ransomNote) > len(magazine):
    #     return False
    # return not collections.Counter(ransomNote) - collections.Counter(magazine)

ransomNote = "aa"
magazine = "ab"

print(canConstruct(ransomNote, magazine))