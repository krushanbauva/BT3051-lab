#BT3051 Assignment 3a
#Roll number: BE17B037
#Collaborators: none
#Time: 30:00

import networkx as nx
import matplotlib.pyplot as plt

def RegularLattice(n, k):
    G = nx.Graph()
    nodes = [i for i in range(1, n+1)]
    G.add_nodes_from(nodes)
    for i in range(0, n):
        for j in range(1, k+1):
            G.add_edge(nodes[i], nodes[i-j])
    nx.draw(G, with_labels = True)

if __name__ == '__main__':
    RegularLattice(50,3)
