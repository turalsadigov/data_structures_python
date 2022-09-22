graph = {
  'a': ['c', 'b'],
  'b': ['d', 'e'], 
  'c': ['f', 'g'], 
  'd': [], 
  'e':[],
  'f':[], 
  'g':[]}


graph2 = {
  'a': ['b', 'c'],
  'b': ['d'], 
  'c': ['e'], 
  'd': ['f'], 
  'e':[],
  'f':[]
}

# iterative approach
def DFprint(graph, starting_node):
    stack = [starting_node]
    res = []
    while stack:
        current = stack.pop()
        res.append(current)
        for neighbor in graph[current]:
            stack.append(neighbor)
    return res


# recursive approach
def DFprint (graph, starting_node):
   res = [starting_node]
   for neighbor in graph[starting_node]:
       res += DFprint(graph, neighbor)
   return res
  
DFprint(graph2, 'a')
 
