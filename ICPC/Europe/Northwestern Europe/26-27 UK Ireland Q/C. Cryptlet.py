import sys
from itertools import permutations, combinations


# 1. TO GET THE INPUT

equation = sys.stdin.readline().strip()
equation = equation.replace("+", " ").replace("=", " ")
equation = list(equation.split())
for idx in range(3):
    equation[idx] = list(equation[idx])


# 2. TO SOLVE THE PROBLEM

left = [0, 0, 0, 0, 0]
right = [0, 0, 0, 0, 0]

for i in range(3):
    term = equation[i]
    for j in range(len(term)):
        if i != 2:
            left[ord(term[-j-1]) - ord('a')] += pow(10, j)
        else:
            right[ord(term[-j-1]) - ord('a')] += pow(10, j)

ans = "impossible"
for comb in combinations(range(0, 10), 5):
    if ans == "impossible":
        for perm in permutations(comb, 5):
            a, b, c, d, e = perm
            left_val = left[0] * a + left[1] * b + left[2] * c + left[3] * d + left[4] * e
            right_val = right[0] * a + right[1] * b + right[2] * c + right[3] * d + right[4] * e
            if left_val == right_val:
                ans = str(a) + str(b) + str(c) + str(d) + str(e)
                break
print(ans)