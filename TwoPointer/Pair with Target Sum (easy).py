def search(arr, target_sum):
    l, r = 0, len(arr)-1

    while l < r:
        if arr[l]+arr[r]< target_sum:
            l+=1
        elif arr[l]+arr[r]> target_sum:
            r-=1
        else:
            return [l,r]
    