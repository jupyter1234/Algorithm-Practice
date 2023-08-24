"""
1로 만들기 실버 3
최소 연산 횟수 구하기 dp?
1. 3으로 나누기
2. 2로 나누기
3. 1 빼기
시간제한이 걸림...
"""
#큰 수에서 1을 만드는 게 아니라 1에서 큰 수로 올라가는 거라면..?   => bottom up 방식
"""
dp를 써야하는 이유
만약 10을 만드려고 한다면 10 -> 5 -> 4 -> 2 -> 1 이 방식도 있지만 10 -> 9 -> 3 -> 1 이 방식이 더 최소의 연산을 사용한다. 그렇기에 n까지의 모든 수에 그 수로
도달하기까지 최소의 횟수를 구하고 그 최소에서 최소의 연산을 하면 된다.
n이 되기 위해선 (n-1) 에서 1을 더하거나 2나 3을 곱해서 n이 되는 두 개의 방식이 있다.
"""
# n = int(input())
# dp = [0] * (n+1)
# for i in range(2,n+1): 
#     if i % 3 == 0 :
#         dp[i] = min(dp[i-1] + 1, dp[i//3] + 1)
#     elif i % 2 == 0:
#         dp[i] = min(dp[i-1] + 1, dp[i//2] + 1)
#     else:
#         dp[i] = dp[i-1] + 1
# print(dp[n]) 
 
# -> 예외발생 케이스 구분 만약 3으로 나누는 경우가 2로 나누는 경우보다 더 오래 걸리는 경우에 대한 처리가 안 됨 모든 경우의 수를 다 시도해봐야됨
n = int(input())
dp = [0] * (n+1)
for i in range(2,n+1): 
    dp[i] = dp[i-1] + 1 #우선 1을 더해보고
    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i//3] + 1)  #3으로 나누는 경우가 더 최적이라면 값 변경
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
print(dp[n])


#top- down 방식 - 재귀
n = int(input())
dp = [-1] * (n+1)
dp[0] = 0
dp[1] = 0
#top- down 주의 할 점 n가 2와 3의 공배수를 경우 두 개 모두 비교해봐야함
def top_down(x):
    if dp[x] != -1:
        return dp[x]
    # if x % 2 == 0 and x % 3 == 0:
    #     dp[x] = min(top_down(x//3) + 1, top_down(x//2) + 1)
    elif x % 3 == 0:
        dp[x] = min(top_down(x//3) + 1, top_down(x-1) + 1)
    elif x % 2 == 0:
        dp[x] = min(top_down(x//2) + 1, top_down(x-1) + 1)
    else:
        dp[x] = top_down(x-1) + 1
    return dp[x]

print(top_down(n))