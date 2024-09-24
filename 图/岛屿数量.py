"""
题目:https://leetcode.cn/problems/number-of-islands/description/?envType=study-plan-v2&envId=top-interview-150
完成时间：2024.9.24
解题思路：抄写的，官网，这里用到了dfs，这里的算法思想就是，一块一块访问，遇到新1就是新岛屿，将访问过的岛屿改为0，防止后面修改
心得：

"""
def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    def dfs(grid, i, j):
        grid[i][j] = 0
        dir=[[1,0],[0,1],[-1,0],[0,-1]]

        for d in dir:
            a=i+d[0]
            b=j+d[1]
            if 0<=a<len(grid) and 0<=b<len(grid[0]):
                if grid[a][b]=='1':
                    dfs(grid, a, b)
    count=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]=='1':
                dfs(grid,i,j)
                count+=1
            print(grid[i][j],end=" ")
        print()
    return count
print(numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
print(numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))