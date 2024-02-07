import sys
import pandas as pd
import os

from board import Board
from bfs import BFS



def main_BFS(scenario, output="./", csv_name="BFS_data.csv"):
    
    try:
        data_frame = pd.read_csv(os.path.join(output, csv_name))
        data_frame = data_frame.drop(columns=["Unnamed: 0"])
    except:
        data_frame = pd.DataFrame(columns=["path", "expanded_node", "fringe_size", "depth"])
    
    puzzle = Board(scenario)
    solution = BFS(puzzle)
    solution.solve()
    data_frame.loc[int(sys.argv[1])] = [str(solution.path), int(str(solution.nodes_expanded)), len(solution.frontier), int(str(solution.max_depth))]

        

    data_frame.to_csv(os.path.join(output, csv_name))
    

if __name__ == "__main__":
    scenarios_path="../scenarios/scenariosWM.csv"
    scenario = pd.read_csv(scenarios_path).to_numpy()[:,1:][int(sys.argv[1])]

    main_BFS(scenario, output="../results", csv_name="BFS_v2_data.csv")

