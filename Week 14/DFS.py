from collections import deque as stack

# Depth first search algorithm
def findPath(Start, Goal):
  # Stack for DFS because it is First-In/Last-Out (FILO)
  open = stack()
  open.append(Start)
  closed = set() # set is used becuase it is efficient for checking if a given node is in the collection because it hashes the data for O(1) for insertion, lookup
  visited = [] # to keep track of path

  while open:
    current = open.pop()
    visited.append(current) 
    if current == Goal:
      return visited

    closed.add(current)
    successors = current.get_vertex() # get list of successors
    successors.sort(reverse = True) # reorder successors in alphabetical order
    for each in successors: 
      if each not in closed: # add successors to open, so long as they have not been visited
         open.append(each)