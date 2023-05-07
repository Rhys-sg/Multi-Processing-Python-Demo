import Node

def nodes_from_txt(file):
  # keeps a list of all nodes found in text file
  listofnodes = [] 

  # dictionary to retrieve node based off name of node, used for setting up vertecises 
  node_dict = {} 

  # opens text file and splices lines based on commas
  # first loop initializes nodes to dictionary and list
  with open(file) as txt:
    txtDocument = [item.split(", ") for item in txt.readlines()]
    for line in txtDocument:
      node_dict.update({line[0] : Node.Node(line[0], int(line[1]), int(line[2]))}) # * operator takes those indexs and uses them as parameters
      listofnodes.append(node_dict[line[0]])

    # second loop initializes vertices between nodes
    # loops through each line, then assigns a vertex for 
    # each of their 4th to last entries (vertices)
    for i in range(len(txtDocument)):
      for j in txtDocument[i][3:]:
          listofnodes[i].set_vertex(node_dict[j[:1]]) # "[:1]" is used to get rid of the \n
  
  txt.close()
  return listofnodes