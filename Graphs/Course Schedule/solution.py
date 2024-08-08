from collections import deque
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites):

        todo = {i: set() for i in range(numCourses)} 
        graph = defaultdict(set)
        for i,j in prerequisites:
            todo[i].add(j)
            graph[j].add(i)
        q = deque([])
        for k,v in todo.items():
            if len(v) == 0:
                q.append(k)
        while q:
            n = q.popleft()
            for i in graph[n]:
                todo[i].remove(n)
                if len(todo[i]) == 0:
                    q.append(i)
            todo.pop(n)
        return not todo
        