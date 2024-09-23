"""
题目:https://leetcode.cn/problems/linked-list-cycle/?envType=study-plan-v2&envId=top-interview-150
完成时间：2024.9.12
解题思路：建立一个列表来存储已经访问过的指针，如果访问时，已经存在，则有环
心得：
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createLinkedListWithCycle(values, pos):
    if not values:
        return None

    nodes = [ListNode(val) for val in values]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:  # 如果 pos 是有效的索引，创建环
        nodes[-1].next = nodes[pos]

    return nodes[0]  # 返回头节点


# 创建链表 [3, 2, 0, -4] 并形成环
head1 = createLinkedListWithCycle([1], -1)
head2 = createLinkedListWithCycle([3,2,0,-4], 1)
head3 = createLinkedListWithCycle([1,2], 0)


# 判断链表是否有环
def hasCycle(head: ListNode) -> bool:
    #我的方法
    if head == None:
        return False
    l = []
    print(head.val)
    p = head
    l.append(head)
    while p.next != None:
        print(p.val)
        p = p.next
        if p in l:
            return True
        l.append(p)
    return False
    #gpt方法
    # if not head:
    #     return False
    #
    # slow = head
    # fast = head
    #
    # while fast and fast.next:
    #     slow = slow.next  # 慢指针走一步
    #     fast = fast.next.next  # 快指针走两步
    #
    #     if slow == fast:  # 如果两指针相遇，说明有环
    #         return True
    #
    # return False  # 如果快指针走到链表尾部，说明没有环


# 输出结果
print(hasCycle(head1))  # 输出: True
print(hasCycle(head2))  # 输出: True
print(hasCycle(head3))  # 输出: True
