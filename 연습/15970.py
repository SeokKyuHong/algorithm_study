import sys
sys.stdin = open("/Users/seokkyuhong/dev/python/algorithm/연습/input.txt","r")

n = int(input())

arr = [[] for _ in range(n)]

# 색깔을 인덱스로 갖는 2중 리스트 생성
for i in range(n):
    position, color = map(int, input().split())
    arr[color-1].append(position)

# 같은 색의 리스트 솔팅
for i in arr:
    i.sort()

result = 0
for j in range(len(arr)):
    for i in range(len(arr[j])):
        # 같은색이 두개밖에 없다면 별도 처리
        if len(arr[j]) == 2:
            result += (arr[j][i+1] - arr[j][i]) *2
            break
        
        # 첫번째 점일때는 한방향의 거리만 계산
        if i == 0:
            result += (arr[j][i+1] - arr[j][i])
        # 마지막이면 별도 처리하고 break
        elif arr[j][i] == arr[j][-1]:
            result += (arr[j][i] - arr[j][i-1])
            break
        # 양쪽의 길이를 비교하여 작은 값으로 계산
        elif (arr[j][i] - arr[j][i-1]) >= (arr[j][i+1] - arr[j][i]):
            result += (arr[j][i+1] - arr[j][i])
        else:
            result += (arr[j][i] - arr[j][i-1])


print(result)