"""
2178
미로찾기 문제
완전탐색
!!!!!!!!!!!!!bfs!!!!!!!!!!!!
행렬 != (x,y)
"""

import sys
from collections import deque

n,m = map(int, input().split())  # (n,m) : 도착 위치

mat = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]  #미로 생성

#위, 오른쪽, 아래, 왼쪽 순
col_movement = [0,1,0,-1]
row_movement = [-1,0,1,0]

#rstrip() : 오른쪽 공백문자 제거
#탐색 우선순위 : 오른쪽, 아래
# cnt = 1 칸수로 세면 문제점 : 길이 막혀서 돌아와야될 때 잘못된 값 도출 -> 그때그때 값을 저장해야됨
q = deque()
q.append((0,0))
while (q):
    row,col = q.popleft()

    #동서남북 탐색, 경로 있는지 확인
    for i in range(4):
        d_row = row + row_movement[i]
        d_col = col + col_movement[i]

        if 0<= d_row < n and 0<= d_col < m and mat[d_row][d_col] == 1:
            q.append((d_row,d_col))
            mat[d_row][d_col] = mat[row][col] + 1
            
print(mat[n-1][m-1])