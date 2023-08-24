"""
10773번
수를 부르다가 0이 나오면 가장 최근에 적은 수를 지움
stack 느낌!
"""

import sys

n = int(input())
arr = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0 :
        arr.append(x)
    else:
        arr.pop()
print(sum(arr))