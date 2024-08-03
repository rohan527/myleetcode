# Max Area of Island

## Description

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.


Question Link: [Leetcode Number](https://leetcode.com/problems/max-area-of-island/description/)

---
## Solution

We iterate through grid, a 2D array, and if we find a cell in grid has value 1, first cell on an unexplored island, we start an area count (res) and mark this first cell as visited (with a -1) in grid.

A cell in the grid is connected to the first cell if there is a path of 1s from the first cell to the this cell. We explore recursively in each connected cell to this cell looking for values of 1.

If a connected cell is in the and its value is 1, we add it to the area for this island, mark it as visited, and keep exploring. If we get a 0 or -1, we consider that the base case for the recursion.

Once the island is completely explored, we determine whether the area of this island is greater than the those explored before. We continue the iteration thoughout the grid to determine the the max.

---

[Neetcode Solution Video](https://youtu.be/iJGr1OtmH0c)