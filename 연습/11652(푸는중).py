import sys
sys.stdin = open("/Users/seokkyuhong/dev/python/algorithm/연습/input.txt","r")

n = int(input())

arr = [int(input()) for _ in range(n)]

arr_t = sorted(arr)

m = 0
if abs(arr_t[0]) > abs(arr_t[-1]):
    m = abs(arr_t[0])
else:
    m = abs(arr_t[-1])

cards_m = [0 for _ in range(m+1)]
cards_p = [0 for _ in range(m+1)]

for i in arr:
    if i >= 0:
        cards_p[i] += 1
    else:
        cards_m[-(i)] += 1

p_max = cards_p.index(max(cards_p))
m_max = cards_m.index(max(cards_m))

if p_max >= m_max:
    print(p_max)
else :
    print(-(m_max))
