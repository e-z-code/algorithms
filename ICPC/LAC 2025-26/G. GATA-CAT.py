import sys

LENGTH = 150
INF = float('inf')


# 1. TO COUNT INCREASES

add_count_gata = [0]
add_count_cat = [0]
for num in range(1, LENGTH + 1):
    add_count_gata.append((num * (num - 1) * (num + 1)) // 6)
    add_count_cat.append((num * (num + 1)) // 2)


# 2. TO GET THE INPUT AND SOLVE THE PROBLEM

query_count = int(sys.stdin.readline())

for query in range(query_count):

    gata_degree, cat_degree = map(int, sys.stdin.readline().split())

    left_gata_degree = gata_degree
    left_cat_degree = cat_degree

    now_block = LENGTH
    result = []
    while now_block > 0:
        while left_gata_degree > 0 and left_gata_degree >= add_count_gata[now_block]:
            result.append("G")
            left_gata_degree -= add_count_gata[now_block]
        while left_cat_degree > 0 and left_cat_degree >= add_count_cat[now_block]:
            result.append("C")
            left_cat_degree -= add_count_cat[now_block]
        result.append("AT")
        now_block -= 1

    print("".join(result))