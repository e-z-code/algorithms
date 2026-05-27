import sys

def hash(direction, i, j):
    return direction * 100000000 + i * 10000 + j


# 2. A FUNCTION TO GET NEXT NODE

def get_next(node):

    now_dir = node // 100000000
    now_i, now_j = (node // 10000) % 10000, node % 10000

    x1, y1 = cats[now_i]
    x2, y2 = cats[now_j]

    dist = abs(x1 - x2) + abs(y1 - y2)
    if now_dir == 0:
        if 2 * y2 - y1 in y_coordinates:
            return hash(1, now_j, y_coordinates[2 * y2 - y1]), dist
        else:
            return None, None
    else:
        if 2 * x2 - x1 in x_coordinates:
            return hash(0, now_j, x_coordinates[2 * x2 - x1]), dist
        else:
            return None, None


# 1. TO GET THE INPUT

cat_count = int(sys.stdin.readline())

cats = []
for cat in range(cat_count):
    x, y = map(int, sys.stdin.readline().split())
    cats.append((x, y))


# 3. TO SOLVE THE PROBLEM

x_coordinates = {}
y_coordinates = {}
for idx in range(cat_count):
    x, y = cats[idx]
    x_coordinates[x] = idx
    y_coordinates[y] = idx

ans = 0
visited = set()

for i in range(cat_count):
    for j in range(i+1, cat_count):

        start_node = hash(0, i, j)
        count = {}

        now_node = start_node
        visited.add(now_node)
        length = 0

        while True:

            next_node, dist = get_next(now_node)
            if next_node is None:
                break

            length += dist

            now_node = next_node
            count[now_node % 10000] = count.get(now_node % 10000, 0) + 1
            if now_node == start_node:
                if max(count.values()) < 2:
                    ans = max(ans, length)
                    break
            if now_node in visited:
                break
            visited.add(now_node)

print(ans)
