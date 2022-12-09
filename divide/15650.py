import sys
sys.stdin = open("/Users/seokkyuhong/dev/python/algorithm/divide/input.txt","r")

n, m = map(int, input().split())

arr = []
def dfs(index):

    if len(arr) == m:
        print(' '.join(map(str, arr)))

    for i in range(1, n+1):
        if i >= index:              # 중복을 없에는 재귀 조건
            arr.append(i)
            dfs(i+1)
            arr.pop()
dfs(1)