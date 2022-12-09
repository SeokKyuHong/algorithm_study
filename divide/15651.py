import sys
sys.stdin = open("/Users/seokkyuhong/dev/python/algorithm/divide/input.txt","r")

n, m = map(int, input().split())       

arr = []
def go():
    if len(arr) == m:           # 3.arr 리스트의 길이가 m이면 출력하고 회기
        print(' '.join(map(str,arr)))
        return
    
    for i in range(1, n+1):     # 1.출력 해야할 수가 1부터 n까지기 떄문에
        arr.append(i)           # 2.예를 들어 1이 처음 들어가고 해당 1을 기준으로 재귀를 돌며 반복
        go()
        arr.pop()               # 4.재귀가 들어갔다 나오면 1번째 인덱스 값 추출하여 다시 for 문을 돌게 한다. 

go()