import sys
sys.stdin = open("/Users/seokkyuhong/dev/python/algorithm/연습/input.txt","r")

#n 명의 이름/국어/영어/수학
#정렬
#국어 점수가 감소하는 순서
#국어 점수가 같으면 영어점ㅅ가 증가하는
#국어, 영어 같으면 수학점ㅁ수가 감소
#점수 같으면 이름 사전순

n = int(input())

arr = []
for i in range(n):
    name, a, b, c = input().split()
    arr.append([int(a), int(b), int(c), name])

# print(arr)
sort_arr = sorted(arr, key = lambda x : (-x[0], x[1], -x[2], x[3]))
# print(sort_arr)

for i in sort_arr:
    print(i[3])

