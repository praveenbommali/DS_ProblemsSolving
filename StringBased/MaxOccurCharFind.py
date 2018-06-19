# Given input String need to find the maximum occurrence character
# return the count and char value


def get_max_occur_char(input_string):
    count = [0] * 256
    max = -1
    c = ''

    for i in input_string:
        print(ord(i))
        count[ord(i)] += 1
        if count[ord(i)] > 1 and max <= count[ord(i)]:
            max = count[ord(i)]
            c = i
    return c, max


print(" Max", get_max_occur_char("sample testtteeeeesssss"))
