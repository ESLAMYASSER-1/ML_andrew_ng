graph={
    "S":["A","B","D"],
    "A":["C"],
    "B":["D"],
    "D":["G"],
    "C":["D","G"],
    "G":[]
}

def alg(graph,start,goal):
    queue=[[start]]
    visited=[]
    
    while queue:
        path=queue.pop(0)
        node= path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes =graph.get(node,[])
            for node2 in adjacent_nodes:
                new_path =path.copy()
                new_path.append(node2)
                queue.append(new_path)
        
    print(queue,visited)
alg(graph,"S","G")


l1 = [1,2,3,4,5,6,7,8,9,10,11]
l2 = ["a","b","c","d","e","f","g","h","i","j",'h']

for (x,y)in zip(l1,l2):
    print(f"{x}{y}")

