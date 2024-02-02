import search
import random

# Module Classes

class EightPuzzleState:
    """
    The Eight Puzzle is described in the course textbook on
    page 64.

    This class defines the mechanics of the puzzle itself.  The
    task of recasting this puzzle as a search problem is left to
    the EightPuzzleSearchProblem class.
    """

    def __init__( self, numbers ):
        """
          Constructs a new eight puzzle from an ordering of numbers.

        numbers: a list of integers from 0 to 8 representing an
          instance of the eight puzzle.  0 represents the blank
          space.  Thus, the list

            [1, 0, 2, 3, 4, 5, 6, 7, 8]

          represents the eight puzzle:
            -------------
            | 1 |   | 2 |
            -------------
            | 3 | 4 | 5 |
            -------------
            | 6 | 7 | 8 |
            ------------

        The configuration of the puzzle is stored in a 2-dimensional
        list (a list of lists) 'cells'.
        """
        self.cells = []
        numbers = numbers[:] # Make a copy so as not to cause side-effects.
        numbers.reverse()  # ensures order when init cells from numbers
        for row in range( 3 ):
            self.cells.append( [] )
            for col in range( 3 ):
                self.cells[row].append( numbers.pop() )
                if self.cells[row][col] == 0:
                    self.blankLocation = row, col

    def isGoal( self ):
        """
          Checks to see if the puzzle is in its goal state.

            -------------
            |   | 1 | 2 |
            -------------
            | 3 | 4 | 5 |
            -------------
            | 6 | 7 | 8 |
            -------------

        >>> EightPuzzleState([0, 1, 2, 3, 4, 5, 6, 7, 8]).isGoal()
        True

        >>> EightPuzzleState([1, 0, 2, 3, 4, 5, 6, 7, 8]).isGoal()
        False
        """
        current = 0
        for row in range( 3 ):
            for col in range( 3 ):
                if current != self.cells[row][col]:
                    return False
                current += 1
        return True

    def legalMoves( self ):
        """
          Returns a list of legal moves from the current state.

        Moves consist of moving the blank space up, down, left or right.
        These are encoded as 'up', 'down', 'left' and 'right' respectively.

        >>> EightPuzzleState([0, 1, 2, 3, 4, 5, 6, 7, 8]).legalMoves()
        ['down', 'right']
        """
        moves = []
        row, col = self.blankLocation
        if(row != 0):
            moves.append('up')
        if(row != 2):
            moves.append('down')
        if(col != 0):
            moves.append('left')
        if(col != 2):
            moves.append('right')
        return moves

    def result(self, move):
        """
          Returns a new eightPuzzle with the current state and blankLocation
        updated based on the provided move.

        The move should be a string drawn from a list returned by legalMoves.
        Illegal moves will raise an exception, which may be an array bounds
        exception.

        NOTE: This function *does not* change the current object.  Instead,
        it returns a new object.
        """
        row, col = self.blankLocation
        if(move == 'up'):
            newrow = row - 1
            newcol = col
        elif(move == 'down'):
            newrow = row + 1
            newcol = col
        elif(move == 'left'):
            newrow = row
            newcol = col - 1
        elif(move == 'right'):
            newrow = row
            newcol = col + 1
        else:
            raise "Illegal Move"

        # Create a copy of the current eightPuzzle
        newPuzzle = EightPuzzleState([0, 0, 0, 0, 0, 0, 0, 0, 0])
        newPuzzle.cells = [values[:] for values in self.cells]
        # And update it to reflect the move
        newPuzzle.cells[row][col] = self.cells[newrow][newcol]
        newPuzzle.cells[newrow][newcol] = self.cells[row][col]
        newPuzzle.blankLocation = newrow, newcol

        return newPuzzle

    # Utilities for comparison and display
    def __eq__(self, other):
        """
            Overloads '==' such that two eightPuzzles with the same configuration
          are equal.

          >>> EightPuzzleState([0, 1, 2, 3, 4, 5, 6, 7, 8]) == \
              EightPuzzleState([1, 0, 2, 3, 4, 5, 6, 7, 8]).result('left')
          True
        """
        for row in range( 3 ):
            if self.cells[row] != other.cells[row]:
                return False
        return True

    def __hash__(self):
        return hash(str(self.cells))

    def __getAsciiString(self):
        """
          Returns a display string for the maze
        """
        lines = []
        horizontalLine = ('-' * (13))
        lines.append(horizontalLine)
        for row in self.cells:
            rowLine = '|'
            for col in row:
                if col == 0:
                    col = ' '
                rowLine = rowLine + ' ' + col.__str__() + ' |'
            lines.append(rowLine)
            lines.append(horizontalLine)
        return '\n'.join(lines)

    def __str__(self):
        return self.__getAsciiString()
    '''
    heuristic function logic
    '''
    #1st heuristic: no. of misplaced
    def misplacedTiles(self):
        """
        Returns the number of misplaced tiles compared to the goal state.
        """
        misplaced_count = 0
        current = 0

        for row in range(3):
            for col in range(3):
                if current != self.cells[row][col] and current!= 0:
                    misplaced_count += 1
                current += 1
                 
        return misplaced_count
    #2nd heuristic: sum of eucleadian distances
    def sum_of_euclidean_distances(self):
        euclidean_sum = 0
        # Define the goal state as a 2D array
        goal_state = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]
        for row in range(3):
            for col in range(3):
                value = self.cells[row][col]
                if value != 0:
                   # Find the goal position (row, column) for the current value
                    for goal_i in range(3):
                     if value in goal_state[goal_i]:
                        goal_j = goal_state[goal_i].index(value)
                        break
                    
                    euclidean_sum += ((row - goal_i) ** 2 + (col - goal_j) ** 2) ** 0.5
                
        return euclidean_sum
    #3rd heuristic: sum of manhattan distances
    def sum_of_manhattan_distances(self):
        # Initialize the distance sum to 0
        distance_sum = 0

        # Define the goal state as a 2D array
        goal_state = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]

        # Iterate over each cell in the puzzle
        for i in range(3):
            for j in range(3):
                # Get the value of the current cell
                value = self.cells[i][j]

                if value != 0:
                   # Find the goal position (row, column) for the current value
                    for goal_i in range(3):
                     if value in goal_state[goal_i]:
                        goal_j = goal_state[goal_i].index(value)
                        break

                    # Calculate Manhattan distance and add to the total sum
                    distance_sum += abs(goal_i - i) + abs(goal_j - j)

        # Return the final sum of Manhattan distances
        return distance_sum
    #4th heuristic: number of tiles out of row + ... out of column
    def tiles_out_of_row_and_column(self, goal_state=[[0, 1, 2], [3, 4, 5], [6, 7, 8]]):
        """
        Returns the sum of the number of tiles out of their correct row positions
        and the number of tiles out of their correct column positions with respect to the goal state.
        """
        out_of_row_count = 0
        out_of_column_count = 0

        for row in range(3):
            for col in range(3):
                value = self.cells[row][col]
                if value != 0:  # Skip the empty space
                    goal_row, goal_col = None, None

                    # Find the goal position in the goal state
                    for i in range(len(goal_state)):
                        if value in goal_state[i]:
                            goal_row = i
                            goal_col = goal_state[i].index(value)
                            break

                    if goal_row is not None and goal_col is not None:
                        if row != goal_row:
                            out_of_row_count += 1

                        if col != goal_col:
                            out_of_column_count += 1
        #print(f"out of row:" + out_of_row_count + "out of column:" + out_of_column_count)
        return out_of_row_count + out_of_column_count
    
