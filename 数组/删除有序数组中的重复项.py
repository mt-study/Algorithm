"""
题目:https://leetcode.cn/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
完成时间：2024.10.10
解题思路：暴力方法
心得：

"""
from xoscar.metrics.backends.console.console_metric import Counter


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    p=0
    for i in range(len(nums)):

        if i-p < len(nums)-p:
            if nums[i-p] in nums[:i-p]:
                nums.remove(nums[i-p])
                p+=1
                nums.append(0)
    return len(nums)-p


print(removeDuplicates(nums = [1,1,2]))
print(removeDuplicates(nums =[0,0,1,1,1,2,2,3,3,4]))