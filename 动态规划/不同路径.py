"""
题目:https://leetcode.cn/problems/unique-paths/
解题思路：逆着来的,当x或者y等于1的时候，只有一个方法了，不得不是1
心得：构建递归，f(n)和f(n-1)的关系
"""
# x走1步或者y走1步
def f(x,y):
    print(x,y)
    if y==1:
        print("y==1")
        return 1
    if x==1:
        print("x==1")
        return 1
    return f(x-1,y)+f(x,y-1)
print(f(7,3))




