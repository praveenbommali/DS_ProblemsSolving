'''

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

'''


class ReverseNumber(object):
    def __init__(self):
        pass

    def reverse(self, x):
        numS = str(x)[::-1]
        if numS[len(numS) - 1] == '-':
            numS = numS[:len(numS) - 1:1]
        numS = int(numS)
        numS = numS - (2 * numS)
        if abs(int(numS)) > 2 ** 31 - 1:
            return 0
        return int(numS)


if __name__ == '__main__':
    reverseNumber = ReverseNumber()
    print(reverseNumber.reverse(123))
