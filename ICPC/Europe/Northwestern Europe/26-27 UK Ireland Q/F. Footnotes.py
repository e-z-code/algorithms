import sys
INF = float('inf')


# 1. TO GET THE INPUT AND EXTRACT THE FOOTNOTE

text = list(sys.stdin.readline().strip())

alphabet_cnt = 0
for character in text:
    if character != "(" and character != ")":
        alphabet_cnt += 1

if alphabet_cnt % 3 != 0:
    print("impossible")
else:

    footnotes = []

    stack = []
    for idx in (range(len(text))):
        character = text[idx]
        if character == "(":
            stack.append((character, idx))
        elif character == ")":
            now_cnt = 0
            while stack:
                last_character, last_idx = stack.pop()
                if last_character == "(":
                    if now_cnt == alphabet_cnt // 3:
                        footnotes.append((last_idx, idx))
                    else:
                        stack.append((str(now_cnt), INF))
                    break
                else:
                    if last_character.isalpha():
                        now_cnt += 1
                    else:
                        now_cnt += int(last_character)
        else:
            if len(stack) != 0:
                stack.append((character, idx))


    # 2. TO SOLVE THE PROBLEM

    if len(footnotes) < 2:
        print("impossible")
    else:
        s1, e1 = footnotes[0]
        s2, e2 = footnotes[1]
        if s1 < s2:
            footnote1 = "".join(text[s1+1:e1])
            footnote2 = "".join(text[s2+1:e2])
            text[s2:e2+1] = "[2]"
            text[s1:e1+1] = "[1]"
            print("".join(text))
            print("[1]", footnote1)
            print("[2]", footnote2)
        else:
            footnote1 = text[s2+1:e2]
            footnote1[s1-s2-1:s1-s2+(e1-s1)] = "[2]"
            footnote2 = "".join(text[s1+1:e1])
            text[s2:e2+1] = "[1]"
            print("".join(text))
            print("[1]", "".join(footnote1))
            print("[2]", footnote2)