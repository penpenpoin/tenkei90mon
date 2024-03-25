N,L = map(int,input().split())
K = int(input())
A = list(map(int,input().split()))

def donyoku_method(minim):
    now_here = 0
    separate_num = 0
    for a in A:
        if a-now_here >= minim:
            separate_num += 1
            now_here = a
            if separate_num == K and L-a >=minim:
                return True
    return False

def waru2kiriage(num):
    return ((num+2-1)//2)
def two_tree_serch():
    right = waru2kiriage(L)
    left = 0
    while not(right == left):
        print(right)
        if donyoku_method(right):
            tmp = right
            right = tmp + waru2kiriage(tmp - left)
            left = tmp
        else:
            tmp = right
            right = left + waru2kiriage(tmp-left)
            if tmp ==right:
                break
    return left

print(two_tree_serch())
