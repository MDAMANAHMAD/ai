//8 puzzle
import heapq

class PuzzleState:
    def _init_(self, board, g, h, parent=None):
        self.board = board
        self.g = g
        self.h = h
        self.parent = parent
        self.empty_row, self.empty_col = self.find_empty_tile()

    def find_empty_tile(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j

    @staticmethod
    def calculate_heuristic(board, goal):
        distance = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] != 0:
                    for x in range(3):
                        for y in range(3):
                            if board[i][j] == goal[x][y]:
                                distance += abs(i - x) + abs(j - y)
        return distance

    def generate_neighbors(self, goal):
        neighbors = []
        row_offsets = [-1, 1, 0, 0]
        col_offsets = [0, 0, -1, 1]

        for i in range(4):
            new_row = self.empty_row + row_offsets[i]
            new_col = self.empty_col + col_offsets[i]
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_board = [row[:] for row in self.board]
                new_board[self.empty_row][self.empty_col], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[self.empty_row][self.empty_col]
                new_h = PuzzleState.calculate_heuristic(new_board, goal)
                neighbors.append(PuzzleState(new_board, self.g + 1, new_h, self))
        return neighbors

    def is_goal(self, goal):
        return self.board == goal

    def print_board(self):
        for row in self.board:
            print(' '.join(map(str, row)))
        print()

    def _lt_(self, other):
        return (self.g + self.h) < (other.g + other.h)

def solve_puzzle(start, goal):
    open_set = []
    closed_set = set()
    start_h = PuzzleState.calculate_heuristic(start, goal)
    heapq.heappush(open_set, PuzzleState(start, 0, start_h))

    while open_set:
        current = heapq.heappop(open_set)

        if current.is_goal(goal):
            print("Solution found!")
            print_solution_path(current)
            return

        closed_set.add(tuple(map(tuple, current.board)))

        for neighbor in current.generate_neighbors(goal):
            if tuple(map(tuple, neighbor.board)) not in closed_set:
                heapq.heappush(open_set, neighbor)

    print("No solution found.")

def print_solution_path(state):
    if state is None:
        return
    print_solution_path(state.parent)
    state.print_board()

if _name_ == "_main_":
    start = [
        [1, 2, 3],
        [4, 0, 5],
        [7, 8, 6]
    ]

    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    solve_puzzle(start, goal)
