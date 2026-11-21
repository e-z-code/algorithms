import sys


# 1. TO GET THE INPUT

round_cnt, gate_cnt = map(int, sys.stdin.readline().split())

gates = []
for round_idx in range(round_cnt):

    now_gates = list(map(str, sys.stdin.readline().strip().split()))

    cmd = []
    if now_gates[0] == "+":
        cmd.append(0)
    else:
        cmd.append(1)

    cmd.extend(sorted(list(map(int, now_gates[1:]))))
    gates.append(cmd)


# 2. TO SOLVE THE PROBLEM

ans = [1 for idx in range(gate_cnt)]

for cmd in gates:
    for idx in range(gate_cnt):
        if cmd[0] == 0:
            ans[idx] += cmd[idx+1]
        else:
            ans[idx] *= cmd[idx+1]

print(sum(ans))