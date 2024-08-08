# Course Schedule

## Description

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

Question Link: [Leetcode 207](https://leetcode.com/problems/course-schedule/description/)

---
## Solution

In this question, we first have to figure out the courses we can take which do not have any pre-requesites. After we do these courses, we can go do the courses that do not have any pre-requesites that need to be done anymore. 

First, we can iterate over all the courses and make them into keys in a hasmpap. In this hashmap, the values would be sets that will have the prerequisires for each key they represent. 

Similarly, we will also create a graph, i.e. a hasmpap where every key is a prerequisite for a course value. 

First we iterate through the first hashmpap, and find the courses that have no prerequisites. We add these courses to a dequqe. 

While there are elements in the dequqe, we pop the leftmost element, we find the courses can now be taken as the popped course is now done. You can find this in the second hasmap. The values which has no prequesites left anymore, can now be added to the queue. 

Finally, return if the queue has no values left to return. Which means that all the courses can be taken. 

---

[Neetcode Solution Video](https://youtu.be/EgI5nU9etnU)