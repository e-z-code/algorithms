import sys


# 1. TO GET THE INPUT

band_cnt, people_cnt, min_people = map(int, sys.stdin.readline().split())

crowd_cnt = [0 for band in range(band_cnt)]
crowds = [[] for band in range(band_cnt)]

see_cnt = []
to_see = []

for person in range(people_cnt):
    favorite_cnt = int(sys.stdin.readline())
    see_cnt.append(favorite_cnt)
    favorites = list(map(int, sys.stdin.readline().split()))
    to_see.append(favorites)
    for idx in range(favorite_cnt):
        favorites[idx] -= 1
    for favorite in favorites:
        crowd_cnt[favorite] += 1
        crowds[favorite].append(person)


# 2. TO SOLVE THE PROBLEM

join_band = set([band for band in range(band_cnt)])
join_people = set([person for person in range(people_cnt)])

while True:

    changed = False

    cancel = []
    for band in join_band:
        if crowd_cnt[band] < min_people:
            cancel.append(band)
            changed = True
    for band in cancel:
        join_band.remove(band)
        for person in crowds[band]:
            see_cnt[person] -= 1

    cancel = []
    for person in join_people:
        if see_cnt[person] * 2 < len(to_see[person]):
            cancel.append(person)
            changed = True
    for person in cancel:
        join_people.remove(person)
        for band in to_see[person]:
            crowd_cnt[band] -= 1

    if not changed:
        break

if len(join_band) == 0:
    print("impossible")
else:
    print("possible")
    ans = list(join_band)
    print(len(ans))
    for idx in range(len(ans)):
        ans[idx] += 1
    print(" ".join(map(str, ans)))