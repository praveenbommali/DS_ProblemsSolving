'''

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

'''


class RotateArray(object):
    def __init__(self):
        pass

    def rotate_array(self, nums, k):
        d = nums[0:k]
        n = len(nums)
        for i in range(0, k):
            nums[n - k], nums[i] = nums[i], nums[n - k]
            k -= 1
        print(nums)


if __name__ == '__main__':
    rotateArray = RotateArray()
    rotateArray.rotate_array([1, 2, 3, 4, 5 ], 2)
