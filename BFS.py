#BFS

from collections import deque

#BFS method

def bfs(graph,start,visited):
    queue = deque([start]) # 비어있는 queue 에 [start] node
    visited[start] = True
    while queue: # queue가 빌때까지 --> [] == False
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
        ]

visited = [False]*9
bfs(graph,1,visited)

# deque 사용법
#queue = deque()
#print(queue)

# [] == False
# a = [1,2,3,4]
# while a:
#     print(a.pop())
