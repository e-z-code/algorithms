import sys
INF = float('inf')


# 1. TO GET THE INPUT

cell_cnt, total_hop_cnt = map(int, sys.stdin.readline().split())
hops = list(sys.stdin.readline().strip().split())
hops_set = set(hops)


# 2. TO COUNT HOPS

name_to_id = {}
id_to_name = {}

now_id = 0
for cell in hops_set:
    name_to_id[cell] = now_id
    id_to_name[now_id] = cell
    now_id += 1

for character in "abcdefghijklmnopqrstuvwxyz":
    if now_id == cell_cnt:
        break
    if character not in hops_set:
        name_to_id[character] = now_id
        id_to_name[now_id] = character
        now_id += 1

hop_cnt = [[0 for j in range(cell_cnt)] for i in range(cell_cnt)]

for idx in range(total_hop_cnt - 1):
    cellA = name_to_id[hops[idx]]
    cellB = name_to_id[hops[idx+1]]
    hop_cnt[cellA][cellB] += 1


# 3. TO SOLVE THE PROBLEM - BITMASK DP

dp = [INF for now_set in range(1 << cell_cnt)]
prev = [INF for now_set in range(1 << cell_cnt)]
dp[0] = 0

for now_set in range(1, 1 << cell_cnt):

    in_elements = []
    out_elements = []
    for element in range(cell_cnt):
        if now_set & (1 << element):
            in_elements.append(element)
        else:
            out_elements.append(element)

    add_val = 0
    for in_element in in_elements:
        for out_element in out_elements:
            add_val += hop_cnt[in_element][out_element] + hop_cnt[out_element][in_element]

    for element in range(cell_cnt):
        if now_set & (1 << element):
            base = dp[now_set ^ (1 << element)]
            if base + add_val < dp[now_set]:
                dp[now_set] = base + add_val
                prev[now_set] = element

ans = []
now_set = (1 << cell_cnt) - 1

while now_set:
    if prev[now_set] == INF:
        break
    ans.append(id_to_name[prev[now_set]])
    now_set ^= (1 << prev[now_set])

print(" ".join(ans))