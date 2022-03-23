p = int(input())
p0 = p

def computeSweetness(s):
    i = 0 # index
    sw = 0 # sweetness
    N = len(s)
    while i < N // 2:
        if s[i] != s[N - i - 1]:
            sw += 1
        i += 1
    return sw


while p > 0:
    n, k = [int(j) for j in input().split(' ')]
    s = input()

    min_n = abs(k - computeSweetness(s))

    print("Case #",p0 - p + 1,": ", min_n,sep='')
    p -= 1