"""
题目：https://leetcode.cn/problems/minimum-size-subarray-sum/description/?envType=study-plan-v2&envId=top-interview-150
作者：Jack
完成时间：2024/11/4 10:16
解题思路：用滑动窗口的，解决，如果总和大于等于，左边加一，总和减；相反右边加一，总和加
心得：
"""


def minSubArrayLen( target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """

    a=0
    b=0
    min_len=len(nums)+1

    sum=nums[a]

    while b<len(nums)-1 and a<len(nums)-1:

        # print(a,b)
        if sum<target :
            b+=1
            sum+=nums[b]
        else:
            if b-a+1<=min_len:
                min_len=b-a+1
            sum-=nums[a]
            a+=1

    # print(a,b)
    while sum>=target:
        if b - a + 1 <= min_len:
            min_len = b - a + 1
        sum-=nums[a]
        a+=1
    if min_len==len(nums)+1:
        return 0
    return min_len


print(minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))
print(minSubArrayLen(target = 4, nums = [1,4,4]))
print(minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))