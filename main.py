# input = 3[A]2[3[B]]C
# output = AAABBBBBBC

import re


def convert_schedule(i):
    output= []

    input = str(i)
    inputs = input.split(']')
    for i in inputs:
        digits = re.findall(r"\d", i)
        # print("digits:", digits)
        result = 1
        for x in digits:
            result = result * int(x)
            # print("result:", result)
        try:
            letter = re.search('[A-Z]', i).group()
            # print("letter:", letter)
            r = 0
            while r < result:
                output.append(letter)
                r += 1
        except:
            pass
    # print("output:", output)
    return ''.join(output)