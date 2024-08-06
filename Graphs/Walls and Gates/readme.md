# Walls and Gates

## Description

You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.


Question Link: [Leetcode 286](https://leetcode.com/problems/walls-and-gates/description/)

---
## Solution

It is very similar to the [Rotting Oranges](https://github.com/rohan527/myleetcode/tree/main/Graphs/Rotting%20Oranges) question. Here, we first iterate through the whole grid to find the locations of the gates and add their indices to a dequeue. 

While there are elements in the dequeue, you pop an element, you then find it's neighbors that exist in the grid, and if the current value in the neighbor cell is greater than closest distance, you change the value to the closest distance. To get the closest distance, it will be the value in the popped location from the deque plus one. Since gates are represnted by 0, we don't need a global value to keep a track of the closest distance. 

---

[Neetcode Solution Video](https://youtu.be/e69C6xhiSQE)