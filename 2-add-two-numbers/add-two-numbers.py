class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = None
        tail = None

        while l1 or l2:
            x = 0
            y = 0

            if l1:
                x = l1.val
                l1 = l1.next

            if l2:
                y = l2.val
                l2 = l2.next

            total = x + y + carry
            carry = total // 10
            digit = total % 10

            node = ListNode(digit)

            if head is None:
                head = node
                tail = node
            else:
                tail.next = node
                tail = node

        if carry > 0:
            tail.next = ListNode(carry)

        return head
