# Given input String need to find all non-empty substrings

def substring_find(input_string):
    for i in range(len(input_string)):
        print(input_string[:1])
        substring_find(input_string[i:i-1])


substring_find("abc")
