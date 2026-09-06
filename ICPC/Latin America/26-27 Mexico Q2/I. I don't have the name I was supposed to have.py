import sys
symbols = "!?.,;$#^{}_=+* "


# 2. FUNCTIONS TO CHECK VALIDITY

def valid_char(line):

    result = True

    for letter in line:
        if not letter.isalnum() and letter not in symbols:
            result = False
            break

    return result

def valid_space(line):

    result = True

    if line.strip() != line:
        result = False

    return result

def valid_script(line):

    result = True

    words = list(line.strip().split())
    for word in words:
        if "_" in word:
            if word.count("_") > 1:
                result = False
                break
            partX, partY = word.split("_")
            if len(partY) < 2 or partY[0] != "{" or partY[-1] != "}":
                result = False
                break
            partY = partY[1:-1]
            if not partX.isalnum() or not partY.isdigit():
                result = False
                break
            if partY.isdigit() and len(partY) > 1 and partY[0] == "0":
                result = False
                break
        elif "^" in word:
            if word.count("^") > 1:
                result = False
                break
            partX, partY = word.split("^")
            if len(partY) < 2 or partY[0] != "{" or partY[-1] != "}":
                result = False
                break
            partY = partY[1:-1]
            if not partX.isalnum() or not partY.isdigit():
                result = False
                break
            if partY.isdigit() and len(partY) > 1 and partY[0] == "0":
                result = False
                break
        else:
            if "{" in word or "}" in word:
                result = False
                break

    return result

def valid_surrounding(line):

    result = True

    for idx in range(len(line)):
        if line[idx].isdigit():
            if idx != 0 and not line[idx-1].isalnum() and line[idx-1] not in " _^{}":
                result = False
                break
            if idx != len(line) - 1 and not line[idx+1].isalnum() and line[idx+1] not in " _^{}":
                result = False
                break

    return result

def valid_num(line):

    result = True

    words = list(line.strip().split())
    for word in words:
        if word.isdigit() and len(word) > 1 and word[0] == "0":
            result = False
            break

    return result

def valid_consecutive_space(line):

    result = True

    for idx in range(1, len(line)):
        if line[idx-1] == line[idx] == " ":
            result = False
            break

    return result

def test(line):

    result = True

    result &= valid_char(line)
    result &= valid_space(line)
    result &= valid_script(line)
    result &= valid_surrounding(line)
    result &= valid_num(line)
    result &= valid_consecutive_space(line)

    return result


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

line_cnt = int(sys.stdin.readline())

lines = []
for line in range(line_cnt):
    lines.append(sys.stdin.readline().strip("\n"))

result = True
for line in lines:
    result &= test(line)

if result:
    print("Ok")
else:
    print("Validation failed")