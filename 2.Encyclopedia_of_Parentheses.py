N = input()
N = int(N)
ans = []

#立っているビットの数を数える
def count_bit(n):
    n = (n & 0b01010101010101010101010101010101) + ((n  & 0b10101010101010101010101010101010)>> 1)
    n = (n & 0b00110011001100110011001100110011) + ((n  & 0b11001100110011001100110011001100)>> 2)
    n = (n & 0b00001111000011110000111100001111) + ((n  & 0b11110000111100001111000011110000)>> 4)
    n = (n & 0b00000000111111110000000011111111) + ((n  & 0b11111111000000001111111100000000)>> 8)
    n = (n & 0b00000000000000001111111111111111) + ((n  & 0b11111111111111110000000000000000)>>16)
    return n

def check(s):
    s =  bin(s)[2:].zfill(N)
    r = 0
    l = 0
    for i in range(len(s)):
        if s[i] == '0':
            l += 1
        elif s[i] == '1':
            r += 1
        if l < r:
            return False
    if l == r:
        return True
    else:
        return False
            


#N桁の括弧の組み合わせを全て求める[(=0 )=1の二進数表記]
def all_combination(n):
    for i in range(2**(n//2-1)+1, 2**(n-1), 2): 
        if count_bit(i)==(n//2) and check(i) == True:
            ans.append(bin(i)[2:].zfill(n))

def bin_to_str(s):
    s = s.replace("0", "(")
    s = s.replace("1", ")")
    return s

if N == 2:
    print("()")
elif N % 2 == 0:
    all_combination(N)
    for i in ans:
        print(bin_to_str(i))
