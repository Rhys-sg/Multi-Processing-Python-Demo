import graphics

def Draw_Nodes_And_Vertex(firstNode, lastNode, nodes, Dict, win):
  marked = set() # keeps track of what already has a line

  for current in nodes:
    # circle
    newcircle = current.get_circle()
    if ((current.__repr__() == firstNode.__repr__()) or (current.__repr__() == lastNode.__repr__())): # checks to see if current node is start or end of path
      newcircle.setFill("light grey")
    else:
      newcircle.setFill("white")
    newlabel = graphics.Text(newcircle.getCenter(), current)

    # add circle to dictionary 
    Dict.update({current.__repr__(): current})
    # sets up vertecies for each node, does not repeat vertecies
    for each in current.get_vertex():
      if each not in marked:
        newline = graphics.Line(newcircle.getCenter(), each.get_circle().getCenter())
        marked.add(current)
        newline.draw(win)
    
    # draws circles then labels
    newcircle.draw(win)
    newlabel.draw(win)
