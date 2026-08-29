import sys
MOD = 998244353


# 1. TO GET THE INPUT

test_cnt = int(sys.stdin.readline())

for test in range(test_cnt):

    word_length, goal_length = map(int, sys.stdin.readline().split())
    word = sys.stdin.readline().strip()


    # 2. TO EXTRACT VALID PREFIXES

    kmp_table = [0 for idx in range(word_length)]

    i = 0
    for j in range(1, word_length):
        while i > 0 and word[i] != word[j]:
            i = kmp_table[i-1]
        if word[i] == word[j]:
            i += 1
            kmp_table[j] = i

    valid_length = []
    for idx in range(word_length):
        if kmp_table[idx] == 0:
            valid_length.append(idx + 1)


    # 3. TO SOLVE THE PROBLEM

    dp = [0 for idx in range(goal_length + 1)]
    dp[0] = 1

    for idx in range(1, goal_length + 1):
        for length in valid_length:
            if idx >= length:
                dp[idx] += dp[idx - length]
                dp[idx] %= MOD

    print(dp[-1])