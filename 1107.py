"""
1105 리모컨 골드 1
주어진 채널로 이동하기 위해 버튼을 입력해야하는 최소 횟수 구하기
1. 고장난 경우가 없거나, 바로 이동가능한 경우
2. 시작채널인 100에서 +-로 이동가능한 경우
3. 모든 경우의 수 탐색
"""
import sys
input = sys.stdin.readline
n = int(input())
m = int(input()) #고장난 버튼의 개수
#고장난 버튼 입력 받기
if m == 0:
    br = []
else: 
    br = list(input().split()) #문자열 형태로 입력받기
    #100에서 플마로 가는 경우
min = abs(100 - n)

    #사용할 수 있는 번호로 이동하고 그 이후에 플마
for i in range(1000000):
    i = str(i)
    for x in range(len(i)):
        if i[x] in br: #갈 수 없는 경우
            break

        elif x == len(i)-1: #i가 입력가능한 경우
            res = abs(int(i) - n) + len(i)
            if (res < min):
                min = res
print(min)