# TODO: Implement The methods in this class

class EightPuzzleSearchProblem(search.SearchProblem):
    """
      Implementation of a SearchProblem for the  Eight Puzzle domain

      Each state is represented by an instance of an eightPuzzle.
    """
    def __init__(self,puzzle):
        "Creates a new EightPuzzleSearchProblem which stores search information."
        self.puzzle = puzzle

    def getStartState(self):
        return puzzle

    def isGoalState(self,state):
        return state.isGoal()

    def getSuccessors(self,state):
        """
          Returns list of (successor, action, stepCost) pairs where
          each succesor is either left, right, up, or down
          from the original state and the cost is 1.0 for each
        """
        succ = []
        for a in state.legalMoves():
            succ.append((state.result(a), a, 1))
        return succ

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        return len(actions)
    # function that pushes the heuristic 1 value to the state
    def heuristic1(self, state, problem=None):
        """
        Returns the heuristic value for a given state using the misplaced tiles heuristic.
        """
        return state.misplacedTiles()
    # function that pushes the heuristic 2 value to the state
    def heuristic2(self, state, problem=None):
        """
        Returns the heuristic value for a given state using the sum of Manhattan distances heuristic.
        """
        return state.sum_of_manhattan_distances()
    # function that pushes the heuristic 3 value to the state
    def heuristic3(self, state, problem=None):
        """
        Returns the heuristic value for a given state using the sum of euclidean distances heuristic.
        """
        return state.sum_of_euclidean_distances()
    # function that pushes the heuristic 4 value to the state
    def heuristic4(self, state, problem=None):
        """
        Returns the heuristic value for a given state using the no. of tiles out of row/column heuristic.
        """
        return state.tiles_out_of_row_and_column()
    

