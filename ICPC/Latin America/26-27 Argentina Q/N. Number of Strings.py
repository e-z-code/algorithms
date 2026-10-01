import sys
MOD = 998244353


# 2. FACTORIAL MOD PRE-PROCESSING

factorial_mod = [1]
for num in range(1, 1000001):
    factorial_mod.append((factorial_mod[-1] * num) % MOD)


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM
# Separate odd index and even index.
# Then, think of making X adjacent pairs (0 <= X <= K) for a parity set.
# Answer equals pow(A, 2) * pow(A-1, N-K-2) * C(N-2, K)

total_length, palindrome_cnt, alphabet_cnt = map(int, sys.stdin.readline().split())

ans = 1

if total_length == 1:
    if palindrome_cnt == 0:
        print(alphabet_cnt)
    else:
        print(0)
elif total_length == 2:
    if palindrome_cnt == 0:
        print(alphabet_cnt * alphabet_cnt)
    else:
        print(0)
else:
    if total_length - 2 >= palindrome_cnt:
        ans *= pow(alphabet_cnt, 2, MOD) * pow(alphabet_cnt-1, total_length-2-palindrome_cnt, MOD)
        ans %= MOD
        ans *= factorial_mod[total_length-2] * pow(factorial_mod[total_length-2-palindrome_cnt], MOD-2, MOD) * pow(factorial_mod[palindrome_cnt], MOD-2, MOD)
        ans %= MOD
        print(ans)
    else:
        print(0)