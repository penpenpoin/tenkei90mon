N = int(input())
#つながっている街のリスト
connect_city_list = [[]for i in range(N)]
for i  in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    connect_city_list[int(a)].append(b)
    connect_city_list[int(b)].append(a)

#dfs
ans = 0
def dfs(start):
    global ans
    num = 0
    stack = [start]
    seen = [start]
    while stack:
        node = stack.pop()
        num += 1
        for i in connect_city_list[node]:
            if not i in seen:
                stack.append(i)
                seen.append(i)
        ans = max(ans,num)

        

for i in range(N):
    if len(connect_city_list[i]) == 1:
        dfs(i)


print(ans+1)


""""
city = []
n = int(input())-1
#町が道とつながっている数を格納するリスト
city_connect_num = [0] * n
city_connect = [[]]

for i in range(n):
    city.append(list(map(int,input().split())))
    city_connect_num[city[i][0]] += 1
    city_connect_num[city[i][1]] += 1
    city_connect[city[i][0]].append(city[i][1]) 
    city_connect[city[i][1]].append(city[i][0])
    


longest_road = 0
seen = []
temp = 0
#DFS?を使って町の道をたどり最大値をlongest_roadに代入
def dfs(start):
    temp += 1
    seen.append(start)
    way = city_connect[start]
    w = way.pop()
    if w not in seen:
        if not way:

        while way:
                dfs(w)
        



#町が1本の道でつながっているところからすべての道をたどる
for i in range(n):
    if city_connect_num[i] == 1:
        while True:
            for j in range(n):
                if city[j][0] == 1
        break


print(longest_road+1)"""