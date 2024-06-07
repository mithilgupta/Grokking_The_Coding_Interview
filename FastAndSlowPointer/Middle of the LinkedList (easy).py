#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next

def findMiddle(self):

	slow, fast = self.head, self.head

	while fast is not None and fast.next is not None:
		slow = slow.next
		fast = fast.next.next


	return slow.val