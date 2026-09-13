import sys

'''
Following code is useful to find the logic.

def make_seq(start):

    cnt = {start:1}
    result = [start]

    while len(result) < 1000:
        result.append(cnt.get(result[-1], 0))
        cnt[result[-1]] = cnt.get(result[-1], 0) + 1

    return result
'''


# 1. TO MAKE THE SEQUENCE AND SOLVE THE PROBLEM

while True:

    start, term = map(int, sys.stdin.readline().split())
    if start == 0 and term == 0:
        break

    if pow(start, 2) + 2 <= term:

        cycle_cnt = (term - (pow(start, 2) + 1)) // (2 * start)
        cycle_idx = (term - (pow(start, 2) + 1)) % (2 * start)
        if cycle_idx == 0:
            cycle_idx = 2 * start

        if cycle_idx % 2 == 1:
            print(start + 1 + cycle_cnt)
        else:
            print(cycle_idx // 2)

    else:

        if term == 1:
            print(start)
        elif term == 2:
            print(1)
        else:
            now_num = 1
            now_term = 2
            while True:
                if term <= now_term + 4 * (start - now_num):
                    if term <= now_term + 2 * (start - now_num):
                        if term % 2 == 1:
                            print(now_num)
                        else:
                            print(now_num + (term - now_term) // 2)
                    elif term <= now_term + 4 * (start - now_num) - 2:
                        if term % 2 == 1:
                            print(now_num + (term - now_term - 2 * (start - now_num) + 1) // 2)
                        else:
                            print(now_num + 1)
                    else:
                        if term == now_term + 4 * (start - now_num) - 1:
                            print(start)
                        else:
                            print(now_num + 2)
                    break
                else:
                    now_term += 4 * (start - now_num)
                    now_num += 2