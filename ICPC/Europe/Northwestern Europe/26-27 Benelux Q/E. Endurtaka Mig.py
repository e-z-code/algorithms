import sys


# 1. TO GET THE INPUT

word = sys.stdin.readline().strip()
length = len(word)


# 2. TO FIND THE POSSIBLE PATTERN

kmp_table = [0 for idx in range(length)]

i = 0
for j in range(1, length):
    while i > 0 and word[i] != word[j]:
        i = kmp_table[i-1]
    if word[i] == word[j]:
        i += 1
        kmp_table[j] = i

pattern = word[:length - kmp_table[-1]]


# 3. TO SOLVE THE PROBLEM

is_pattern = True
if pattern == word or length % len(pattern) != 0:
    is_pattern = False

if is_pattern:
    if len(pattern) == 1:
        print(length)
        print(" ".join([pattern for repeat in range(length)]))
    else:
        print(2)
        print(word[:-1], word[-1])
else:
    print(1)
    print(word)