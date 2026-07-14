# Last updated: 7/14/2026, 2:00:18 PM
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = set(map(tuple, obstacles))

        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        x = y = 0
        dir_idx = 0
        max_dist = 0

        for cmd in commands:
            if cmd == -1: 
                dir_idx = (dir_idx + 1) % 4

            elif cmd == -2:  
                dir_idx = (dir_idx - 1) % 4

            else:
                dx, dy = directions[dir_idx]

                for _ in range(cmd):
                    nx, ny = x + dx, y + dy

                    if (nx, ny) in obstacle_set:
                        break

                    x, y = nx, ny
                    max_dist = max(max_dist, x * x + y * y)

        return max_dist