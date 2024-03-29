N = int(input())
connection_city_list = [[] for i in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    connection_city_list[a-1].append(b-1)
    connection_city_list[b-1].append(a-1)

def bfs(city_num):
    que = [city_num]
    seen = [0] * N
    depth = [0]*N
    depth[city_num] = 1
    while que:
        node = que.pop()
        seen[node] = 1
        for n in connection_city_list[node]:
            if  seen[n] == 0:
                que.append(n)
                depth[n]= depth[node] + 1
    return depth

print(max(bfs(max(enumerate(bfs(0)),key=lambda x:x[1])[0])))
