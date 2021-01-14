#Adjacency matrix : 2D matrix for node and edge

INF = 99999
graph = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]
#Adjacency list : list of adjacent node for each node
# 2D list which has 3 Rows
graph = [[] for _ in range(3)]
# Making empty 2D list

print(graph)

#Information for node 0
graph[0].append((1,7))
graph[0].append((2,5))

#Information for node 1
graph[1].append((0,7))

#Information for node 2
graph[2].append((0,5))

##두 방식의 차이:

# Adjacent matrix는 node간 모든 관계를 저장하므로 node 걔수가 많을 수록 메모리를 불필요하게 낭비하게 된다.
# Adjacent list는 연결된 정보만을 저장하므로 메모리를 효율적을 사용한다. 대신, 특정한 두 node가 연결되어 있는지에 대한 정보를 얻는 속도가 느리다.


## DFS ----> Using stack (Recursive function)

def dfs(graph,v,visited):
    #v = node number
    #Current node visited
    visited[v] = True
    print(v, end=' ')#v print 후 ' ' 추가

    for i in graph[v]: # node v 와 이어져 있는 node를 adjacent list에서 찾아 순회
        if not visited[i]: #visited[v]가 False라면
            dfs(graph,i,visited)

#Adjacent list
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

visited = [False] * 9 # [False,False,False,False,False,False,False,False,False] list 생성법

dfs(graph,2,visited)

# DFS 는 stack을 이용한다.
# 2D empty list 만드는 법, dfs 구현법, [False]*9 표현, end = ' '를 통한 출력 설정

