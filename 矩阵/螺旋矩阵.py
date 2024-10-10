"""
题目:https://leetcode.cn/problems/spiral-matrix/?envType=study-plan-v2&envId=top-interview-150
完成时间：2024.10.10
解题思路：暴力方法，先制定顺时针顺序，如果要走的节点已经被访问了，则拐弯。
心得：

"""


def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    m=len(matrix)
    n=len(matrix[0])
    flag=[[0] *n for _ in range(m)]
    print(flag)
    l=[]
    pp=[[0,1],[1,0],[0,-1],[-1,0]]
    i = 0
    j = 0
    h=[]
    count=0
    while count<m*n:
        print(count)
        for p in pp:
            if i==0 and j==0 and count==0:
                p
            else:
                i = i + p[0]
                j = j + p[1]
            while 0<=i<=m-1 and 0<=j<=n-1:
                if flag[i][j]:
                    break
                flag[i][j] = 1
                count+=1
                print(i,j)
                h.append(matrix[i][j])

                i = i + p[0]
                j = j + p[1]

                if i > m - 1 or i <0 :
                    i-=p[0]
                    break
                if j > n - 1 or j < 0:
                    j-=p[1]
                    break
                if flag[i][j]:
                    i-=p[0]
                    j-=p[1]
                    break

    return h

# print(spiralOrder(matrix=[[1,2,3],[4,5,6],[7,8,9]]))
print(spiralOrder(matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(spiralOrder(matrix=[[3],[2]]))