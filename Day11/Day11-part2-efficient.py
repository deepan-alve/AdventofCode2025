from functools import lru_cache

def parse_input(filename):
    """Parse the input file and build the graph."""
    graph = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(': ')
            device = parts[0]
            outputs = parts[1].split()
            graph[device] = outputs
    return graph

def make_count_paths(graph):
    """Create a memoized path counting function for a specific graph."""
    cache = {}
    
    def count_paths(current, target):
        """Count all paths from current to target using memoization."""
        # Check cache
        if (current, target) in cache:
            return cache[(current, target)]
        
        # Base case: reached target
        if current == target:
            return 1
        
        # Dead end: no outgoing connections
        if current not in graph:
            return 0
        
        # Sum paths through all neighbors
        total = 0
        for neighbor in graph[current]:
            total += count_paths(neighbor, target)
        
        # Cache result
        cache[(current, target)] = total
        return total
    
    return count_paths

def solve_part2(graph):
    """
    Find paths from svr to out that visit both dac and fft.
    
    Key insight: In a DAG (Directed Acyclic Graph), if a path must visit
    both A and B, one must come before the other. We check both orderings:
    1. svr -> dac -> fft -> out
    2. svr -> fft -> dac -> out
    
    For each ordering, multiply the segment counts.
    """
    # Create memoized path counter
    count_paths = make_count_paths(graph)
    
    start = "svr"
    end = "out"
    wp1 = "dac"  # Waypoint 1
    wp2 = "fft"  # Waypoint 2
    
    print("Calculating path segments...")
    
    # SCENARIO 1: dac comes before fft
    # Path segments: svr -> dac -> fft -> out
    paths_svr_dac = count_paths(start, wp1)
    paths_dac_fft = count_paths(wp1, wp2)
    paths_fft_out = count_paths(wp2, end)
    
    scenario_1 = paths_svr_dac * paths_dac_fft * paths_fft_out
    
    print(f"Scenario 1 (svr->dac->fft->out):")
    print(f"  svr->dac: {paths_svr_dac}")
    print(f"  dac->fft: {paths_dac_fft}")
    print(f"  fft->out: {paths_fft_out}")
    print(f"  Total: {scenario_1}")
    print()
    
    # SCENARIO 2: fft comes before dac
    # Path segments: svr -> fft -> dac -> out
    paths_svr_fft = count_paths(start, wp2)
    paths_fft_dac = count_paths(wp2, wp1)
    paths_dac_out = count_paths(wp1, end)
    
    scenario_2 = paths_svr_fft * paths_fft_dac * paths_dac_out
    
    print(f"Scenario 2 (svr->fft->dac->out):")
    print(f"  svr->fft: {paths_svr_fft}")
    print(f"  fft->dac: {paths_fft_dac}")
    print(f"  dac->out: {paths_dac_out}")
    print(f"  Total: {scenario_2}")
    print()
    
    # Total paths visiting both waypoints
    total = scenario_1 + scenario_2
    
    print(f"=" * 50)
    print(f"Total paths from '{start}' to '{end}' visiting both '{wp1}' and '{wp2}': {total}")
    
    return total

def main():
    # Parse input
    graph = parse_input('input.txt')
    print(f"Graph has {len(graph)} devices\n")
    
    # Solve Part 2
    result = solve_part2(graph)

if __name__ == "__main__":
    main()
