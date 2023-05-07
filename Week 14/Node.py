import graphics

# A node that has a list of its vertices. 
# Adding a vertex to between nodes "a" and "b" will add "a" to b's list of vertices and vice versa
# can return list of node's vertices
class Node:
    def __init__(self, name, x, y):
      self.vertex = []
      self.name = name
      self.x = x
      self.y = y
      self.circle = graphics.Circle(graphics.Point(x, y), 20)

    # adds other to this nodes list of connections
    # and adds this node to the other nodes list of connections
    # ensures that verticies can be travelled in either direction
    # if statement avoides repeat entries
    def set_vertex(self, other):
      if other not in self.vertex:
        self.vertex.append(other)
        other.vertex.append(self)

    # returns the list of nodes connected to this one
    def get_vertex(self):
      return self.vertex

    # returns a refrence to the circle object used to
    # visualize this node
    def get_circle(self):
      return self.circle
    
    # returns coordinates
    def get_coordinates(self):
      return [self.x, self.y]

    # returns string name
    # used as printable and comparable representation of the object
    def __repr__(self):
      return self.name

    # compares node's name to other node's name
    # used for sorting nodes
    def __lt__(self, other):
      return self.name < other.name
    
    