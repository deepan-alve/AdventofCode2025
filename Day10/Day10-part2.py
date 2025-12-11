import re
from typing import List, Set, Tuple
from pulp import *

def parse_line(line: str) -> Tuple[List[int], List[Set[int]]]:
    """Parse a line into joltage requirements and button definitions."""
    joltage_match = re.search(r'\{([0-9,]+)\}', line)
    target = [int(x) for x in joltage_match.group(1).split(',')]
    
    button_matches = re.findall(r'\(([0-9,]+)\)', line)
    buttons = []
    for btn_str in button_matches:
        button_set = set(int(x) for x in btn_str.split(','))
        buttons.append(button_set)
    
    return target, buttons

def solve_ilp(buttons: List[Set[int]], target: List[int]) -> int:
    """
    Solve using Integer Linear Programming.
    Minimize: sum(x_i) for all buttons i
    Subject to: sum over buttons i of (x_i * a_ij) = target_j for each counter j
                x_i >= 0, x_i integer
    """
    n_counters = len(target)
    n_buttons = len(buttons)
    
    # Create the problem
    prob = LpProblem("ButtonPresses", LpMinimize)
    
    # Decision variables: number of times each button is pressed
    button_vars = [LpVariable(f"button_{i}", lowBound=0, cat='Integer') for i in range(n_buttons)]
    
    # Objective: minimize total button presses
    prob += lpSum(button_vars)
    
    # Constraints: for each counter, sum of contributions must equal target
    for counter_idx in range(n_counters):
        constraint = lpSum([
            button_vars[button_idx] 
            for button_idx in range(n_buttons) 
            if counter_idx in buttons[button_idx]
        ])
        prob += constraint == target[counter_idx], f"counter_{counter_idx}"
    
    # Solve
    prob.solve(PULP_CBC_CMD(msg=0))
    
    if prob.status != 1:  # 1 = Optimal
        return -1
    
    # Get solution
    total_presses = sum(int(v.varValue) for v in button_vars)
    return total_presses

def main():
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')
    
    total_presses = 0
    for i, line in enumerate(lines, 1):
        target, buttons = parse_line(line)
        min_presses = solve_ilp(buttons, target)
        if min_presses == -1:
            print(f"No solution for line {i}")
        else:
            total_presses += min_presses
    
    print(f"Fewest button presses required: {total_presses}")

if __name__ == "__main__":
    main()
