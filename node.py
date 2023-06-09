#define a node in python
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
    """input:self,data
        output:null
        insert a child node to the tree
    """
    def insert(self,data):
        if self.data is None:
            self.data=data
        else:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
                    
"""input:root
    output:all node in order
    show all node in order
    we use recursion when we see that a process is repeating and it shows a pattern in it.
"""
def inOrderPrint(r):
    if r is None:
        return None
    else:
        inOrderPrint(r.left)
        print(r.data,end=" ")
        inOrderPrint(r.right)

"""input:root
    output:all node in order
    show all node in pre order
"""
def inPreOrderPrint(r):
    if r is None:
        return None
    else:
        print(r.data,end=" ")
        inPreOrderPrint(r.left)
        inPreOrderPrint(r.right)
"""input:root
    output:all node in order
    show all node in post order
"""
def inPostOrderPrint(r):
    if r is None:
        return None
    else:
        print(r.data,end=" ")
        inPostOrderPrint(r.right)
        inPostOrderPrint(r.left)

"""input:Node r
    output: list d
    make an adjacent list d of all node in r
"""        
def makeList(r):
    if r is None:
        return None
    else:
        d[r.data]=[]
        makeList(r.left)
        if r.left is not None:
            d[r.data].append(r.left.data)
        if r.right is not None:
            d[r.data].append(r.right.data)
        makeList(r.right)
        
    return d
"""input:List al
    output:list visited
    make all node and his chilren level by level in queue then pop the parent and continue
"""
def bfs(al):
    queue=['g']
    visited=[]
    while queue:
        node=queue.pop(0)
        visited.append(node)
        for elt in al[node]:
            queue.append(elt)
    print(visited)
    

    return visited
"""input:list al
    output:list visited
    go through a tree using dfs
"""           
def dfs(al):
    stack=['g']
    visited=[]
    while stack:
        node=stack.pop()
        if node  not in visited:
            visited.append(node)
            [stack.append(x) for x in al[node]]
    return visited

"""input: list al, value key to search
    output:True(founded) or False(not founded)
    search a element in a tree using dfs
"""
def search(al,key):
    stack=['g']
    visited=[]
    found=False
    while stack:
        node=stack.pop()
        if node==key:
            return True
        if node not in visited:
            visited.append(node)
            [stack.append(x) for x in al[node]]
    return found
#creating the tree
if __name__=="__main__":
    root=Node('g')
    root.insert('c')
    root.insert('b')
    root.insert('a')
    root.insert('e')
    root.insert('d')
    root.insert('f')
    root.insert('i')
    root.insert('h')
    root.insert('j')
    root.insert('k')
    """ inOrderPrint(root)
        inPreOrderPrint(root)
        inPostOrderPrint(root)
    """
    d={}
    aList=makeList(root)
    for elt in aList:
        print(elt,":",aList[elt])
    bfs(aList)
    print(search(aList, "f"))
    
    
    
