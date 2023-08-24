"""
(10x10)색종이 겹친 부분 넓이 구하기
입력값
색종이 개수 : n
시작점 x,y 좌표 (x,y)
진짜 단순하게 접근하면 됨! 100x100 모눈종이가 있다고 생각하고 그걸 색칠하면 됨 나중에 최종적으로 색칠된 부분만 세면됨(파이썬 .count())
굳이 수학적 접근 안해도 됨
"""
#101 X 101 생성 <- 0은 제외해야되니깐
mat = [[0 for _ in range(101)] for _ in range(101)] #인덱스 [0,_] [_,0] 은 없는 셈

# 0 : 흰색 1 : 검정색
n = int(input()) #색종이 개수
for _ in range(n):
    i,j = map(int,input().split())
    for x in range(10):
        mat[j+x][i:i+10] = [1,1,1,1,1,1,1,1,1,1]
cnt = 0
for i in range(1,101):
    cnt += mat[i].count(1)
print(cnt)