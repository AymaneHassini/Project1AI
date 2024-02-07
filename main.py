import pandas as pd
from eightpuzzle import createRandomEightPuzzle, EightPuzzleSearchProblem
import search

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
    #misplaced_row_col = puzzle.tiles_out_of_row_and_column()
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
    #heuristic_function4 = problem.heuristic4

    #path = search.aStarSearch(problem, heuristic_function4)[0]

    """
    path = search.breadthFirstSearch(problem)
    """   
    #print('A* found a path of %d moves: %s' % (len(path), str(path)))
    path,expanded_nodes,fringe_size,depth=search.ucs(problem)
    print('BFS found a path of %d moves: %s' % (len(path), str(path)))
    print('Expanded Nodes:', expanded_nodes)
    print('Max Fringe Size:', fringe_size)
    print('Depth of Tree:', depth)
    curr = puzzle
    i = 1
    for a in path:
        curr = curr.result(a)
        print('After %d move%s: %s' % (i, ("", "s")[i>1], a))
        print(curr)

        input("Press return for the next state...")   # wait for key stroke
        i += 1
