import sys
from fractions import Fraction


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

berry_cnt, sugar_cnt, water_cnt = map(Fraction, sys.stdin.readline().strip().split())

units = [Fraction(berry_cnt, 12), Fraction(sugar_cnt, 12), Fraction(water_cnt, 40)]
need_unit = max(units)

ans = [str(float(need_unit * 12 - berry_cnt)), str(float(need_unit * 12 - sugar_cnt)), str(float(need_unit * 40 - water_cnt))]
print(" ".join(ans))
