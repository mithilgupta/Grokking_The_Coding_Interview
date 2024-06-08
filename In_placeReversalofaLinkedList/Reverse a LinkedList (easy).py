# Reverse a LL
def reverse(self):

	prev = None
	current = self.head
	next = None


	while current is not None:

		# getting the next element in the list
		next = current.next

		# Linking the pointer from current to previous
		current.next = prev

		# Moving previous to current
		prev = current

		# moving current to next
		current = next


	print(prev.val)

	self.head = prev