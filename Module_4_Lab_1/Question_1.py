import sys
class Solution:
    def clumsy(self, N):
        ans = 0
        for i in range(N, 0, -4):
            x = (1 if i == N else -1) * i
            if i - 1 >= 1:
                x *= i - 1
                if i - 2 >= 1:
                    x //= i - 2
                    if i - 3 >= 1:
                        x += i - 3
            ans += x
        return ans
"""Main"""

if __name__ == "__main__":
    solution = Solution()
    N = int(input())  # Prompt the user for input
    clumsy_factorial = solution.clumsy(N)
    print(clumsy_factorial)
                                                                                                                            