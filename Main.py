import DFS
import readFromFile
import Node
import Graph

def main():
  # makes a list of nodes from txt document using nodes_from_txt function
  listofnodes = readFromFile.nodes_from_txt("C:/Users/rsore/Desktop/General/School/Whitman/(2) Sophmore/Semester 2/CS-481-B Independent Study/Week 10/Using Zelle v2/document.txt")

  # makes visual traversing from node b (first index) to node a (zeroth index)
  Graph.makeWindow(listofnodes, DFS.findPath(listofnodes[1], listofnodes[0])) 
  
main() 