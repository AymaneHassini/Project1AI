import numpy as np
import pandas as pd
import search
from tqdm import tqdm
import os
from eightpuzzle import EightPuzzleState, EightPuzzleSearchProblem, createRandomEightPuzzle

def create_scenarios(number_scenarios = 700, name = "scenarios.csv"):
    
    """create different scenarios for EightPuzzle Game
        if given no argument a scenario with 700 initial state is created
    Args:
        number_scenarios (int): MAX 9!-1
        name (str): this takes the path name of the generated scenario.csv file
    """
    # scenarios will not exceed the # of possible initial states
    if number_scenarios > 0 and number_scenarios < 362880:  
        # creating goal state through ranging from 0 to 8
        goal =  np.arange(9, dtype=np.uint8)
        # if user do not enter the extension, it makes it .csv automatically
        if not name.endswith(".csv"):
            name += ".csv"
        # make a 2d array with 700 cell (number_scenario inputted) full with 0's
        scenarios = np.zeros((number_scenarios, 9), dtype=np.uint8)
        # initializing the scenarios indices
        scenario = 0
        # while we did not reach the number of cells filled yet
        while scenario != number_scenarios:
            # copy the goal and shuffle it
            scenario_random = goal.copy()
            np.random.shuffle(scenario_random)
            # if not reached the goal nor had a repeated scenario
            if not np.all(scenario_random == goal) and not np.all((scenarios == scenario_random)):
              # append unique scenario to already existing scenarios
                scenarios[scenario] = scenario_random
                scenario += 1
        # save the scnarios to the csv file
        pd.DataFrame(scenarios).to_csv(name)
    else:
        # if the user want more than possible permutation or impossible number of scenarios print: 
        print("Impossible to create that number of scenarios")


def create_scenarios_with_moves(number_scenarios = 700, name = "scenarios.csv", patience=50, moves = 25):
    
    scenario = 0
    patience_counter = 0
    scenarios = np.zeros(shape=(number_scenarios, 9), dtype=np.uint8)
    if number_scenarios > 0 and number_scenarios < 362880:  
        # creating goal state through ranging from 0 to 8
        goal =  np.arange(9, dtype=np.uint8)
        # if user do not enter the extension, it makes it .csv automatically
        if not name.endswith(".csv"):
            name += ".csv"
        while scenario != number_scenarios:

            if patience_counter > patience:
                moves += 1
                patience_counter = 0
                
            puzzle = createRandomEightPuzzle(moves=moves)
            scenario_random = search.currentStatetoNumpy(puzzle)
            if not np.all(scenario_random == goal) and not np.all((scenarios == scenario_random)):
                scenarios[scenario] = scenario_random
                scenario += 1
            else:
                patience_counter += 1
        # save the scnarios to the csv file
        pd.DataFrame(scenarios).to_csv(name)
    else:
        # if the user want more than possible permutation or impossible number of scenarios print: 
        print("Impossible to create that number of scenarios")
        
def automate_traversal(scenarios_path="scenarios.csv", output="./"):
    """
    Args:
        scenarios_path (str): path_csv
        output (str, optional): where to store the results
    """

    # list of standard search algorithms
    algos = [search.breadthFirstSearch, search.uniformCostSearch]
    algo_names =["BFS", "UCS"]
    # creating a list containing 4 data frames
    data_frames = [pd.DataFrame(columns=["path", "expanded_node", "fringe_size", "depth"]) for i in range(4)]
    # reading from the scenario.csv file
    scenarios = pd.read_csv(scenarios_path).to_numpy()[:,1:]
    # looping through all the scenarios and using tqdm for loading bar visualization
    for scenario_id in tqdm(range(len(scenarios))):
        # converting numpy array to list
        puzzle = EightPuzzleState(list(scenarios[scenario_id]))
        
        # create the puzzle
        problem = EightPuzzleSearchProblem(puzzle)

        # looping through standards search algos and saving results in data frames

        index = 0
        for algo in algos:
            data_frames[index].loc[len(data_frames[index].index)] = algo(problem)
            data_frames[index].to_csv(os.path.join(output, f"{algo_names[index]}_data.csv"))
            index += 1
    
    # # saving data frames to csv file
    # print("saving csv")
    # # looping through standards search algos and saving results in data frames
    # algo_names = ["BFS", "DFS", "UCS"]
    # for i in range(len(algo_names)):

    #     data_frames[i].to_csv(os.path.join(output, f"{algo_names[i]}_data.csv"))

    # main function: creating the scenarios by automation
if __name__ == '__main__':
    
    # create_scenarios(20, "scenariosUCS.csv")
    # create_scenarios_with_moves(number_scenarios=100, name = "scenariosWM.csv", patience=70, moves=15)
    automate_traversal(scenarios_path="../scenarios/scenariosWM.csv", output="../results")