EIGHT_PUZZLE_DATA = [[1, 0, 2, 3, 4, 5, 6, 7, 8],
                     [1, 7, 8, 2, 3, 4, 5, 6, 0],
                     [4, 3, 2, 7, 0, 5, 1, 6, 8],
                     [5, 1, 3, 4, 0, 2, 6, 7, 8],
                     [1, 2, 5, 7, 6, 8, 0, 4, 3],
                     [0, 3, 1, 6, 8, 2, 7, 5, 4]]

def loadEightPuzzle(puzzleNumber):
    """
      puzzleNumber: The number of the eight puzzle to load.

      Returns an eight puzzle object generated from one of the
      provided puzzles in EIGHT_PUZZLE_DATA.

      puzzleNumber can range from 0 to 5.

      >>> print loadEightPuzzle(0)
      -------------
      | 1 |   | 2 |
      -------------
      | 3 | 4 | 5 |
      -------------
      | 6 | 7 | 8 |
      -------------
    """
    return EightPuzzleState(EIGHT_PUZZLE_DATA[puzzleNumber])

def createRandomEightPuzzle(moves=100):
    """
      moves: number of random moves to apply

      Creates a random eight puzzle by applying
      a series of 'moves' random moves to a solved
      puzzle.
    """
    puzzle = EightPuzzleState([0,1,2,3,4,5,6,7,8])
    for i in range(moves):
        # Execute a random legal move
        puzzle = puzzle.result(random.sample(puzzle.legalMoves(), 1)[0])
    return puzzle

if __name__ == '__main__':
    puzzle = createRandomEightPuzzle(25)
    print('A random puzzle:')
    print(puzzle)

    # create the puzzle
    problem = EightPuzzleSearchProblem(puzzle)
    '''
    # printing the no. of misplaced tiles

    misplaced_tiles = puzzle.misplacedTiles()
    print(f"Number of misplaced tiles: {misplaced_tiles}")
    
    '''
    # printing sum of manhattan distances
    '''
    manhattan_distance = puzzle.sum_of_manhattan_distances()
    print(f"Sum of Manhattan distances: {manhattan_distance}")
    '''
    '''
    # printing sum of euclidean distances
    euclidean_distance_sum = puzzle.sum_of_euclidean_distances()
    print(f"Total Euclidean Distance: {euclidean_distance_sum}")
    '''
    #printing no. of misplaced row/column
    misplaced_row_col = puzzle.tiles_out_of_row_and_column()
    print(f"Tiles out of row and column: {misplaced_row_col}")
    '''
    # initializing the heuristic 1 function 
    heuristic_function1 = problem.heuristic1
    '''
    
    '''
    # initializing the heuristic 2 function 
    heuristic_function2 = problem.heuristic2
    '''
    '''
    # initializing the heuristic 3 function 
    heuristic_function3 = problem.heuristic3
    '''
     
     # initializing the heuristic 4 function 
    heuristic_function4 = problem.heuristic4

    path= search.aStarSearch(problem, heuristic_function4)

    """
    path = search.breadthFirstSearch(problem)
    """   
    print('A* found a path of %d moves: %s' % (len(path), str(path)))
    curr = puzzle
    i = 1
    for a in path:
        curr = curr.result(a)
        print('After %d move%s: %s' % (i, ("", "s")[i>1], a))
        print(curr)

        input("Press return for the next state...")   # wait for key stroke
        i += 1
