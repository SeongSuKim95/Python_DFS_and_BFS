#MAZE
from collections import deque

# N,M = map(int,input().split())
#
# maze= []
# for i in range(N):
#    maze.append(list(map(int,input())))

N = 5
M = 6
maze = [[1,0,1,0,1,0],[1,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]

#Using BFS -> searching nearby node -> queue 사용

#Direction

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):

    queue = deque()
    queue.append((x,y)) # starting point
    #Queue에서 좌표 뽑을때 x, y = queue.popleft()

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                #Exception case
                continue

            if maze[nx][ny] == 0:
                continue

            elif maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                #maze[x][y] = 지금까지 온 거리

                queue.append((nx,ny))

    print(maze)
    return maze[N-1][M-1]

print(bfs(0,0))