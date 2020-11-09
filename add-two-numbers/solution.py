class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = ""
        while self is not None:
            s = s + str(self.val)
            self = self.next
        return s


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode)-> ListNode:
        l3 = None
        carry = 0
        while True:
            val = 0
            if l1 is None and l2 is None:
                if carry == 1:
                    node = ListNode(1)
                    temp = l3
                    while True:
                        if temp.next is None:
                            temp.next = node
                            break
                        temp = temp.next
                break
            if l1 is not None:
                val += l1.val
                l1 = l1.next
            if l2 is not None:
                val += l2.val
                l2 = l2.next
            val += carry
            if val >= 10:
                carry = 1
                val = val % 10
            else:
                carry = 0

            # new node goes to the end of the stack
            node = ListNode(val)
            temp = l3
            while True:
                if temp is None:
                    l3 = node
                    break
                elif temp.next is None:
                    temp.next = node
                    break
                temp = temp.next

        return l3
