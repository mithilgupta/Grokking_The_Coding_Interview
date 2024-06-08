# I have an approach for N^2 time complexity. Using 2 while loops.
def findCycleStart(self):  

	# slow = self.head
	fast = self.head

	cnt = 0

	while fast is not None and cnt < 30:
		fast = fast.next
		cnt +=1
		# print(fast.val)

		slow = self.head

		# print("slow:")
		while slow != fast:
			# print(slow.val)
			if slow.val == fast.next.val:
				return slow.val
			slow = slow.next

# This is the implementation of the optimized solution


def findCycleStart(self):

	# getting the node where slow and fast meet incase of cycle
	slow = self.head
	fast = self.head

	ele = Node(0)

	while fast is not None and fast.next is not None:
		fast = fast.next.next
		slow = slow.next

		if slow == fast:
			ele = slow
			break

	# print(ele.val)

	# Getting the Cycle Length
	cycle_length = 1

	temp_node = ele.next

	while temp_node != ele:
		temp_node = temp_node.next
		cycle_length +=1

	print(cycle_length)

	# Starting with head and incrementing pointer2 by cycle_length
	# To get the node which is the head of the cycle.

	pointer1 = self.head
	pointer2 = self.head

	for i in range(cycle_length):
		pointer2 = pointer2.next


	# print(pointer1.val,pointer2.val)

	while pointer1 != pointer2:
		pointer1 = pointer1.next
		pointer2 = pointer2.next


	return(pointer1.val)

