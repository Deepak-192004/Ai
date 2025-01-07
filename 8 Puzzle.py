import copy
from heapq import heappush, heappop
N = 3
DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)] 
class PriorityQueue:
    def __init__(self):
        self.heap = []
    def push(self, node):
        heappush(self.heap, node)

    def pop(self):
        return heappop(self.heap)

    def is_empty(self):
        return not self.heap
class Node:
    def __init__(self, parent, matrix, empty_pos, cost, level):
        self.parent = parent
        self.matrix = matrix
        self.empty_pos = empty_pos
        self.cost = cost
        self.level = level

    def __lt__(self, other):
        return self.cost < other.cost
def calculate_cost(matrix, final):
    return sum(matrix[i][j] != final[i][j] and matrix[i][j] != 0 
               for i in range(N) for j in range(N))
def create_node(matrix, empty_pos, new_empty_pos, level, parent, final):
    new_matrix = copy.deepcopy(matrix)
    x1, y1 = empty_pos
    x2, y2 = new_empty_pos
    new_matrix[x1][y1], new_matrix[x2][y2] = new_matrix[x2][y2], new_matrix[x1][y1]
    cost = calculate_cost(new_matrix, final)
    return Node(parent, new_matrix, new_empty_pos, cost, level)
def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N
def print_path(node):
    if node:
        print_path(node.parent)
        for row in node.matrix:
            print(" ".join(map(str, row)))
        print()
def solve_puzzle(initial, empty_pos, final):
    pq = PriorityQueue()
    root = Node(None, initial, empty_pos, calculate_cost(initial, final), 0)
    pq.push(root)
    while not pq.is_empty():
        current = pq.pop()
        if current.cost == 0:
            print_path(current)
            return
        x, y = current.empty_pos
        for dx, dy in DIRECTIONS:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                child = create_node(current.matrix, (x, y), (new_x, new_y), 
                                    current.level + 1, current, final)
                pq.push(child)
initial = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
final = [[1, 2, 3], [5, 8, 6], [0, 7, 4]]
empty_pos = (1, 2)
solve_puzzle(initial, empty_pos, final)
