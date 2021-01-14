import time

N, M = map(int,input().split())
#2 dimension array intializing
#map = [[] for _ in range(N)]

#Empty list
graph = []
for i in range(N):
    graph.append(list(map(int,input())))

def DFS(x,y):

    # Exception
    if x < 0 or y < 0 or x >=N or y >= M :
        return False

    if graph[x][y] == 0 :
        graph[x][y] = 1
        DFS(x-1,y)
        DFS(x,y-1)
        DFS(x+1,y)
        DFS(x,y+1)
        #True일때 0인 node 들의 묶음으로 counting
        return True

    #if graph[x][y] !=0
    return False


result = 0

for i in range(N):
    for j in range(M):
        if DFS(i,j) == True:
            result +=1

print(result)

## def 함수 내에서 if 조건문에 따른 return을 설정하는 idea
## Exception handling
