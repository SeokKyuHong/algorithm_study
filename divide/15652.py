import sys
sys.stdin = open("/Users/seokkyuhong/dev/python/algorithm/divide/input.txt","r")

n, m = map(int, input().split())

arr = []
def dfs(index):
    if len(arr) == m:                  # 재귀 끝 지점
        print(' '.join(map(str, arr)))
        return
    
    for i in range(index, n+1):     # 반복문의 시작이 이전 i값부터 되도록
        arr.append(i)               
        dfs(i)            
        arr.pop()

dfs(1)                   # 반복조건을 위해 인자 넘김