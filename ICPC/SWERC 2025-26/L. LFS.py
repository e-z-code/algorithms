import sys
INF = float('inf')


# 1. TO GET THE INPUT

word_length, query_cnt = map(int, sys.stdin.readline().split())
word = sys.stdin.readline().strip()


# 2. TO ORGANIZE INFORMATION TO SOLVE THE PROBLEM

prefix_sum = [[0 for alphabet in range(26)] for idx in range(word_length + 1)]

for idx in range(1, word_length + 1):
    now_alphabet = ord(word[idx-1]) - ord('a')
    for alphabet in range(26):
        prefix_sum[idx][alphabet] = prefix_sum[idx-1][alphabet]
        if alphabet == now_alphabet:
            prefix_sum[idx][alphabet] += 1

next_loc = [[INF for alphabet in range(26)] for idx in range(word_length)]

for idx in range(word_length-1, -1, -1):
    for alphabet in range(26):
        if idx != word_length - 1:
            next_loc[idx][alphabet] = next_loc[idx+1][alphabet]
    next_loc[idx][ord(word[idx]) - ord('a')] = idx

end = [-1 for idx in range(word_length)]

for alphabet in range(26):
    stack = []
    for idx in range(word_length):
        if word[idx] == chr(alphabet + ord("a")):
            if idx == word_length - 1 or (stack and word[stack[-1] + 1] != word[idx + 1]):
                while stack:
                    end[stack.pop()] = idx
            stack.append(idx)
    while stack:
        end[stack.pop()] = INF


# 3. TO SOLVE THE PROBLEM

for query in range(query_cnt):

    left, right = map(int, sys.stdin.readline().split())

    max_cnt = -1
    max_alphabet = []
    for alphabet in range(26):
        count = prefix_sum[right][alphabet] - prefix_sum[left-1][alphabet]
        if count > max_cnt:
            max_cnt = count
            max_alphabet = [alphabet]
        elif count == max_cnt:
            max_alphabet.append(alphabet)

    left -= 1
    right -= 1

    ans = 0
    for alphabet in max_alphabet:

        now_cnt = 1
        now_alphabet = alphabet

        while end[next_loc[left][now_alphabet]] > right and now_alphabet != ord(word[right]) - ord("a"):
            if next_loc[left][now_alphabet] != word_length-1:
                now_alphabet = ord(word[next_loc[left][now_alphabet] + 1]) - ord("a")
                if next_loc[left][now_alphabet] <= right:
                    now_cnt += 1
                else:
                    break
            else:
                break

        ans = max(ans, now_cnt)

    print(ans)