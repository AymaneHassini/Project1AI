# 8 Puzzle Game with Heuristics

This repository contains the implementation of an 8-puzzle game solver using various heuristics. The project is part of the CSC 4301 - Introduction to Artificial Intelligence course.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Heuristics Implemented](#heuristics-implemented)
- [Results and Analysis](#results-and-analysis)
- [Conclusion](#conclusion)


## Introduction

The 8-puzzle game is a classic problem in artificial intelligence where the objective is to rearrange randomly shuffled tiles on a 3x3 grid, numbered 1 through 8 with one empty space, to reach a specific goal configuration. This project explores the implementation, evaluation, and comparison of different techniques to solve the 8-puzzle game using A* search algorithm with various heuristics.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/8-puzzle-heuristics.git
   cd 8-puzzle-heuristics
2-Install the required dependencies:
 ```bash
pip install -r requirements.txt
```
## 3- Usage
To run the solver, execute the following command:
```bash
python main.py
```
This will run the 8-puzzle solver using A* search algorithm with different heuristics and compare their performance.

## 4-Heuristics Implemented

Number of Misplaced Tiles: Counts the number of tiles not in their goal position.
Sum of Euclidean Distances: Calculates the Euclidean distance for each tile from its goal position.
Sum of Manhattan Distances: Computes the sum of the horizontal and vertical distances each tile needs to move to reach its goal position.
Number of Tiles Out of Row and Column: Counts the number of tiles that are not in their correct row or column.
Results and Analysis
## 5- Results and Analysis
The performance of each heuristic is evaluated based on three metrics:

Fringe Size: The number of nodes kept in memory during the search.
Number of Expanded Nodes: The total number of nodes explored.
Tree Depth: The depth of the search tree when the goal is found.
Summary of Findings
Manhattan Distance heuristic consistently resulted in the smallest fringe size, indicating lower memory usage and better space efficiency.
Euclidean Distance and Manhattan Distance heuristics had similar performance in terms of the number of expanded nodes, both being more efficient than the other heuristics.
All heuristics showed similar average tree depths, which is expected as they are all admissible heuristics used with A* search, leading to optimal solutions.
Conclusion
## 6-Conclusion 
The Sum of Manhattan Distances heuristic was found to be the most effective for the 8-puzzle problem, providing a good balance between accuracy and resource efficiency. While all implemented heuristics are admissible and produce optimal solutions, Manhattan Distance offers the best performance in practical scenarios for this specific problem.
