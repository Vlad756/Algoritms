# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
def two_sum(nums, target): # O(n^2)
    li = []
    i = 0
    while i < len(nums):
        j = 1
        while j < len(nums):
            if nums[i] + nums[j] == target and ([j, i] or [i, j]) not in li:
                li.append([i, j])
            j += 1
        i += 1
    return li

hey = two_sum([2,3,4,5,6,7], 9)
print(hey)
