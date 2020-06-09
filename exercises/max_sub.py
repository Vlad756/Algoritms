# Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest 
# sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution,
# try coding another solution using the divide and conquer approach, 
# which is more subtle.
def maxSubArray(nums): # time complexity O(n), space complexity O(1)
	result = nums[0]
	summ = nums[0]
	i = 1
	while i < len(nums):
		summ = max(nums[i], summ + nums[i] )
		result = max(result, summ)
		i += 1
	return result

x = maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(x)