import sys
def smallest_values(arr, k, n):
    result = []
    for i in range(len(arr) - k + 1):
        sub_array = arr[i:i+k]
        sub_array.sort()
        result.append(sub_array[n - 1])
    return result

#Accepting input from the user
input_arr = list(map(int, input().split()))
k = int(input())
n = int(input())

#Calculating and displaying the output
output = smallest_values(input_arr, k, n)
print(' '.join(map(str, output)))
                                                                                                                            