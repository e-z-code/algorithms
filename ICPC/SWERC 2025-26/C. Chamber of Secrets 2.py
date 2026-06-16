import sys


# 1. TO GET THE INPUT

test_cnt = int(sys.stdin.readline())

for test in range(test_cnt):

    arr_cnt, arr_length = map(int, sys.stdin.readline().split())

    # 2. TO SOLVE THE PROBLEM

    if arr_cnt % 2 == 0:

        check = set()
        for idx in range(arr_cnt):
            arr = tuple(map(int, sys.stdin.readline().split()))
            if arr not in check:
                check.add(arr)

        ans = []
        for arr in check:
            for num in arr:
                ans.append(num)
        print(" ".join(map(str, ans)))

    else:

        graph = {}

        start = None
        for idx in range(arr_cnt):
            arr = list(map(int, sys.stdin.readline().split()))
            arrA, arrB = tuple(arr[:arr_length // 2]), tuple(arr[arr_length // 2:])
            if start is None:
                start = arrA
            graph[arrA] = arrB

        ans = []
        visited = set()
        visited.add(start)

        now_node = start
        while graph[now_node] in graph and graph[now_node] not in visited:
            for num in now_node:
                ans.append(num)
            now_node = graph[now_node]
        for num in now_node:
            ans.append(num)

        print(" ".join(map(str, ans)))