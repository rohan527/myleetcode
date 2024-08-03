# Number of Islands

## Description

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


Question Link: [Leetcode 200](https://leetcode.com/problems/number-of-islands/description/)

---
## Solution

In the grid, we need to record 1 peice of information of one point, grid[i][j], i.e., if grid[i][j] has been visited or not.
We initialize the check matrix with all False. It means none of the elements in the check matrix has been visited.

If one point grid[i][j] has not been visited, check[i][j] == False, it means we haven't count this point into one islands.
If one point grid[i][j] has been visited, check[i][j] == True, it means we already count this point into one islands.
Search function:

Search function:
Each time you call search function, the search function will end until all the neighbors of grid[i][j] have value "1" been visited, i.e., those points are labeled True in check matrix.

---

[Neetcode Solution Video](https://youtu.be/pV2kpPD66nE)