# Rotting Oranges

## Description

You are given an m x n grid where each cell can have one of three values:

- 0 representing an empty cell,
- 1 representing a fresh orange, or
- 2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Question Link: [Leetcode 994](https://leetcode.com/problems/rotting-oranges/description/)

---
## Solution

If the grid is empty, return -1.

First, we have to know which oranges in the grid are rotten. So traverse the grid, and append the indices of the oranges that are rotten in the deque. Also count the number of oranges that are fresh. This will help us in exiting BFS sooner if all oranges are already rotten and in the end when we have to return an answer.

Now, we can keep a track of the minutes starting from zero. While there are rotten oranges in the deque and there are fresh oranges, add 1 to the answer and create a for loop for the length of the current deque. Essentially, we are finding out all the fresh oranges next to the rotten oranges and making them all rotten for the first minute. And then we keep doing this while there are elements in the dequeue and we have fresh oranges. 

After the dequeue is empty, return -1 if there are fresh oranges else return the minutes. 

---

[Neetcode Solution Video](https://youtu.be/y704fEOx0s0)