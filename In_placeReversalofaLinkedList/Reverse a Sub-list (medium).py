
def reverse_idx(self, p,q):

	cnt = 0

	curr = self.head

	# Initializing 4 variables to store the pointers.
	start_1 = None
	start_2 = None
	end_2 = None
	end_1 = None



	while curr is not None:
		cnt +=1

		if cnt == p-1:
			start_1 = curr
		if cnt == p:
			start_2 = curr
		if cnt == q:
			end_2 = curr
		if cnt == q+1:
			end_1 = curr

		curr = curr.next

	# I am able to get the required nodes that we need to connect the chain after reversing.
	print(start_1.val, start_2.val, end_2.val, end_1.val)
	print(self)


	curr = start_2
	prev = None
	next = None

	# I am able to iterate between the index values and reverse them. The code is working when I print the values.
	while curr != end_1:
		print(curr.val)

		next = curr.next

		curr.next = prev
		prev = curr
		
		curr = next


	print("---------------------")
	print(prev.val, prev.next.val, prev.next.next.val)
	print(curr.val, curr.next.val)
	print(next.val, next.next.val)
	print("---------------------")

	start_1 = prev



	# The chain is breaking at this point.
	print(self)



	# Third loop

	curr = self.head

	while curr is not None:

		print(curr.val)

		if curr == start_1:
			curr.next = prev


		curr = curr.next


