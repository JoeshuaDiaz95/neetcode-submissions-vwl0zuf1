# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        #save the first node
        dummynode = ListNode()
        dummynode.next = head

        fast = head
        slow = head

        #get the middle node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #need to reverse the second half of the list and cut off the first half
        prev = None
        curr = slow.next
        slow.next = None  # Cut off first half

        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # need to concatenate the two linked list and return dummnode.next
        first = head
        second = prev

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
