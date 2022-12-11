import sys
import heapq
sys.stdin = open("/Users/seokkyuhong/dev/python/algorithm/연습/input.txt","r")

n = int(input())
cards = []
for i in range(n):
    heapq.heappush(cards, int(input()))

sum = 0
for i in range(n-1):
    cmp = heapq.heappop(cards) + heapq.heappop(cards)
    cards.append(cmp)
    sum += cmp
print(sum)