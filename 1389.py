"""
1389 케빈 베이컨 게임
실버 1
"""
from collections import deque

n,m = map(int,input().split())
mat = [[False] * (n+1) for _ in range (n+1)]
inf = float("inf")
bacon = [inf] * (n+1) #베이컨수 저장

for _ in range(m):
    x,y = map(int, input().split())
    mat[x][y]= True
    mat[y][x] = True

#x->nxt
for i in range(1,n+1):
    q = deque()
    q.append(i)
    dist = [-1] * (n+1)
    dist[i] = 0 #i 시작점
    while(q):
        x = q.popleft()
        for nxt in range(1,n+1):
            if mat[x][nxt] == True and dist[nxt] == -1:
                #아직 방문하지 않은 도시
                dist[nxt] = dist[x] + 1
                q.append(nxt)

    #베이컨 수 구하기
    num = 0
    for w in range(1,n+1):
        if w!= i:
            num += dist[w]
    bacon[i] = num
min = inf
for j in range(1,n+1):
    if bacon[j] < min:
        min = bacon[j]
        min_index = j
print(min_index)