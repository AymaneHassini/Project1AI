# search.py


"""
In search.py, we implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import numpy as np
class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]
# def depthFirstSearch(problem):
#     """Search the deepest nodes in the search tree first."""

#     #states to be explored (LIFO). holds nodes in form (state, action)
#     frontier = util.Stack()
#     #previously explored states (for path checking), holds states
#     exploredNodes = np.zeros(shape=(1, 9), dtype=np.uint8)
#     #exploredNodes = set()
#     #define start node
#     startState = problem.getStartState()
#     startNode = (startState, [])
    
#     frontier.push(startNode)

#     # initializing counter for expended nodes
#     expanded_node = 0
#     # initializing fringe size
#     fringe_size = 0

#     index = 0
    
#     while not frontier.isEmpty():
        
#         frontier_size = len(frontier.list)
        
#         if frontier_size > fringe_size:
#             fringe_size = frontier_size        

        
#         #begin exploring last (most-recently-pushed) node on frontier
#         currentState, actions = frontier.pop()
#         #currentStatetoNumpy(currentState)
#         currentState_array = currentStatetoNumpy(currentState)
        
#         # if currentState not in exploredNodes:
#         if not np.any(np.all(exploredNodes == currentState_array, axis=1)):
#             #mark current node as explored
#             #exploredNodes.add(currentState)
#             if exploredNodes.shape[0] == 1:
#                 exploredNodes[0] = currentState_array
#                 index += 1
#             else:
#                 exploredNodes = np.resize(exploredNodes, (exploredNodes.shape[0] + 1, 9))
#                 exploredNodes[index] = currentState_array
#                 index += 1

#             if problem.isGoalState(currentState):
#                 return actions, expanded_node, frontier_size, len(actions)
#             else:
#                 #increment the expanded nodes counter
#                 expanded_node+=1

#                 #get list of possible successor nodes in 
#                 #form (successor, action, stepCost)
#                 successors = problem.getSuccessors(currentState)
                
#                 #push each successor to frontier
#                 for succState, succAction, succCost in successors:
#                     newAction = actions + [succAction]
#                     newNode = (succState, newAction)
#                     frontier.push(newNode)
            
#                 frontier_size = len(frontier.list)

#         del currentState

#     return actions, expanded_node, frontier_size, len(actions) 
def depthFirstSearch(problem):
    """Search the deepest nodes in the search tree first."""

    #states to be explored (LIFO). holds nodes in form (state, action)
    frontier = util.Stack()
    #previously explored states (for path checking), holds states
    exploredNodes = []
    #define start node
    startState = problem.getStartState()
    startNode = (startState, [])
    
    frontier.push(startNode)

    # initializing counter for expended nodes
    expanded_node = 0

    # initializing fringe size
    fringe_size = 0
    
    while not frontier.isEmpty():

        frontier_size = len(frontier.list)
        
        if frontier_size > fringe_size:
            fringe_size = frontier_size 

        #begin exploring last (most-recently-pushed) node on frontier
        currentState, actions = frontier.pop()

        if currentState not in exploredNodes:

            #mark current node as explored
            exploredNodes.append(currentState)
         
            if problem.isGoalState(currentState):
                return actions, expanded_node, fringe_size, len(actions)
            else:

                #    increment the expanded nodes counter
                expanded_node += 1  
                #get list of possible successor nodes in 
                #form (successor, action, stepCost)
                successors = problem.getSuccessors(currentState)
                
                #push each successor to frontier
                for succState, succAction, succCost in successors:
                    newAction = actions + [succAction]
                    newNode = (succState, newAction)
                    frontier.push(newNode)

                frontier_size = len(frontier.list)
        
        
    return actions, expanded_node, fringe_size, len(actions)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    #to be explored (FIFO)
    frontier = util.Queue()
    
    #previously expanded states (for cycle checking), holds states
    exploredNodes = set()
    
    startState = problem.getStartState()
    startNode = (startState, [], 0) #(state, action, cost)
    
    frontier.push(startNode)
     # initializing counter for expended nodes
    expanded_node = 0
    # initializing fringe size
    fringe_size = 0
    while not frontier.isEmpty():
        frontier_size = len(frontier.list)
        
        if frontier_size > fringe_size:
            fringe_size = frontier_size 
        #begin exploring first (earliest-pushed) node on frontier
        currentState, actions, currentCost = frontier.pop()
        
        if currentState not in exploredNodes:
            #put popped node state into explored list
            exploredNodes.add(currentState)

            if problem.isGoalState(currentState):
                return actions,expanded_node, fringe_size, len(actions)
            else:
                #increment the expanded nodes counter
                expanded_node += 1
                #list of (successor, action, stepCost)
                successors = problem.getSuccessors(currentState)
                
                for succState, succAction, succCost in successors:
                    newAction = actions + [succAction]
                    newCost = currentCost + succCost
                    newNode = (succState, newAction, newCost)

                    frontier.push(newNode)

    return actions, expanded_node, fringe_size, len(actions)
        
def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    #to be explored (FIFO): holds (item, cost)
    frontier = util.PriorityQueue()

    #previously expanded states (for cycle checking), holds state:cost
    exploredNodes = {}
    
    startState = problem.getStartState()
    startNode = (startState, [], 0) #(state, action, cost)
    
    frontier.push(startNode, 0)
    # initializing counter for expended nodes
    expanded_node = 0
    # initializing fringe size
    fringe_size = 0
    while not frontier.isEmpty():
        frontier_size = len(list(frontier.heap))
        
        if frontier_size > fringe_size:
            fringe_size = frontier_size 
        #begin exploring first (lowest-cost) node on frontier
        currentState, actions, currentCost = frontier.pop()
        
        if (currentState not in exploredNodes) or (currentCost < exploredNodes[currentState]):
            #put popped node's state into explored list
            exploredNodes[currentState] = currentCost

            if problem.isGoalState(currentState):
                return actions,expanded_node, fringe_size, len(actions)
            else:
                #increment the expanded nodes counter
                expanded_node += 1
                
                #list of (successor, action, stepCost)
                successors = problem.getSuccessors(currentState)
                
                for succState, succAction, succCost in successors:
                    newAction = actions + [succAction]
                    newCost = currentCost + succCost
                    newNode = (succState, newAction, newCost)

                    frontier.update(newNode, newCost)

    return actions, expanded_node, fringe_size, len(actions)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    #to be explored (FIFO): takes in item, cost+heuristic
    frontier = util.PriorityQueue()

    exploredNodes = set()  # holds state

    startState = problem.getStartState()
    startNode = (startState, [], 0) #(state, action, cost)

    frontier.push(startNode, 0)
    
    # initializing counter for expended nodes
    expanded_node = 0
    
    # initializing fringe size
    fringe_size = 0

    while not frontier.isEmpty():
        
        frontier_size = len(list(frontier.heap))
        
        if frontier_size > fringe_size:
            fringe_size = frontier_size 

        #begin exploring first (lowest-combined (cost+heuristic) ) node on frontier
        currentState, actions, currentCost = frontier.pop()

        #put popped node into explored set
        exploredNodes.add(currentState)

        if problem.isGoalState(currentState):
            return actions, expanded_node, fringe_size, len(actions)

        else:
            #increment the expanded nodes counter
            expanded_node += 1
            
            
            #list of (successor, action, stepCost)
            successors = problem.getSuccessors(currentState)

            #examine each successor
            for succState, succAction, succCost in successors:
                newAction = actions + [succAction]
                newCost = problem.getCostOfActions(newAction)
                newNode = (succState, newAction, newCost)

                #check if this successor has been explored
                already_explored = succState in exploredNodes

                #if this successor not explored, put on frontier and explored set
                if not already_explored:
                    frontier.push(newNode, newCost + heuristic(succState, problem))
                    exploredNodes.add(succState)

    return actions, expanded_node, fringe_size, len(actions)
def currentStatetoNumpy(currentState):
        array = np.empty(9, dtype=np.uint8)
        
        index = 0
        for line in str(currentState).split("\n")[1:-1:2]:

            for number in line.split("|")[1:-1]:
                
                if number.isspace():
                    array[index] = 0
                else:
                    array[index] = int(number)
                index += 1


        return array


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
