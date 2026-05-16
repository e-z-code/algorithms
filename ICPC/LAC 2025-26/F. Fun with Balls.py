import sys
from itertools import product
from collections import deque


def in_range(row, col):
    return 0 <= row < 17 and 0 <= col < 17


# 2. FUNCTIONS

def get_piles(piles, align):
    result = [[0 for col in range(17)] for row in range(17)]

    for height in range(17):
        line = list(piles[height])
        if align == "L":
            for idx in range(-1, -len(line) - 1, -1):
                result[height][idx] = line[idx]
        else:
            for idx in range(len(line)):
                result[height][idx] = line[idx]

    return result


def get_size(piles, align):
    if align == "L":
        dy = [-1, -1, 0, 0, 1, 1]
        dx = [-1, 0, -1, 1, 0, 1]
    else:
        dy = [-1, -1, 0, 0, 1, 1]
        dx = [0, 1, -1, 1, -1, 0]

    result = 0
    visited = [[0 for col in range(17)] for row in range(17)]

    for row in range(17):
        for col in range(17):
            if not visited[row][col] and piles[row][col] != 0:

                queue = deque([(row, col)])
                visited[row][col] = 1

                size = 1
                while queue:
                    now_row, now_col = queue.popleft()
                    for idx in range(6):
                        next_row = now_row + dy[idx]
                        next_col = now_col + dx[idx]
                        if in_range(next_row, next_col) and not visited[next_row][next_col]:
                            if piles[now_row][now_col] == piles[next_row][next_col]:
                                queue.append((next_row, next_col))
                                visited[next_row][next_col] = 1
                                size += 1

                result = max(result, size)

    return result


# 1. TO GET THE INPUT

ball_count = int(sys.stdin.readline())
colors = list(map(int, sys.stdin.readline().split()))


# 3. TO SOLVE THE PROBLEM

ans = 0

for now_case in product(("L", "R"), repeat=16):

    max_height = 1
    now_height = 0
    choice_idx = 0

    piles = [deque() for height in range(17)]
    piles[0].append(colors[0])

    for idx in range(1, ball_count):

        color = colors[idx]
        if now_case[choice_idx] == "L":
            piles[now_height].appendleft(color)
        else:
            piles[now_height].append(color)

        if max_height == now_height:
            max_height += 1
            now_height = 0
            choice_idx += 1
        else:
            now_height += 1

    piles = get_piles(piles, now_case[choice_idx])
    ans = max(ans, get_size(piles, now_case[choice_idx]))
    if ans == 42:
        print(now_case)
        print(now_case[choice_idx])
        for line in piles:
            print(line)
        break

print(ans)

