#mathematician representation
#G=(V,E) v:vertices
from collections import namedtuple

Graph=namedtuple("Graph", ["nodes","edges","is_directed"])



def adjacency_dict(graph):
    """
    Args:
        graph (Graph): 
        Returns the adjacency list representation of the graph.
    """
    adj={node:[] for node in graph.nodes}
    for edge in graph.edges:
        node1,node2=edge[0],edge[1]
        adj[node1].append(node2)
        if not graph.is_directed:
            adj[node2].append(node1)
    return adj

def adjacency_matrix(graph):
    """
    Args:
        graph (Graph): 
        Returns the adjacency matrix of the graph.
        Assumes that graph.nodes is equivalent to range(len(graph.nodes))
    """
    adj=[[0 for node in graph.nodes]for node in graph.nodes]
    for edge in graph.edges:
        node1,node2=edge[0],edge[1]
        adj[node1][node2]+=1
        if not graph.is_directed:
            adj[node2][node1]+=1
    return adj

def degrees(graph):
    """
    Args:
        graph (Graph): Returns a dictionary of degrees for each node in the graph
    """
    adj_list=adjacency_dict(graph)
    degrees={
        node:len(neighbors)
        for node, neighbors in adj_list.items()
    }
    return degrees

if __name__=="__main__":
    nodes=range(4)
    edges=[
        (0,1),
        (0,1),
        (0,2),
        (0,2),
        (0,3),
        (1,3),
        (2,3)
    ]
    G2=Graph(nodes,edges,is_directed=False)
    nodes=["A","B","C","D"]
    edges=[
    ("A","B"),
    ("A","B"),
    ("A","C"),
    ("A","C"),
    ("A","D"),
    ("B","D"),
    ("C","D"), 
    ]   

    G1=Graph(nodes, edges,is_directed=False)
    G3=Graph(nodes=range(3),edges=[(1,0),(1,2),(0,2)],is_directed=True)
    print(adjacency_matrix(G3))
    print(adjacency_dict(G3))
    