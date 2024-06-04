# Not working for some cases.
# Some issue with the loops and if else conditions.
# Maybe need more practice with pseudo Code?

# In the actual answer, they have 2 separate if else conditions. I merged them into 1.
#

def searchTriplet(arr, target):

    arr.sort()
    # print(arr)

    min_ = float("inf")
    triplet = float("inf")

    for i in range(len(arr)-2):
        # print(arr[i])

        l = i+1
        r = len(arr)-1

        while l<r:
        
            temp_sum = arr[i] + arr[l] + arr[r]
            abs_diff = abs(temp_sum-target)

            if temp_sum > target:
                if min_ >= abs_diff:
                    min_ = abs_diff
                    triplet = min(triplet, temp_sum)

                    
                r-=1
            else:
                if min_ >= abs_diff:
                    min_ = abs_diff
                    triplet = min(triplet, temp_sum)       
                
                l+=1

    return triplet   
            