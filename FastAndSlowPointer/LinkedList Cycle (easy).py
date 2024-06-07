# /*class Node {
#   constructor(value, next = null) {
#     this.val = value;
#     this.next = next;
#   }
# }*/


def hasCycle(self, head):

	if self.head.next == None:
		return False

	slow = self.head
	fast = self.head.next

	while fast is not None or fast.next.next is not None :

		if slow == fast:
			return True
		else:
			pass
			
		slow = slow.next
		fast = fast.next.next


	return False

