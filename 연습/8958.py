import sys
sys.stdin = open("/Users/seokkyuhong/dev/python/algorithm/input.txt","r")

# 'O'가 나오면  1씩 더함
# 'x'가 나오면 초기화

t = int(input())

arr = []
for i in range(t):
    count = 0
    sum1 = 0
    arr.append(input())
    for j in arr[i]:
        if 'O' == j:
            count +=1
        else:
            count = 0
        sum1 += count
    print(sum1)

