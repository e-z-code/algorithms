import sys
problems = "ABCDEFGHIJKL"

# 1. PRE-PROCESSING

menu = {}
for problem in problems:
    menu["WrongProblem" + problem] = 100
    menu["SameProblem" + problem] = 30
    menu["UnreasonableLimitForProblem" + problem] = 5
    menu["WeakTestsForProblem" + problem] = 3
    menu["BadProblem" + problem] = 1
menu["UnreasonableProblemArrangement"] = 10


# 2. TO GET THE INPUT

test_cnt = int(sys.stdin.readline())

for test in range(test_cnt):

    review_cnt, key_score = map(int, sys.stdin.readline().split())

    score = 0
    for idx in range(review_cnt):
        review = sys.stdin.readline().strip()
        score += menu.get(review, 0)

    if key_score < score:
        print("Joker")
    else:
        print("Judger")