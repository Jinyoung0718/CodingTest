import sys
input = sys.stdin.readline

N, M = map(int, input().split()) 
lis = list(map(int, input().split()))

SUM = [0]
temp = 0

for i in lis:
    temp += i
    SUM.append(temp)

for _ in range(M):
    s, e = map(int, input().split())
    print(SUM[e] - SUM[s - 1])