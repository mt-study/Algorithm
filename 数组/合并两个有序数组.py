"""
题目：https://leetcode.cn/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
作者：Jack
完成时间：2024/11/4 09:31
解题思路：新建一个数组，防止覆盖
心得：
"""


def merge( nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    l=nums1[:m]

    a=0
    b=0

    mid=0

    while a<m or b<n:
        print(a,b)
        if a>=m:
            nums1[mid]=nums2[b]
            b+=1
            mid+=1
            continue
        if b>=n:
            nums1[mid]=l[a]
            a+=1
            mid+=1
            continue

        if l[a]<=nums2[b]:
            nums1[mid]=l[a]
            mid+=1
            a+=1
        elif l[a]>nums2[b]:
            nums1[mid]=nums2[b]
            mid+=1
            b+=1
    return nums1

print(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))