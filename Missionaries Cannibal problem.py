from collections import deque

initial_state = {'left': {'missionaries': 3, 'cannibals': 3}, 'right': {'missionaries': 0, 'cannibals': 0}, 'boat': 'left'}

def is_valid(state):
    for side in ['left', 'right']:
        if state[side]['missionaries'] < 0 or state[side]['cannibals'] < 0 or \
           (state[side]['missionaries'] > 0 and state[side]['cannibals'] > state[side]['missionaries']):
            return False
    return True

def generate_next_states(state):
    moves, boat, other = [], state['boat'], 'left' if state['boat'] == 'right' else 'right'
    for m in range(3):
        for c in range(3):
            if 1 <= m + c <= 2 and state[boat]['missionaries'] >= m and state[boat]['cannibals'] >= c:
                new_state = {side: state[side].copy() for side in ['left', 'right']}
                new_state[boat]['missionaries'] -= m
                new_state[boat]['cannibals'] -= c
                new_state[other]['missionaries'] += m
                new_state[other]['cannibals'] += c
                new_state['boat'] = other
                if is_valid(new_state):
                    moves.append(new_state)
    return moves

def find_solution():
    queue = deque([(initial_state, [])])
    while queue:
        state, path = queue.popleft()
        if state['left']['missionaries'] == 0 and state['left']['cannibals'] == 0:
            return path
        for next_state in generate_next_states(state):
            if next_state not in path:
                queue.append((next_state, path + [next_state]))
    return None

solution = find_solution()
if solution:
    for i, state in enumerate(solution):
        print(f"Step {i + 1}: {state}")
else:
    print("No solution found.")
