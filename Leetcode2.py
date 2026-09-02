# l1 digit + l2 digit + carry
#             ↓
#           total
#             ↓
# total % 10  → answer digit
# total // 10 → next carry

# l1 = [2,4,3]
# l2 = [5,6,7]

# 2+5=7
# 4+6=10  digit 0, carry 1
# 3+4+1 = 8

# answer = [7,0,8]

class Solution:
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            digit = total % 10
            carry = total // 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next