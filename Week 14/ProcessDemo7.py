# imports to include aspects from previous iteration
import DFS
import readFromFile
import Vector_Math
import Visual

import multiprocessing
import time
# Import Zelle graphics.py library
from graphics import *

# Simulate motion tracking position data
# Writes current "x" coordinate value into shared dictionary.
# Dictionary key "stop" signals when the program should stop.
def playerMotion(dictionary):
    # To simulate player movement about the graph, define a list
    # of (x,y) coordinate points.
    # These points just represent how the player moves around in the graph.
    # These points are not the computed navigation path from start to goal.
    # This list of points will be replaced by live streaming motion-tracking coordinates.

    # changed to use coordinates from .txt file
    coordList = dictionary.get("coordList")

    index = 0
    dictionary["stop"] = False
    while index < len(coordList):
        # On each iteration write the current coordinate x,y to the dictionary.
        dictionary["x"] = coordList[index][0]
        dictionary["y"] = coordList[index][1]
        
        time.sleep(2)
        index = index + 1
    dictionary["stop"] = True
  
# Update Zelle graphics display
# Compute navigation guidance signals to player
def update_graph_display(dictionary):
    window = GraphWin("Animation Demo", 1920, 1080, autoflush = False)

    # Create dot to visualize player position.
    # dictionary.get("NodePathway")[0] returns [x,y] for start position
    visualizeplayer_dot = createDot(dictionary.get("CircleDict"), dictionary.get("PlayerDotRad"), dictionary.get("NodePathway")[0].get_coordinates(), "pink", "Player")
    player_text = Text(visualizeplayer_dot.getCenter(), "Player")
    player_text.setSize(9)

    # Create dot to visualize each node.
    Visual.Draw_Nodes_And_Vertex(dictionary.get("NodePathway")[0], dictionary.get("NodePathway")[-1], dictionary.get("AllNodes"), dictionary.get("CircleDict"), window)


    # Create Zelle graphics shapes to draw the graph with nodes and edges.
    
    # Draw graph shapes to make them visible in the window.
    
    # Initialize current navigation way point from solution path list stored in dictionary.
    # Player will try to navigate towards the current way point.

    index = dictionary.get("index_of_current_node_path_entry")

    while not dictionary["stop"]:
        # wait so that the program doesn't run too quickly
        time.sleep(0.5)
        
        if index >= len(dictionary.get("NodePathway")):
             print("Congratulations! You reached the goal.")
             return
        
        # Get current player (x,y) coordinates on the graph.
        x = dictionary["x"]
        y = dictionary["y"]     

        # prints feedback and next node
        print("You are at ", [x, y], ", going to node ", dictionary.get("NodePathway")[index], "at", dictionary.get("coordList")[index])

        # Compute relative turn direction and distance needed to move player
        # to reach the current navigation way point
        navigationDirections = Vector_Math.calculate_angle_distance([x, y], dictionary.get("coordList")[index], dictionary.get("user_heading"))

        # Print current player navigation directions.
        # index 1 = distance (float)
        # index 2 = degree (float)
        # index 3 = "left" / "right" / "StraightBehind" / "StraightForward" 
        print("Turn", navigationDirections[2], "to the" , navigationDirections[3], "and walk", navigationDirections[1])
        
        # Buzz haptic vest
        
        # Check if player position is close enough to the current way point.
        # If yes, then update current way point to be next way point along computed navigation path.
        
        # Repaint moving player dot in its new position.
        # Erase dot from old position.
        cP = visualizeplayer_dot.getCenter()
        visualizeplayer_dot.undraw()
        player_text.undraw()
        # Move dot to new (x,y) position
        # Zelle graphics only provides a method to increment x, y
        # so we must compute the displacement vector from current position
        # to the desired new position.
        visualizeplayer_dot.move(x - cP.getX(), y - cP.getY())
        player_text.move(x - cP.getX(), y - cP.getY())
        visualizeplayer_dot.draw(window)
        player_text.draw(window)
        # Repaint the Zelle graphics window 30-times per second.
        # This call repaints and pauses for 1/30th of a second.
        update(30)
        # update index to get next point, can't change dict:
        # dictionary.get("index_of_current_node_path_entry") += 1
        if(Vector_Math.get_distance([x,y], dictionary.get("coordList")[index]) <= dictionary.get("NodeDotRad")):
            index += 1
            dictionary.update({"index_of_current_node_path_entry" : index})

def createDot(CircleDict, rad, xy, color, Name):
    cp = Point(xy[0], xy[1])
    dot = Circle(cp, rad)
    # Fill interior of circle in given color
    dot.setFill(color)
    dot.setOutline("black")
    # add dot to shared dictionary
    CircleDict.update({Name : dot})
    return dot
  
if __name__ == '__main__':
    manager = multiprocessing.Manager()
    shared_dict = manager.dict()
    
    # Load graph from data text file.
    # Construct graph object
    # makes a list of nodes from txt document using nodes_from_txt function
    listofnodes = readFromFile.nodes_from_txt("C:/Users/rsore/Desktop/General/School/Whitman/(2) Sophmore/Semester 2/CS-481-B Independent Study/Week 13/document.txt")
    
    # Store graph into shared dictionary
    # make dictionary of the graph, then add it to the shared dictionary
    graph_dictionary = {}
    print("Here are the lists of Nodes:")
    for each in listofnodes:
        graph_dictionary.update({each.name : each})
        print(each)

    shared_dict["graphNodes"] = graph_dictionary

    # Prompt user to enter starting vertex in graph
    print("What node would you like to start at?")
    startingNodeName = input()
    
    # Prompt user to enter ending vertex in graph 
    print("What node would you like go to?")
    endingNodeName = input()   
    
    # Compute navigation path list of vertices in graph
    # nodePathway returns a list of node objects
    nodePathway = DFS.findPath(graph_dictionary[startingNodeName], graph_dictionary[endingNodeName]) # both startingNodeName and endingNodeName need to be valid
    

    # Store path list, coordinate list, index, and initial heading into shared dictionary
    shared_dict.update({"AllNodes" : listofnodes})
    shared_dict.update({"NodePathway" : nodePathway})
    shared_dict.update({"coordList" : [each.get_coordinates() for each in nodePathway]})
    # print(shared_dict.get("coordList"))
    shared_dict.update({"index_of_current_node_path_entry" : 1})
    shared_dict.update({"user_heading" : [1, 0]})
    shared_dict.update({"PlayerDotRad" : 20})
    shared_dict.update({"NodeDotRad" : 20})
    CircleDict = {}
    shared_dict.update({"CircleDict" : CircleDict})
    



    process_playerMotion = multiprocessing.Process(target=playerMotion, args=[shared_dict])
    process_update_graph_display = multiprocessing.Process(target=update_graph_display, args=[shared_dict])
  
    process_playerMotion.start()
    process_update_graph_display.start()
  
    process_playerMotion.join()
    process_update_graph_display.join()