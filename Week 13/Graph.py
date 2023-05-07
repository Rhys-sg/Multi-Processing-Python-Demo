import graphics

def makeWindow(nodes, results):
  marked = set() # keeps track of what already has a line
  win = graphics.GraphWin("Screen", 1920, 1080) # create screen

  for current in nodes:
    # circle
    newcircle = current.get_circle()
    newcircle.setFill("pink")
    newlabel = graphics.Text(newcircle.getCenter(), current)

    # sets up vertecies for each node, does not repeat vertecies
    for each in current.get_vertex():
      if each not in marked:
        newline = graphics.Line(newcircle.getCenter(), each.get_circle().getCenter())
        marked.add(current)
        newline.draw(win)
    
    # draws circles then labels
    newcircle.draw(win)
    newlabel.draw(win)

  for i in range(len(results)):
    results[i].get_circle().setFill("light blue")
    win.getMouse() # pause for click in window
    results[i].get_circle().setFill("yellow")

  win.close()