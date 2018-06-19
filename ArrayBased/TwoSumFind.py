'''

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


def find_two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and target == nums[i] + nums[j]:
                return i, j


nums = [3, 2, 4]
target = 6
print(find_two_sum(nums, target))
