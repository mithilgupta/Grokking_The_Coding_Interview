
def get_digit_sq(num):
    ans = 0
    num = str(num)
    for i in range(len(num)):
        # print(num[i])
        ans += int(num[i])*int(num[i])

    return ans
        

# Happy number
# This Brute Force approach with List works with 2 loops.
def find(num):

    ll = []

    # Initializing with the first value
    dig_sq = get_digit_sq(num)
    ll.append(dig_sq)

    while ll[-1] != 1:
        new_dig_sq = get_digit_sq(ll[-1])
    
        for i in range(len(ll)):
            if ll[i] == new_dig_sq:
                return False
                
        ll.append(new_dig_sq)


    return True


# I tried doing it with Slow and Fast Pointer.
# But I got stuck in 2 places:
# 1. Initializing slow and Fast, because how do I counter initial While COndition if both are HEAD.
# 2. The values of slow and fast are not changing with each iteration (function call to get_digit_sq()) -> Does this need recursion??
    
def find2(num):
    slow = num
    fast = get_digit_sq(num)
    cnt = 0

    while slow != fast and cnt < 30:
        fast = get_digit_sq(get_digit_sq(num))
        slow = get_digit_sq(num)
        cnt +=1


        print(slow, fast)
