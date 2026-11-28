import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

length = int(sys.stdin.readline())

done = [0 for idx in range(length)]

while sum(done) != length:

    target_idx = 0
    for idx in range(length):
        if not done[idx]:
            target_idx = idx
            break

    print(target_idx+1, 1)
    sys.stdout.flush()
    result = int(sys.stdin.readline())
    if result == length:
        sys.exit()

    best_idx = 0
    best_length = result
    for idx in range(1, length):
        print(idx, idx+1)
        sys.stdout.flush()
        result = int(sys.stdin.readline())
        if result == length:
            sys.exit()
        if result > best_length:
            best_idx = idx
            best_length = result

    print(length, best_idx+1)
    sys.stdout.flush()
    result = int(sys.stdin.readline())
    if result == length:
        sys.exit()

    done[target_idx] = 1
    val = done.pop(target_idx)
    done.insert(best_idx, val)
