import sys
from collections import deque
sys.stdin = open("/Users/seokkyuhong/dev/python/algorithm/연습/input.txt","r")

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in graph:
    i.sort()

# [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]

visited_1 = [False] * (n+1)
visited_2 = [False] * (n+1)

def dfs(start):
    visited_1[start] = True
    print(start, end = ' ')  
    for i in graph[start]:
        if not visited_1[i]:
            dfs(i)
        else:
            continue

dfs(v)

print()

q = deque()
def bfs(start):
    visited_2[start] = True
    q.append(start)
    while q:
        c = q.popleft()
        print(c, end = ' ')
        for i in graph[c]:
            if not visited_2[i]:
                visited_2[i] = True
                q.append(i)
            else:
                continue


bfs(v)
