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
