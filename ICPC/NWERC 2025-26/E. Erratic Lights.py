import sys
sys.setrecursionlimit(10 ** 6)


# 2. DP FUNCTION

def solve(first, second, third):

    if dp[first][second][third] != -1:
        return dp[first][second][third]

    if first + second <= third:
        dp[first][second][third] = 3 * (first + second)
    else:
        if second == third:
            dp[first][second][third] = (solve(first-1, third, second+1) / 3 + solve(first-1, second, third+1) / 3 + 1) * 3 / 2
        else:
            dp[first][second][third] = (solve(first-1, second+1, third) / 3 + solve(first-1, second, third+1) / 3 + 1) * 3 / 2

    return dp[first][second][third]


# 1. TO GET THE INPUT

light_count = int(sys.stdin.readline())
lights = sys.stdin.readline().strip()

count = [0, 0, 0]
for light in lights:
    if light == "r":
        count[0] += 1
    elif light == "g":
        count[1] += 1
    else:
        count[2] += 1
count.sort()


# 3. TO SOLVE THE PROBLEM

dp = [[[-1 for third in range(101)] for second in range(101)] for first in range(101)]

print(solve(count[0], count[1], count[2]))