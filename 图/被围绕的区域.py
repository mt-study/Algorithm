"""
题目：https://leetcode.cn/problems/surrounded-regions/?envType=study-plan-v2&envId=top-interview-150
作者：Jack
完成时间：2024/10/24 16:25
解题思路：
心得：
"""
board=[["X","X","X","X"],["X","0","0","X"],["X","X","0","X"],["X","0","X","X"]]

def dfs(board,i,j):
    if not 0<=i<len(board) or not 0<=j<len(board[0]) or board[i][j]!="0":
        return
    board[i][j]="B"
    pp=[[1,0],[0,1],[-1,0],[0,-1]]

    for p in pp:
        x=i+p[0]
        y=j+p[1]
        dfs(board,x,y)

def solve( board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    m=len(board)
    n=len(board[0])

    for i in range(m):
        dfs(board,i,0)
        dfs(board,i,n-1)
    for i in range(n):
        dfs(board,0,i)
        dfs(board,m-1,i)
    for i in range(m):
        for j in range(n):
            if board[i][j]=="B":
                board[i][j]="0"
            elif board[i][j]=='0':
                board[i][j]="X"
    return board



print(solve(board))
print(solve([["X","X","X","X"],["X","0","0","X"],["X","X","0","X"],["X","0","X","X"]]))
