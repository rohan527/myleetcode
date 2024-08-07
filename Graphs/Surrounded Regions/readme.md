# Surrounded Regions

## Description

You are given an `m x n` matrix `board` containing letters `'X'` and `'O'`, capture regions that are surrounded:

- Connect: A cell is connected to adjacent cells horizontally or vertically.

- Region: To form a region connect every `'O'` cell.

- Surround: The region is surrounded with `'X'` cells if you can connect the region with `'X'` cells and none of the region cells are on the edge of the board.

A surrounded region is captured by replacing all `'O'`s with `'X'`s in the input matrix board.

Question Link: [Leetcode 130](https://leetcode.com/problems/surrounded-regions/description/)

---
## Solution

First, go through all the boubdaries and find the `'O'`s and convert these `'O'`s and the ones neighboring it to some different character. 

Then traverse through the whole grid and convert all the `'O'`s to `'X'` and the different character back to `'O'`. 

---

[Neetcode Solution Video](https://youtu.be/9z2BunfoZ5Y)