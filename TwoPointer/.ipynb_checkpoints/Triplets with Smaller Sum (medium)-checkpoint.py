# I can think of doing this with 3 loops.
# Which is Brute Force.


def searchTriplets(self, arr, target):
	arr.sort()
	#     print(arr)
	output = []
	
	for i in range(len(arr)-2):
	#         print(arr[i])
		for l in range(i+1, len(arr)-1):
			r = len(arr)-1
			
			while r > l:
				temp_sum = arr[i]+arr[l]+ arr[r]
				
				if temp_sum < target:
					output.append([arr[i],arr[l],arr[r]])
					
				r-=1
				
	return(len(output))