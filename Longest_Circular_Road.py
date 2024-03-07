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
    branching_num =[0 for i in range(N-1)]
    stack = [start]
    seen = [start]
    most_far = 1
    while stack:
        node = stack.pop()
        way_of_num = 0
        for i in connect_city_list[node]:
            if not i in seen:
                stack.append(i)
                seen.append(i)
                way_of_num += 1
        if way_of_num > 1:
            num +=1
            branching_num.append(num)
        if way_of_num == 1:
            num +=1
        elif way_of_num == 0:
            tmp = ans
            ans = max(num,ans)
            if not tmp == ans:
                most_far = node
            num = branching_num.pop()
    return most_far
    
ppp = dfs(0)
dfs(ppp)
print(ans+1)
