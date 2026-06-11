import sys
OFFSET = 1 << 18


# 3. FUNCTIONS TO SOLVE THE PROBLEM

def get_sum(left, right):

    left += OFFSET
    right += OFFSET

    result = 0
    while left <= right:
        if left % 2 == 1:
            result += seg_tree[left]
            left += 1
        if right % 2 == 0:
            result += seg_tree[right]
            right -= 1
        left >>= 1
        right >>= 1

    return result

def turn_off(idx):

    idx += OFFSET
    while idx != 0:
        seg_tree[idx] -= 1
        idx >>= 1


# 1. TO GET THE INPUT

card_cnt = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
for idx in range(card_cnt):
    cards[idx] -= 1


# 2. MAKE DDL

tail_loc = card_cnt - 1
loc = [-1 for idx in range(card_cnt)]
prev = [-1 for idx in range(card_cnt)]
next = [-1 for idx in range(card_cnt)]

for idx in range(card_cnt):
    loc[cards[idx]] = idx
    prev[idx] = (idx-1) % card_cnt
    next[idx] = (idx+1) % card_cnt


# 4. TO SOLVE THE PROBLEM

node_cnt = OFFSET << 1

seg_tree = [0 for idx in range(node_cnt)]
for idx in range(card_cnt):
    seg_tree[idx + OFFSET] = 1
for idx in range(OFFSET-1, 0, -1):
    seg_tree[idx] = seg_tree[(idx << 1)] + seg_tree[(idx << 1) | 1]

ans = []
for num in range(card_cnt-1, -1, -1):

    now_loc = loc[num]
    if now_loc <= tail_loc:
        ans.append(get_sum(now_loc, tail_loc))
    else:
        ans.append(get_sum(now_loc, card_cnt-1) + get_sum(0, tail_loc))

    turn_off(now_loc)

    prev_loc = prev[now_loc]
    next_loc = next[now_loc]

    tail_loc = prev[now_loc]
    next[prev_loc] = next_loc
    prev[next_loc] = prev_loc

print(" ".join(map(str, reversed(ans))))