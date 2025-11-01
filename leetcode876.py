class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length=0
        curr1=head
        while curr1:
            length=length+1
            curr1=curr1.next
        middle=length//2
        curr=head
        while middle!=0:
            middle-=1
            curr=curr.next
        return curr


        