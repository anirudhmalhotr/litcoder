class Solution:
    """
    A class implementing a solution to calculate the minimum steps required to reach a target sweetness level
    by combining candies.

    """
    def minStepsToReachTargetSweetness(self, target, candies):
        """
        Calculates the minimum steps required to reach the target sweetness level.
        """
        # Sort the candies in ascending order
        candies.sort()
        steps = 0
        while candies[0] < target:
            leastSweet = candies.pop(0)
            secondLeastSweet = candies.pop(0)
            newSweetness = leastSweet + 2 * secondLeastSweet
            # Insert the new sweetness back into the sorted list of candies
            i = 0
            while i < len(candies) and candies[i] < newSweetness:
                i += 1
            candies.insert(i, newSweetness)
            steps += 1
        return steps

# Create an instance of the Solution class
solution = Solution()

# Input target sweetness and list of initial sweetness levels of candies
target = int(input())
candies = list(map(int, input().split()))

# Get the minimum steps to reach the target sweetness level
steps = solution.minStepsToReachTargetSweetness(target, candies)

# Print the minimum steps required
print(steps)
                                                                                                                            