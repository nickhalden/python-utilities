import re


def firstRepeatingLetter(s):

    return unique(s)


def unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 256:
        return False

    char_set = [0 for _ in range(256)]  # set everythin false
    for char in string:
        val = ord(char)
        char_set[val] = char_set[val] + 1


    counter=0
    for x in char_set:
        if x >= 2:

            return chr(counter)

        counter=counter+1
firstRepeatingLetter('finding')