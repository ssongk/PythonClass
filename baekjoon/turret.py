# 백준 1002번 문제
import math
t=int(input())
for i in range(t):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    if x1==x2 and y1==y2:
        if r1==r2:
            print(-1)
            continue
        else:
            print(0)
            continue
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    if distance == r1+r2 or distance == abs(r1-r2):
        print(1)
        continue
    if distance > r1+r2 or distance<abs(r1-r2):
        print(0)
    elif distance < r1+r2:
        print(2)