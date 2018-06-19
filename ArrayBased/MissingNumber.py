'''Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2'''


class MissingNum():
    def __init__(self):
        pass

    def missing_num(self, nums):
        n_len = len(nums)
        sum_all = (n_len)*(n_len+1)/2
        sum_nums = sum(nums)
        missing_num = sum_all -sum_nums
        print(int(missing_num))


if __name__ == '__main__':
    missingNum = MissingNum()
    missingNum.missing_num([9,6,4,2,3,5,7,0,1])
