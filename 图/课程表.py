"""
题目:https://leetcode.cn/problems/course-schedule/description/?envType=study-plan-v2&envId=top-interview-150
完成时间：2024.9.25
解题思路：这道题，根本不是判断能不能完成课程数目，只是判断，有没有遗漏的不能进行学习的，如果都可以进行学习，直接返回true，否则是false
心得：

"""


def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    if prerequisites == []:
        return True
    dict={}
    for i in prerequisites:

        if i[1] not in dict:
            dict[i[1]]=0
        if i[0] not in dict:
            dict[i[0]]=1
        else:
            dict[i[0]]+=1

    l=[]
    count=0
    for k,v in dict.items():
        if v==0:
            l.append(k)
    while len(l)>0:
        t=l.pop(0)
        dict.pop(t)
        count+=1
        for j in prerequisites:
            if t==j[1]:
                dict[j[0]]-=1
        for k, v in dict.items():
            if v == 0 and k not in l:
                l.append(k)
    print(prerequisites)
    print(count)
    print(numCourses)
    if len(dict)==0:
        return True
    else:
        return False
    return count == numCourses
print(canFinish(2,[[1,2],[1,4],[4,3],[2,3],[2,5],[3,5],[4,5]]))
print(canFinish(2,[[1,0]]))
print(canFinish(2,[[1,0],[0,1]]))
print(canFinish(1,[]))
print(canFinish(5,[[1,4],[2,4],[3,1],[3,2]]))