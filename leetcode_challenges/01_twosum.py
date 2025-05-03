# LeetCode Two Sum Problem Solution 
# Date: 6/12/2024
# Given a list of numbers and a target, find indices of the two numbers such that they add up to the target.

# Input list of numbers
numbers = [3, 2, 4]

# Target sum
target = 6

# Initialize an empty list to store indices
indices = []

# Iterate over each pair of numbers in the list with a Nested Loop
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        # Check if the sum of the pair equals the target
        if numbers[i] + numbers[j] == target:
            # If so, append their indices to the indices list
            indices.append(i)
            indices.append(j)
            break  # Break the inner loop once the pair is found
    if indices:  # If indices are found, break the outer loop as well
        break

# Print the indices of the numbers that sum to the target
print(indices)  # Expected Output: [1, 2]


# The Actual One uploaded to Leet Code

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         indices = []
#         # Nested loop
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     indices.append(i)
#                     indices.append(j)
#                     return indices


# Learned: Nested Loops, how to append indices and values of a list, sum(), and how to iterate a list with for loop. 