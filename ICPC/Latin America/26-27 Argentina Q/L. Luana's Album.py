import sys
INF = float('inf')


# 1. TO GET THE INPUT

sticker_cnt, slot_cnt = map(int, sys.stdin.readline().split())
stickers = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

stickers_sorted = sorted(list(set(stickers)))

now_num = 0
convert = {}
for idx in range(len(stickers_sorted)):
    sticker = stickers_sorted[idx]
    if sticker <= slot_cnt and sticker not in convert:
        convert[sticker] = now_num
        now_num += 1

stickers_converted = []
for sticker in stickers:
    if sticker <= slot_cnt:
        stickers_converted.append(convert[sticker])

stickers = stickers_converted
stickers_reversed = reversed(stickers)

best_forward = [INF for num in range(now_num)]
for sticker in stickers:
    if sticker != 0:
        best_forward[sticker] = min(best_forward[sticker-1], sticker)
    best_forward[sticker] = min(best_forward[sticker], sticker)

best_forward_move = [0 for num in range(now_num)]
for num in range(now_num):
    best_forward_move[best_forward[num]] = max(best_forward_move[best_forward[num]], num + 1)
for num in range(1, now_num):
    best_forward_move[num] = max(best_forward_move[num-1], best_forward_move[num])

best_backward = [INF for num in range(now_num)]
for sticker in stickers_reversed:
    if sticker != 0:
        best_backward[sticker] = min(best_backward[sticker-1], sticker)
    best_backward[sticker] = min(best_backward[sticker], sticker)

best_backward_move = [0 for num in range(now_num)]
for num in range(now_num):
    best_backward_move[best_backward[num]] = max(best_backward_move[best_backward[num]], num + 1)
for num in range(1, now_num):
    best_backward_move[num] = max(best_backward_move[num-1], best_backward_move[num])

now_cnt = 0
now_sticker = 0
while True:
    now_cnt += 1
    now_sticker = max(best_forward_move[now_sticker], best_backward_move[now_sticker], now_sticker)
    if now_sticker == now_num:
        break

print(now_num, now_cnt)