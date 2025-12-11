import re
from typing import List, Tuple, Set
from itertools import product

def parse_line(line: str) -> Tuple[List[int], List[Set[int]]]:
    """Parse a line into target configuration and button definitions."""
    indicator_match = re.search(r'\[([.#]+)\]', line)
    target = [1 if c == '#' else 0 for c in indicator_match.group(1)]
    
    button_matches = re.findall(r'\(([0-9,]+)\)', line)
    buttons = []
    for btn_str in button_matches:
        button_set = set(int(x) for x in btn_str.split(','))
        buttons.append(button_set)
    
    return target, buttons

def gaussian_elimination_gf2(buttons: List[Set[int]], target: List[int]) -> int:
    """
    Solve using Gaussian elimination over GF(2) and find minimum weight solution.
    Returns the minimum number of button presses needed, or -1 if no solution exists.
    
    buttons: Each set contains the indices of lights that button toggles.
    target: The desired state of each light.
    """
    n_lights = len(target)
    n_buttons = len(buttons)
    
    # Build augmented matrix: rows = lights, cols = buttons, last col = target
    aug = []
    for light_idx in range(n_lights):
        row = []
        for button_idx in range(n_buttons):
            row.append(1 if light_idx in buttons[button_idx] else 0)
        row.append(target[light_idx])
        aug.append(row)
    
    # Track which columns have pivots and which are free variables
    pivot_cols = []
    free_cols = []
    
    # Forward elimination with column tracking
    current_row = 0
    for col in range(n_buttons):
        # Find pivot in this column
        pivot_row = -1
        for r in range(current_row, n_lights):
            if aug[r][col] == 1:
                pivot_row = r
                break
        
        if pivot_row == -1:
            # This is a free variable
            free_cols.append(col)
            continue
        
        # This column has a pivot
        pivot_cols.append((current_row, col))
        
        # Swap rows
        aug[current_row], aug[pivot_row] = aug[pivot_row], aug[current_row]
        
        # Eliminate
        for r in range(n_lights):
            if r != current_row and aug[r][col] == 1:
                for c in range(n_buttons + 1):
                    aug[r][c] ^= aug[current_row][c]
        
        current_row += 1
    
    # Check for inconsistency
    for row in range(current_row, n_lights):
        if aug[row][n_buttons] == 1:
            return -1
    
    # If no free variables, we have a unique solution
    if not free_cols:
        solution = [0] * n_buttons
        for row, col in pivot_cols:
            solution[col] = aug[row][n_buttons]
        return sum(solution)
    
    # Try all combinations of free variables to find minimum weight solution
    min_weight = float('inf')
    
    for free_values in product([0, 1], repeat=len(free_cols)):
        solution = [0] * n_buttons
        
        # Set free variables
        for i, col in enumerate(free_cols):
            solution[col] = free_values[i]
        
        # Back substitute for pivot variables
        for row, col in reversed(pivot_cols):
            val = aug[row][n_buttons]
            for c in range(col + 1, n_buttons):
                val ^= (aug[row][c] * solution[c])
            solution[col] = val
        
        weight = sum(solution)
        min_weight = min(min_weight, weight)
    
    return min_weight

def solve_machine(target: List[int], buttons: List[Set[int]]) -> int:
    """Solve for a single machine."""
    return gaussian_elimination_gf2(buttons, target)

def main():
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')
    
    total_presses = 0
    for i, line in enumerate(lines, 1):
        target, buttons = parse_line(line)
        min_presses = solve_machine(target, buttons)
        if min_presses == -1:
            print(f"No solution for line {i}")
        else:
            total_presses += min_presses
    
    print(f"Fewest button presses required: {total_presses}")

if __name__ == "__main__":
    main()
