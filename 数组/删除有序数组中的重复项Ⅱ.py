"""
题目：https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
作者：Jack
完成时间：2024/10/28 08:56
解题思路：解此题，关键就是定义三个指针，一个指针用来写，两个指针用来划定范围。这里的关键点其实就是边界判定。
        我这里一共是将 列表 倒数第二个长度作为结束的。这里一共有两种情况，如果最后一位的话，最后一位是重复的还是新的，如果是重复的，那么就减一 否则减二
心得：用时一上午
"""

def removeDuplicates( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a,b,c=0,0,0
    m=0
    while c<len(nums) and a<=c:
        while nums[c]==nums[b] and c<len(nums)-1:
            c+=1
        if c-b<=1:
            nums[a]=nums[b]
            a+=1
        elif c-b>=2:
            nums[a]=nums[b]
            a+=1
            nums[a]=nums[b]
            a+=1
            # m=m+c-b-2
            if c==len(nums)-1 and nums[c]==nums[b] :
                m=m+c-b-1
            else:
                m=m+c-b-2
        b=c
    print(nums)
    return len(nums)-m
# print(removeDuplicates([1,1,1,2,2,3]))
print(removeDuplicates([0,0,1,1,1,1,2,3,3]))
# print(removeDuplicates([1,1,1]))
print(removeDuplicates([1,1,2]))
print(removeDuplicates([1,1,1,1]))

