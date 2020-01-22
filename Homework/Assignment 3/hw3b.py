#BT3051 Assignment 3b
#Roll number: BE17B037
#Collaborators: none
#Time: 1:30:00

import networkx as nx

def maze(MazeMatrix,start,finish):

    def MazeMatrix2Graph(MazeMatrix):
        MazeGraph = nx.Graph()
        for i in range(m):
            for j in range(n):
                if MazeMatrix[i][j] == 1:
                    MazeGraph.add_node((i, j))
                    if i-1>=0 and MazeMatrix[i-1][j]==1:
                        MazeGraph.add_edge((i, j), (i-1, j))
                    if j-1>=0 and MazeMatrix[i][j-1]==1:
                        MazeGraph.add_edge((i, j), (i, j-1))
        return MazeGraph

    def MazeAnswerBFS(MazeGraph,start,finish):
        queue = []
        distance = [[99999999 for i in range(n)] for j in range(m)]
        parent = [[(-1, -1) for i in range(n)] for j in range(m)]
        queue.append(start)
        (i, j) = start
        distance[i][j] = 0
        parent[i][j] = (i, j)
        for node_1 in queue:
            (i1, j1) = node_1
            for node_2 in list(MazeGraph.adj[node_1]):
                (i2, j2) = node_2
                if (distance[i1][j1] + 1) < distance[i2][j2]:
                    queue.append((i2, j2))
                    distance[i2][j2] = distance[i1][j1] + 1
                    parent[i2][j2] = node_1
        shortest_path = []
        (i, j) = finish
        while(not parent[i][j]==(i, j)):
            shortest_path.append((i, j))
            (i, j) = parent[i][j]
        shortest_path.append((i, j))
        shortest_path = shortest_path[::-1]
        return shortest_path

    def MazeComponentsDFS(MazeGraph):
        stack = []
        components = []
        count = 0
        Visited = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if Visited[i][j] == 0 and (i, j) in list(MazeGraph.nodes):
                    count = count+1
                    stack.append((i, j))
                    Visited[i][j] = 1
                    individual_component = []
                    while(len(stack)!=0):
                        node_1 = stack.pop()
                        individual_component.append(node_1)
                        for node_2 in list(MazeGraph.adj[node_1]):
                            (i2, j2) = node_2
                            if (Visited[i2][j2] == 0):
                                stack.append(node_2)
                                Visited[i2][j2] = 1
                    components.append(individual_component)
        return components
    
    m = len(MazeMatrix)
    n = len(MazeMatrix[0])
    
    G = MazeMatrix2Graph(MazeMatrix)
    a = MazeAnswerBFS(G,start,finish)
    b = MazeComponentsDFS(G)

    print(a)
    print(b)

if __name__ == '__main__':
    #DO NOT MODIFY THE FOLLOWING
    hw3bmaze=    [[1,0,1,1,0,1],
                  [1,1,0,0,0,0],
                  [0,1,0,1,1,1],
                  [0,1,1,1,0,1],
                  [1,0,0,1,1,1],
                  [1,1,0,0,0,1],
                  [0,0,1,1,0,1]]

    hw3bstart=(0,0)
    hw3bfinish=(6,5)
    print(maze(hw3bmaze,hw3bstart,hw3bfinish))

#output for this example should be:
#[(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5), (6, 5)]
#[[(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5), (6, 5), (3, 5), (2, 5), (2, 4), (2, 3)], [(0, 2), (0, 3)], [(0, 5)], [(4, 0), (5, 0), (5, 1)], [(6, 2), (6, 3)]]
