import sys


# 2. DFS FUNCTION TO SOLVE THE PROBLEM

def dfs(num):

    ans.append(num)
    visited[num] = 1

    for prime in primes:
        if num * prime <= tome_cnt:
            if not visited[num * prime]:
                dfs(num * prime)
        else:
            break


# 1. SIEVES OF ERATOSTHENES

is_prime = [1 for num in range(1000001)]
is_prime[0], is_prime[1] = 0, 0

factor = 2
while factor <= 1000:
    if is_prime[factor]:
        for multiple in range(factor * 2, 1000001, factor):
            is_prime[multiple] = 0
    factor += 1

primes = []
for num in range(1000001):
    if is_prime[num]:
        primes.append(num)


# 3. TO GET THE INPUT AND SOLVE THE PROBLEM

tome_cnt, query_cnt = map(int, sys.stdin.readline().split())

ans = []
visited = [0 for num in range(tome_cnt + 1)]
dfs(1)

for query in range(query_cnt):
    order = int(sys.stdin.readline())
    print(ans[order-1])