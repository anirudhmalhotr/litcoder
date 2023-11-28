import sys
def kth_smallest_trimmed_number(nums, queries):
    result = []
    nums = nums.split()  # Split the input string into a list of numbers
    
    for k, trim in queries:
        trimmed_nums = [num[-trim:] for num in nums]  # Trim each number to the specified rightmost digits
        sorted_nums = sorted(trimmed_nums)  # Sort the trimmed numbers
        
        kth_smallest = sorted_nums[k - 1]  # Find the kth smallest trimmed number
        index = trimmed_nums.index(kth_smallest)  # Retrieve its index in the trimmed list
        
        result.append(index)  # Append the index to the result array
    
    return result
 
"""Main"""
input_nums = input()
queries_count = int(input())
 
queries = []
for _ in range(queries_count):
    query = list(map(int, input().split()))
    queries.append(query)
 
output = kth_smallest_trimmed_number(input_nums, queries)
print(*output)  # Print the output array
                                                                                                                            