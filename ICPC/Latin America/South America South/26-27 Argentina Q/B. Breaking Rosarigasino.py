import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

word = sys.stdin.readline().strip()

candidates = set()
convert = {"AGASA":"A", "EGASE":"E", "IGASI":"I", "OGASO":"O", "UGASU":"U"}

for idx in range(len(word) - 4):
    if word[idx:idx+5] in convert:
        candidates.add(word[:idx] + convert[word[idx:idx+5]] + word[idx+5:])

if len(candidates) == 0:
    print("-")
elif len(candidates) == 1:
    ans = list(candidates)[0]
    print(ans)
else:
    print("+")