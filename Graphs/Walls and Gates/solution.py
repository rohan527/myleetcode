from collections import deque

class Solution:

    def wallsAndGates(self, rooms):
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return

        rows_count = len(rooms)
        cols_count = len(rooms[0])

        #// 1. Find all gates
        q = deque()
        for r in range(rows_count):
            for c in range(cols_count):
                if rooms[r][c] == self.gate:
                    q.append((r, c))

        #// 2. Find shorstest distance to gate: BFS:
        while q:
            r, c = q.popleft()

            candidate_distance = rooms[r][c] + 1
            
            for d_r, d_c in self.directions:
                adj_r, adj_c = r + d_r, c + d_c
                if adj_r in (-1, rows_count) or adj_c in (-1, cols_count):
                    continue
                        
                if candidate_distance < rooms[adj_r][adj_c]: #// no check if cell is a wall since the candidate_distance will be always > -1
                    rooms[adj_r][adj_c] = candidate_distance
                    q.append((adj_r, adj_c))

        