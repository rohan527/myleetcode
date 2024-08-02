# Tries

The Trie (pronounced as "try") data structure is a tree-like data structure used for storing a dynamic set of strings. It is commonly used for efficient retrieval and storage of keys in a large dataset. The structure supports operations such as insertion, search, and deletion of keys, making it a valuable tool in fields like computer science and information retrieval. In this article we are going to explore insertion and search operation in Trie Data Structure. [GeeksforGeeks](https://www.geeksforgeeks.org/trie-insert-and-search/#representation-of-of-trie-node)

Essentially, you would have nodes in the tree wich would have character values. Following these nodes from the root to the leaf would give you one specific string that is being represented. 

Every insertion, therefore, is a O(n) task as you will be making 'n' new nodes for 'n' characters in the string. 

Similarly, searching will be a O(n) task as you will be searching for a keyword that is 'n' characters long. 