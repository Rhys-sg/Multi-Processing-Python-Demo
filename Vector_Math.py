import math

# recieves two vectors (a vector is a list of two numbers)
# returns scalar, not point or vector
# if a and b are unit length, a dot b = cosine(theta)
def dot(a, b):
    return a[0]*b[0] + a[1]*b[1]

# recieves two vectors
# return a vector that is the combination of the two vectors
# order does not matter
def add(a, b):
    return [a[0]+b[0] , a[1]+b[1]]

# recieves two vectors
# return a vector that is the result of a-b
# destination point is first (a)
def sub(a, b):
    return [a[0]-b[0] , a[1]-b[1]]

# recieves one vector and resturns magnitude
def length(a):
    return math.sqrt(a[0]**2 + a[1]**2)

# recieves a vector
# return the unit-length
# equivlent vector
def normalize(a):
    leng = length(a)
    # if vector is [0,0], avoid deviding by 0 by returning a
    if (leng == 0): return a
    return [a[0]/leng, a[1]/leng]

# recieve heading vector, retrun right hang vector
def get_rightHand(a):
    return [a[1], -a[0]]

# Given an (x,y) point ptP and a vec_Heading, return what angle someone needs to turn and what distance they need to travel to get to ptA
def calculate_angle_distance(ptP, ptA, vec_Heading):
    vec_unit_Heading = normalize(vec_Heading)
    vec_unit_RightHand = get_rightHand(vec_unit_Heading)
    vec_toGoal = sub(ptA, ptP)
    vec_unit_toGoal = normalize(vec_toGoal)

    # calculate the radians based on the dot product of unit vector
    radians = math.acos(dot(vec_unit_toGoal, vec_unit_Heading))
    degrees = radians * (180/math.pi)

    distance = length(vec_toGoal)

    # find position of the goal in terms of unit heading and rigt and coordinates, assuming origin at ptP
    position = [dot(vec_unit_RightHand, vec_toGoal), dot(vec_unit_Heading, vec_toGoal)]

    # Check if a user needs to turn left, right, or straigt and how much based on degrees
    variance = 0 #.25
    if (position[0] < variance):
        TurnDirection = "Left"
    elif (position[0] > -variance):
        TurnDirection = "Right" 
    elif (position[1] < 0):
        TurnDirection = "StraightBehind" 
    else :
        TurnDirection = "StraightForward" 
    
    # position is the second point in human-coordinates
    return position, distance, degrees, TurnDirection