import sys
sys.stdin = open("/Users/seokkyuhong/dev/python/algorithm/input.txt","r")

t = int(input())

arr = []
for i in range(t):
    x, y = map(int, input().split())
    arr.append((y,x))
arr.sort()
    
for i in arr:    
    print(i[1], i[0])
    