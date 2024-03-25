H,W = map(int, input().split())
A = []
ans = []
for i in range(H):
    A.append(list(map(int,input().split())))

tate = []
yoko = []
for i in range(H):
    tmp = 0
    for j in range(W):
        tmp += A[i][j]
    tate.append(tmp)
for i in range(W):
    tmp = 0
    for j in range(H):
        tmp += A[j][i]
    yoko.append(tmp)

for i in range(len(tate)):
    for j in range(len(yoko)):
        print(tate[i]+yoko[j]-A[i][j],end=" ")
    print()
