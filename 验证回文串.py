"""

题目:https://leetcode.cn/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150
解题思路：a-z 97 122
        0-9 48 57
        从后往前和从前往后
心得：


"""
def get(s,n):
    while True:
        if not ((ord(s[n])>=97 and ord(s[n])<=122) or (ord(s[n])>=48 and ord(s[n])<=57)):
            n-=1
        else:
            return n

def isPalindrome(s):
    s=s.lower()
    s=list(s)
    n=len(s)-1
    for i in range(len(s)):
        # if s[i] (ord(a)>=97 and ord(a)<=122) or (ord(a)>=48 and ord(a)<=57)
        if i==n:
            return True
        if not ((ord(s[i])>=97 and ord(s[i])<=122) or (ord(s[i])>=48 and ord(s[i])<=57)):
            continue
        n=get(s,n)
        if s[i]==s[n]:
            n-=1
        else:
            return False
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))

print(ord('0'))
print(ord('9'))
print(ord('a'))
print(ord('z'))
print(s[2])
