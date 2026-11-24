import sys
alphabet = "abcdefghijklmnopqrstuvwxyz"


# 1. TO GET THE INPUT

word_cnt, goal_cnt = map(int, sys.stdin.readline().split())
words = list(sys.stdin.readline().strip().split())
for idx in range(word_cnt):
    words[idx] = list(words[idx])


# 2. TO SOLVE THE PROBLEM

cnt = {}
for word in words:
    for character in word:
        cnt[character] = cnt.get(character, 0) + 1

sorted_char = sorted(list(alphabet), key = lambda x : -cnt.get(x, 0))

for i in range(word_cnt):
    for j in range(len(words[i])):
        if sorted_char.index(words[i][j]) >= goal_cnt:
            words[i][j] = sorted_char[0]

for idx in range(word_cnt):
    words[idx] = "".join(words[idx])
print(" ".join(words))