"""
题目:https://leetcode.cn/problems/valid-sudoku/description/?envType=study-plan-v2&envId=top-interview-150
解题思路：暴力破解
完成时间：24.9.5
心得：最重要的是九宫格条件的学习

"""


def isValidSudoku(board):
    t = [[[], [], []],
         [[], [], []],
         [[], [], []]]
    for i in range(9):
        p = []
        m = []
        for j in range(9):
            if board[i][j] in t[int(i / 3)][int(j / 3)] and board[i][j] != '.':
                return False
            else:
                t[int(i / 3)][int(j / 3)].append(board[i][j])
            if board[i][j] in p and board[i][j] != '.':
                return False
            else:
                p.append(board[i][j])
            if board[j][i] in m and board[j][i] != '.':
                return False
            else:
                m.append(board[j][i])
    return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(isValidSudoku(board))
