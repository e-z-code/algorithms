import sys


# 2. FUNCTIONS

def is_num(word):

    result = True
    for char in word:
        if not char.isdigit():
            result = False
            break
    return result

def is_exp_of_ten(num):

    result = True
    if num[0] != "1":
        result = False

    for idx in range(1, len(num)):
        if num[idx] != "0":
            result = False
            break
    return result

def divide(num):

    int_part = num[0]
    decimal_part = list(num[1:])
    while decimal_part and decimal_part[-1] == "0":
        decimal_part.pop()
    decimal_part = "".join(decimal_part)

    return int_part, decimal_part

def convert(num):

    exp = len(num) - 1

    if int(num) % 10000 == 0:
        if is_exp_of_ten(num):
            return "10^{" + str(exp) + "}"
        else:
            int_part, decimal_part = divide(num)
            if len(decimal_part) != 0:
                return str(int_part) + "." + str(decimal_part) + "\cdot10^{" + str(exp) + "}"
            else:
                return str(int_part) + "\cdot10^{" + str(exp) + "}"
    else:
        return str(num)


# 1. TO GET THE INPUT

line_cnt = int(sys.stdin.readline())

strings = []
for line in range(line_cnt):
    string = list(sys.stdin.readline().strip().split())
    strings.append(string)


# 3. TO SOLVE THE PROBLEM

for string in strings:

    ans = []

    for word in string:
        if is_num(word):
            ans.append(convert(word))
        else:
            ans.append(word)

    print(" ".join(ans))
