# Implement Trie (Prefix Tree)

## Description

Implement the Trie class:

- Trie(): Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
- boolean search(String word): Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix):  Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.


Question Link: [Leetcode 208](https://leetcode.com/problems/implement-trie-prefix-tree/description/)

---
## Solution

Before creating the Trie class, create a TrieNode class which will act as the nodes. Nodes will be initialized with a children hashmap and boolean for wether it is the last character in the word. By default, the boolean will be false and the hashmap will be empty. 

Initialise the Trie with a root node that is a TrieNode. 

### Insert

Start with the root node. Iterate through every character of the string. If there is a key with the current character in the children hashmap for the TrieNode, go to the next node which will be the value for the key. If there is not a key with the current character in the hashmap, make a new character key with the value as a new node. Change current node to new node. 

At the end of the iteration, change the current TrieNodes boolean to True. 


### Search

Search follows a very similar process to Insert. If there is not a key value in the current nodes hashmap with the current character return false. 
However, if you reach the end of the iteration, you may still not have the solution. 

Make sure to return the current TrieNode's boolean. 

### StartsWith

Literally the same as Search! Only you return True at the end of the iteration. 


---

[Neetcode Solution Video](https://youtu.be/oobqoCJlHA0)