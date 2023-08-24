"""
1003
실버3
피보나치 함수에서 0과 1이 출력되는 횟수 구하기
"""

#그냥 피보나치 쓰면 되나,,? 했는데 시간제한 있음! 일반적인 재귀로는 못 구함 다이나믹?
def fibo(num,memo,zero_one):
    if num <= 1:
        return num
    else:
        if memo[num] > 0:
            return memo[num]
        memo[num] = fibo(num-1,memo,zero_one) + fibo(num-2,memo,zero_one)
        zero_one[0][num] = zero_one[0][num-1] + zero_one[0][num-2]
        zero_one[1][num] = zero_one[1][num-1] + zero_one[1][num-2]
        return memo[num]
    
def top_down(x):
    if x == 0:
        zero_one = [[1],[0]]
    else: 
        zero_one = [[0] * (x+1) for _ in range(2)] #[i][0] = 0 출력횟수 저장, [i][1] = 1 출력횟수 저장 
        zero_one[0][0] = 1
        zero_one[0][1] = 0
        zero_one[1][0] = 0
        zero_one[1][1] = 1
    memo = [0] * (x+1)  #top-down 값 저장
    fibo(x,memo,zero_one)
    return zero_one

n = int(input())
for _ in range(n):
    x = int(input())
    res = top_down(x)
    print(res[0][x],res[1][x])