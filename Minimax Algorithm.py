class Node:
    def __init__(self, value, player, children=None):
        self.value = value
        self.player = player
        self.children = children or []

    def is_terminal(self):
        return len(self.children) == 0


class GameTree:
    def __init__(self, root):
        self.root = root

    def minimax(self, node, depth, is_maximizing):
        # If the node is terminal or depth is 0, return the value of the node
        if node.is_terminal() or depth == 0:
            return node.value

        if is_maximizing:
            best = float('-inf')
            for child in node.children:
                best = max(best, self.minimax(child, depth - 1, False))
            return best
        else:
            best = float('inf')
            for child in node.children:
                best = min(best, self.minimax(child, depth - 1, True))
            return best


def create_sample_game_tree():
    # Create a sample game tree for demonstration purposes
    leaf1 = Node(3, "MIN")
    leaf2 = Node(5, "MIN")
    leaf3 = Node(6, "MIN")
    leaf4 = Node(9, "MIN")
    leaf5 = Node(1, "MIN")
    leaf6 = Node(2, "MIN")
    leaf7 = Node(0, "MIN")
    leaf8 = Node(4, "MIN")

    # Level 1 (Maximizing player)
    node1 = Node(None, "MAX", [leaf1, leaf2])
    node2 = Node(None, "MAX", [leaf3, leaf4])
    node3 = Node(None, "MAX", [leaf5, leaf6])
    node4 = Node(None, "MAX", [leaf7, leaf8])

    # Level 2 (Minimizing player)
    root = Node(None, "MAX", [node1, node2, node3, node4])
    
    return root


# Create the sample game tree
root = create_sample_game_tree()

# Create the GameTree object
game_tree = GameTree(root)

# Apply Minimax algorithm with depth 3 and maximizing player at the root
best_value = game_tree.minimax(root, 3, True)

# Output the result
print(f"Best value at root for maximizing player: {best_value}")
