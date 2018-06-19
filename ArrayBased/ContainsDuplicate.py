'''

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
'''


class ConatinsDuplicate:
    def __init__(self):
        pass

    def find_duplicate(self, nums):
        dict = {}
        for i in nums:
            dict[i] = 0

        for i in nums:
            if dict[i] == 0:
                dict[i] = 1
            else:
                return True
        return False


if __name__ == '__main__':
    conatinsDuplicate = ConatinsDuplicate()
    print(conatinsDuplicate.find_duplicate([1, 2, 3, 4]))
