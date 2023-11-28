class Solution:
    """
    A class implementing a solution to find the minimum number of times 'k' needs to be subtracted from 'num'
    to obtain a number divisible by 10.
    """
    def minimumNumbers(self, num, k):
        """
        Finds the minimum number of times 'k' needs to be subtracted from 'num'
        to obtain a number divisible by 10.
        """
        if num == 0:
            return 0
        for i in range(1, num+1):
            t = num - k * i
            if t >= 0 and t % 10 == 0:
                return i
        return -1

# Create an instance of the Solution class
solution = Solution()

# Taking input for 'num' and 'k'
num = int(input())
k = int(input())

# Get the minimum number of subtractions needed
result = solution.minimumNumbers(num, k)

# Print the result
if result == -1:
    print("-1")
else:
    print(result)
                                                                                                                            