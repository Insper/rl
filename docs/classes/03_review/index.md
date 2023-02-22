# Implementations review

## Taxi driver review

The goal of this exercise was to implement a taxi-driver agent. A *taxi driver* agent can pick up a passenger at one point and leave this passenger at another point considering a specific map.

The most two common solutions were: 

* a **breadth search algorithm**. This algorithm is **complete** and **optimal**. However, this algorithm has a high memory requirement compared to other algorithms, and the time complexity can be high.

* an **A* algorithm** using the package `AStar` or from scratch. This algorithm uses the concept of **heuristics** to reduce memory and time. It is also **complete** and **optimal** since the heuristic used is **admissible**. The typical heuristics for this type of problem are **manhattan distance** and **euclidean distance**. Above there is a snapshot of the code using `AStar` package: 

```python
    def distance(n1, n2):
        return abs(n1[0]-n2[0]) + abs(n1[1]-n2[1])

    def cost(n, goal):
        return 1

    path1 = []
    if passenger != taxi:
        path1 = list(astar.find_path(taxi, passenger, neighbors_fnct=neighbors,
                    heuristic_cost_estimate_fnct=cost, distance_between_fnct=distance))
    path2 = list(astar.find_path(passenger, target, neighbors_fnct=neighbors,
            heuristic_cost_estimate_fnct=cost, distance_between_fnct=distance))
    return path1 + path2
```

## Tic-tac-toe review

The goal of this exercise was to implement a tic-tac-toe agent that never loses the game - an agent able to play and win or draw the tic-tac-toe game against another agent, human or artificial.

In other to simulate the environment, each group used a specific environment from the [pettingzoo](https://pettingzoo.farama.org/environments/classic/tictactoe/) project. 

All groups used a **Min-Max** algorithm that is broadly used in competitive situations. According to one of the groups (Carlos Dip, Lucas Fukada and Breatriz Bernardinho), *"the minimax algorithm has a time complexity of $O(b^d)$, where $b$ is the number of branches to be evaluated at each state, and $d$ is the depth of the search. Since tic-tac-toe is a very simple, brief game, this is still possible to implement and run without any optimizations, however for a game like chess, the depth would need to be severely restricted to allow for real-time play. The space complexity is $O(bd)$ because of the recursive implementation of the move tree search"*.

*"...tic-tac-toe is very simple"* because $b$ and $d$ are equal to $9$. 

A few groups used the concept of the *utility function* to evaluate intermediated situations and other groups did not use a *utility function* because they rich the end of the game in each **Min-Max** search. 

