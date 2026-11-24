import sys
INF = float('inf')


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

n = int(sys.stdin.readline())

best_a, best_b = INF, INF
for a in range(n + 1, 2 * n):
    if a * n % (a - n) == 0:
        b = a * n // (a - n)
        if a + b < best_a + best_b:
            best_a, best_b = a, b

if best_a > best_b:
    best_a, best_b = best_b, best_a

print(best_a, best_b)
