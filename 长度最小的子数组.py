"""

题目:https://leetcode.cn/problems/minimum-size-subarray-sum/?envType=study-plan-v2&envId=top-interview-150
解题思路：
心得：

"""

#方法一:暴力破解

def minSubArrayLen1( target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    if sum(nums) < target:
        return 0
    else:
        lena= len(nums)
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if sum(nums[i:j+1]) >= target:
                    if len(nums[i:j+1])<=lena:
                        print(nums[i:j+1])
                        lena=len(nums[i:j+1])

    return lena
# 滑动窗口
def minSubArrayLen2( target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """

    if sum(nums) < target:
        return 0
    else:
        i = 0
        lena= len(nums)
        for j in range(len(nums)):
            while sum(nums[i:j+1])>=target:
                if len(nums[i:j+1])<lena:
                    lena=j-i+1
                i+=1
        return lena
print(minSubArrayLen2(7,[2,3,1,2,4,3]))

# 一举多得
# 
# ①无需回头
# ②一个尝试，一个侦查