def func(array):
    max_len = 0
    sum=0
    sum_map = {0:-1}
    
    for i in range(len(array)):
        if nums[i] == 0:
            sum -= 1
        else:
            sum +=1
        
        if sum in sum_map:
            max_len = max(max_len, i-sum_map[sum])
        else:
            sum_map[sum] = i
        
    return max_len
    
nums = list(map(int,input().split()))
output = func(nums)
print(output)