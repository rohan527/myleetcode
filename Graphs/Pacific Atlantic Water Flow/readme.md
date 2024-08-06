# Pacific Atlantic Water Flow

## Description

There is an `m x n` rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the height above sea level of the cell at coordinate `(r, c)`.

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates `result` where `result[i] = [ri, ci]` denotes that rain water can flow from cell `(ri, ci)` to both the Pacific and Atlantic oceans.


Question Link: [Leetcode 417](https://leetcode.com/problems/pacific-atlantic-water-flow/description/)

---
## Solution

Instead of going with the flow or water, we can go against the flow of water. That is, we start from the shores of the two oceans, and go upstream i.e. when the height of the neighboring cell increases instead of decreasing. 

We simply create two sets, one for the cells we can reach upstream from the Atlantic and one for the Pacific. We add the shores, i.e. the left and top edge for the Pacific and the right and the bottom edge for the Atlantic to two lists or deques. We call both these lists on a function that will return a set of the cells we can reach from the list of shores we sent. The answer will be the intersection of these two sets. 

In the function, we will use BFS to visit all the neighboring cells first and add the cells that follow the condition i.e. the height should be more than the current cell.

---

[Neetcode Solution Video](https://youtu.be/s-VkcjHqkGI)