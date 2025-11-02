Brute method-

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values == values[::-1]
    

optimal method-

class Solution:
    def isPalindrome(self, head):
        # Finding the middle of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #Reverse the second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        #Compare both halves
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True