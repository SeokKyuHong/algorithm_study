import sys
sys.stdin = open("/Users/seokkyuhong/dev/python/algorithm/연습/input.txt","r")

n = int(input())

arr = {}

for i in range(n):
    a = int(input())
    if a in arr:
        arr[a] += 1
    else:
        arr[a] = 1

sort_arr = sorted(arr.items())

sort_arr.sort(key=lambda x:-x[1])
print(sort_arr[0][0])




# 메로리 초과...
# m = 0
# if abs(arr_t[0]) > abs(arr_t[-1]):
#     m = abs(arr_t[0])
# else:
#     m = abs(arr_t[-1])

# cards_m = [0 for _ in range(m+1)]
# cards_p = [0 for _ in range(m+1)]

# for i in arr:
#     if i >= 0:
#         cards_p[i] += 1
#     else:
#         cards_m[-(i)] += 1

# p_max = 0
# if max(cards_p) > max(cards_m):
#     p_max = cards_p.index(max(cards_p))
#     print(p_max)
# else:
#     p_max = cards_m.index(max(cards_m))
#     print(-p_max)

