import sys

#bottom up 방식
"""
n = int(input())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] #걸리는 기간, 비용 순서대로 입력

dp = [0 for _ in range(n+1)] #최대 수익 저장

for i in range(n): #bottom up
    for j in range(i+table[i][0],n+1):
        if dp[j] < dp[i] + table[i][1] :
            dp[j] = dp[i] + table[i][1]

print(dp[n])
"""
#topdown 방식
n = int(input())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]

#이건 좀 이해 안 됨