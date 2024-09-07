"""
题目:https://leetcode.cn/problems/summary-ranges/description/?envType=study-plan-v2&envId=top-interview-150
解题思路：暴力破解
完成时间：24.9.7
心得：利用双指针，一个保存开始，一个保存结束，如果和后面的数值不连续，那么将会以下一个作为开始充值m 和 n的值

"""


def summaryRanges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    if len(nums) == 0:
        return []
    l = []
    m = 0
    n = 0
    nums.append(nums[-1])
    for i in range(len(nums)-1):
        if nums[i] + 1 != nums[i + 1]:
            if m == n:
                l.append(str(nums[m]))
            else:
                l.append(str(nums[n])+'->'+str(nums[m]))
            m = i + 1
            n = i + 1
        else:
            m += 1
    return l


print([0, 1, 2, 4, 5, 7])
print(summaryRanges([0, 1, 2, 4, 5, 7]))
print(summaryRanges([0,2,3,4,6,8,9]))

