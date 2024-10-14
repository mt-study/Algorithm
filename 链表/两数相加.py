"""
题目:https://leetcode.cn/problems/add-two-numbers/?envType=study-plan-v2&envId=top-interview-150
完成时间：2024.10.15
解题思路：暴力方法
心得：
这道题的关键就是进位，最后一位的处理，如果小于10那么不能进位，也就下一位不需要，反之添加为1.
这里的我的方法是在所有长度中都进行计算，也有的方法是，处理完了所有位数在进行判断，细细想来其实算法思想一致，自己的判断太冗余了
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def build_(l):
    head = ListNode(l[0])
    current = head
    for i in range(1, len(l)):
        current.next = ListNode(l[i])
        current = current.next
    return head

def addTwoNumbers( l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    current1=l1
    current2=l2
    t = current1.val + current2.val

    head=ListNode(t%10)
    current1 = current1.next
    current2 = current2.next
    current3=head
    if t>=10:
        current3.next=ListNode(int(t/10))
    else:
        if current1 or current2:
            current3.next=ListNode(int(t/10))
    current3=current3.next

    while current1 or  current2:
        if current1 and not current2:
            t=current1.val
        elif not current1 and current2:
            t=current2.val
        else:
            t= current1.val+current2.val
        m=t+current3.val
        # print(m%10)
        # current3.next = ListNode(int(m / 10))
        current3.val = m%10
        # current3 = current3.next

        if current1:
            current1=current1.next
        if current2:
            current2=current2.next
        if not current1 and not current2:
            print("ffff")
            print(m)
            if m>=10:
                print("dddd")
                current3.next = ListNode(int(m / 10))
                current3 = current3.next
            else:
                current3.next = None
        else:
            current3.next = ListNode(int(m / 10))
            current3 = current3.next
    p=head
    while p:
        print(p.val)
        p=p.next
    return head

# print(addTwoNumbers(build_([2,4,3]),build_([5,6,4])))
# print(addTwoNumbers(build_([0]),build_([0])))
# print(addTwoNumbers(build_([9,9,9,9,9,9,9]),build_([9,9,9,9])))
print(addTwoNumbers(build_([9,9,1]),build_([1])))
print(addTwoNumbers(build_([5]),build_([5])))