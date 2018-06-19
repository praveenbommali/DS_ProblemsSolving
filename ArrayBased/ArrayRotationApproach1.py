# Basic Array Rotation Approach takes O(n^2) time

import array

'''
In this Approach it takes 0(n^2) time 
'''


def array_rotation1(input_array, offset):
    input_len = len(input_array)
    for i in range(0, offset):
        last_index = input_array[0]
        for j in range(input_len - 1):
            input_array[j] = input_array[j + 1]
        input_array[input_len - 1] = last_index
    print(input_array)


def gcd(d, n):
    if n == 0:
        return d
    else:
        return gcd(n, d % n)


def array_rotation2(input_array, n, d):
    for i in range(gcd(d, n)):
        temp = input_array[i]
        j = i
        while True:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            input_array[j] = input_array[k]
            j = k
        input_array[j] = temp
    print(input_array)


def reverse_array(input_array, a, b):
    while a < b:
        temp = input_array[a]
        input_array[a] = input_array[b]
        input_array[b] = temp
        a += 1
        b -= 1


def array_rotation3(input_array, n, d):
    reverse_array(input_array, 0, d - 1)
    reverse_array(input_array, d, n - 1)
    reverse_array(input_array, 0, n - 1)


def array_rotation4(input_array, n, d):
    for i in range(d):
        cyclic_rotate(input_array)
    print(input_array)


def cyclic_rotate(input_array):
    n = len(input_array)
    temp = input_array[n - 1]
    for i in range(n - 1, 0, -1):
        input_array[i] = input_array[i - 1]
    input_array[0] = temp


input_array = array.array('i', [1, 2, 3, 4, 5, 6])
print(input_array)
offset = int(input("Please enter the offset value"))
# array_rotation1(input_array, offset)
# array_rotation2(input_array, len(input_array), offset)

# array_rotation3(input_array, len(input_array), offset)
array_rotation4(input_array, len, offset)
