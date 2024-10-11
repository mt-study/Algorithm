"""
题目:https://leetcode.cn/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150
完成时间：2024.10.11
解题思路：先排序，后合并
心得：

"""


def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    intervals=sorted(intervals)
    l=[]
    l.append(intervals[0])
    for i in range(1,len(intervals)):

        if intervals[i][0]>l[len(l)-1][1] :
            l.append(intervals[i])
        elif intervals[i][0]<l[len(l)-1][0] and intervals[i][1]<l[len(l)-1][0] :
            l.append(intervals[i])
        elif intervals[i][0]>l[len(l)-1][0]:
            if l[len(l)-1][1]<intervals[i][1]:
                l[len(l)-1][1]=intervals[i][1]
        if intervals[i][0]<=l[len(l)-1][0] and intervals[i][1]>=l[len(l)-1][0]:
            l[len(l)-1][0]=intervals[i][0]
            if intervals[i][1] > l[len(l) - 1][1]:
                l[len(l)-1][1]=intervals[i][1]

    return l

# print(merge([[1,4],[4,5]]))
# print(merge([[1,3],[2,6],[8,10],[15,18]]))
# print(merge([[1,4],[0,4]]))
# print(merge([[1,4],[0,1]]))
# print(merge([[1,4],[1,5]]))
# print(merge([[1,4],[2,3]]))
# print(merge([[1,4],[0,0]]))
# print(merge([[1,4],[0,1]]))
print(merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
print(merge([[1,3],[2,6],[8,10],[15,18]]))
