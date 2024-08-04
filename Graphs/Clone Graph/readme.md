# Clone Graph

## Description

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Question Link: [Leetcode 133](https://leetcode.com/problems/clone-graph/description/)

---
## Solution

To solve this problem we need two things:

BFS to traverse the graph
A hash map to keep track of already visited and already cloned nodes
We push a node in the queue and make sure that the node is already cloned. Then we process neighbors. If a neighbor is already cloned and visited, we just append it to the current clone neighbors list, otherwise, we clone it first and append it to the queue to make sure that we can visit it in the next tick.

---

[Neetcode Solution Video]()