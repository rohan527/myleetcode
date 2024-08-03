# Word Search II

## Description

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.


Question Link: [Leetcode Number](https://leetcode.com/problems/word-search-ii/description/)

---
## Solution

Okay this one was not easy. At all. 

To start with, we will first have to create a trie for the list of words. Here, at the end of the trie, we will add a new '#' key that will be equal to the word that is current being input.

Next, we will iterate over each character on the board, and check if that character does exist in the root hash map. If it does, we will call the dfs function on the indices and the root:

For the dfs function, since we already know that the first character does exist in the trie, we will check if there is a '#' in the hashmap too. If there is a '#', it means that we came across a word, and we can add it to our result list. 

Now, since the character we have come across is already visited, we will have to temporarily mark it as done.

We will have to check for all possible neigbors for the current position on the board. If the neighbor exists in the Trie, we will call dfs on the indices of this neighbor with this node. 

After going through all possible neighbors, we will return the first character value on the board to it's original character. 

IMP: In the dfs function, at the end, we can also remove the current node from the trie if it has no children. i.e. if the current node doesn't exist in the list of words, we can remove it so that we do not iterate over it multiple times in the next iterations. This is optional, but will make the code go faster. 

After iterating through all the positons on the board, return the result list


---

[Neetcode Solution Video](https://youtu.be/asbcE9mZz_U)