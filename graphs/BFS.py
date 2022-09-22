graph = {
  'a': ['c', 'b'],
  'b': ['d', 'e'], 
  'c': ['f', 'g'], 
  'd': [], 
  'e':[],
  'f':[], 
  'g':[]}


graph2 = {
  'a': ['c', 'b'],
  'b': ['d'], 
  'c': ['e'], 
  'd': ['f'], 
  'e':[],
  'f':[]
}



# iterative approach
def BFprint(graph, starting_node):
    q = [starting_node]
    res = []
    while q:
      current = q.pop(0)
      res.append(current)
      for neighbor in graph[current]:
        q.append(neighbor)
    return res

    
BFprint(graph2, 'a')

      
