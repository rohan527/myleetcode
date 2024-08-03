# Design Add and Search Words Data Structure

## Description

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

- WordDictionary(): Initializes the object.
- void addWord(word) Adds word to the data structure, it can be matched later.
- bool search(word): Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


Question Link: [Leetcode 211](https://leetcode.com/problems/design-add-and-search-words-data-structure/description/)

---
## Solution

{Similar to Implement Trie}

The add functions is very similar to Trie. For search, the caveat is the ".". Since, if you come across the period, you will have to consider every child node, the best way to do this would be DFS. 

Here, you pass to the DFS function, the current node and inedex:
- if index is length of word, then return if it is the last character in the word
- if the character at index is a ".", call DFS on each of the nodes and return True if a single one passes
- if there is a character other than "." at the index, check if the charcter is a key in the children hashmap, if it is, then call DFS on the child node with an incrememnt in the index
- return False if all of them fail

---

[Neetcode Solution Video](https://youtu.be/BTf05gs_8iU)