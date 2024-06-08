# Problem: https://leetcode.com/problems/rotate-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head == None:
            return head
        
        ll_length = 0
        current = head

        while current is not None:
            ll_length +=1
            current = current.next


        # print(ll_length)
        # Getting the length to rotate the LL by
        len_rotate = k%ll_length
        
        
        current = head

        # Iterating over the LL to get the new head and new tail and storing them in separate variables
        for i in range(len_rotate):
            current = current.next

        new_tail = current
        new_head = current.next

        # print(new_head.val, new_tail.val)

        # Delinking the new tail
        new_tail.next = None

        # Creating a new variable curr to iterate over the LL from the new head to the new tail
        curr = new_head

        # print(self.head.val)

        for i in range(ll_length-1):
            if curr.next is None:
                curr.next = head

            curr = curr.next

        # Setting start pointer to the new head
        head = new_head

        return head
         