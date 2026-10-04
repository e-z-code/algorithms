import sys
from collections import deque


# 1. TO GET THE INPUT

test_cnt = int(sys.stdin.readline())

for test in range(test_cnt):

    ops = []
    op_cnt = int(sys.stdin.readline())


    # 2. TO SORT OPERATIONS BASED ON NUMBER

    valid = set()
    num_op = dict()

    for op in range(op_cnt):

        cmd, num = sys.stdin.readline().strip().split()
        num = int(num)
        ops.append((cmd, num))

        if cmd == "+":
            if num in valid:
                num_op[num].append("-")
                num_op[num].append("+")
            else:
                valid.add(num)
                if num in num_op:
                    num_op[num].append("+")
                else:
                    num_op[num] = deque(["+"])
        elif cmd == "-":
            valid.remove(num)
            num_op[num].append("-")
        elif cmd == "T":
            num_op[num].append("?")
        else:
            if num in valid:
                valid.remove(num)
                num_op[num].append("-")
                num_op[num].append("?")
            else:
                if num in num_op:
                    num_op[num].append("?")
                else:
                    num_op[num] = deque(["?"])


    # 3. TO SOLVE THE PROBLEM

    ans = []
    valid = set()
    stack = []

    for cmd, num in ops:

        now_cmd = num_op[num].popleft()
        ans.append(now_cmd)
        if now_cmd == "+":
            valid.add(num)
            stack.append(num)

        while stack:
            top = stack[-1]
            if num_op[top]:
                if num_op[top][0] == "-":
                    ans.append("-")
                    num_op[top].popleft()
                    valid.remove(top)
                    stack.pop()
                else:
                    break
            else:
                ans.append("-")
                valid.remove(top)
                stack.pop()

    print("".join(ans))