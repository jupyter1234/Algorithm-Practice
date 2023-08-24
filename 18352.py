"""
bfs
도시개수 : n
도로개수 : m
거리정보 : k
출발도시 : x
"""
import sys
from collections import deque

n,m,k,x = map(int,sys.stdin.readline().split())

mat = [[] for _ in range(n+1)] #도시끼리 연결유무 저장
dist = [-1] * (n+1)
dist[x] = 0
#visited = [False] * (n+1) #방문유무 저장 필요없음
q = deque()
q.append(x)
for _ in range(m): 
    i,j = map(int,sys.stdin.readline().split())
    mat[i].append(j)
cnt = 1
while q and cnt < m:
    src = q.popleft()
    for i in mat[src]: #경로 존재
        if dist[i] == -1:
            dist[i] = dist[src] + 1
            q.append(i)
    cnt += 1
cnt_dis = 0
for i in range(1,n+1):
    if dist[i] == k:
        cnt_dis += 1
        print(i)
if cnt_dis == 0:
    print(-1)
