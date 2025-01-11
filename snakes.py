# The snakesAndLadders method calculates the minimum moves to reach the last square on a snakes and ladders board.

# Helper Function:
# - `intToPos`: Converts a square number to its corresponding board position, accounting for the alternating row directions.

# BFS Approach:
# - Start at square 1 and simulate dice rolls (1 to 6) to calculate reachable squares.
# - Use the board value to handle snakes or ladders and adjust the destination square.
# - If the final square (n * n) is reached, return the number of moves.
# - Use a `visit` set to track visited squares and avoid cycles.

# TC: O(n^2) - Traverse up to all squares on the board.
# SC: O(n^2) - Space for the queue and visited set.


from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def intToPos(square):
            r = (square - 1) // n
            c = (square - 1) % n
            if r % 2 == 1:
                c = n - 1 - c
            r = n - 1 - r
            return r, c
        
        q = deque([(1, 0)])
        visit = set()
        
        while q:
            square, moves = q.popleft()
            
            for i in range(1, 7):
                nextSquare = square + i
                r, c = intToPos(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                
                if nextSquare == n * n:
                    return moves + 1
                
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append((nextSquare, moves + 1))
        
        return -1