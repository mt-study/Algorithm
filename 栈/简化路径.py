"""
题目:https://leetcode.cn/problems/simplify-path/?envType=study-plan-v2&envId=top-interview-150
完成时间：2024.10.13
解题思路：栈的方法
心得：

"""


def simplifyPath(path):
    """
    :type path: str
    :rtype: str
    """
    l=[]
    paths=path.split('/')
    l.append('/')
    for i in range(len(paths)):
        if not paths[i]:
            continue
        if paths[i]=='..':
            l.pop()
            if len(l)==0:
                l.append('/')
                continue
            l.pop()
            continue
        if paths[i]=='.':
            continue
        l.append(paths[i])
        l.append('/')
    return ''.join(l) if len(l)==1 else ''.join(l[:-1])
print(simplifyPath("/home/"))
# print(simplifyPath("/home//foo/"))
# print(simplifyPath("/.../a/../b/c/../d/./"))
# print(simplifyPath("/home/user/Documents/../Pictures"))
print(simplifyPath("/../"))
print(simplifyPath("/a/../../b/../c//.//"))
