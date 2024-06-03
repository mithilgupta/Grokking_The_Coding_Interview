def moveElements(arr):
    # just getting the count
    # if len(arr) < 1:
    #     return 0
        
    # cnt = 1
    
    # for i in range(1,len(arr)):
    #     if arr[i] >arr[i-1]:
    #         cnt+=1
    # return cnt


    # Moving them to the beginning of the array as well

    cnt = 1
    l = 0

    for i in range(1,len(arr)):
        if arr[i] != arr[l]:
            l+=1
            if l < i:
                arr[i], arr[l] = arr[l], arr[i]
    return l+1
            