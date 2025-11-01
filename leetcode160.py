class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen=set()
        a=headA
        b=headB
        while a:
            seen.add(a)
            a=a.next
        while b:
            if b in seen:
                return b
            b=b.next
        return None
      
         