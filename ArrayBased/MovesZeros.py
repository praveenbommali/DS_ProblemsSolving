'''Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.'''


class MoveZeros():
    def __init__(self):
        pass

    def move_zeros(self, nums):
        num_len = len(nums)
        count = 0
        for i in range(num_len):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
        for i in range(count, num_len):
            nums[i] = 0
        print(nums)

    def move_zeros1(self, nums):
        num_len = len(nums)
        nzero, cur = 0, 0
        for cur in range(num_len):
            if nums[cur] != 0:
                nums[nzero], nums[cur] = nums[cur], nums[nzero]
                nzero += 1
        print(nums)

if __name__ == '__main__':
    moveZeros = MoveZeros()
    nums = [0, 1, 0, 3, 12]
    moveZeros.move_zeros(nums);
    moveZeros.move_zeros1(nums)
