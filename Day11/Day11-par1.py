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

def count_paths(graph, start, end, visited=None):
    """Count all paths from start to end using DFS."""
    if visited is None:
        visited = set()
    
    # Base case: reached the destination
    if start == end:
        return 1
    
    # If this device is not in the graph or we've visited it, return 0
    if start not in graph or start in visited:
        return 0
    
    # Mark current device as visited
    visited.add(start)
    
    # Count paths through all outputs
    total_paths = 0
    for output in graph[start]:
        total_paths += count_paths(graph, output, end, visited)
    
    # Backtrack: remove current device from visited
    visited.remove(start)
    
    return total_paths

def main():
    # Parse input
    graph = parse_input('input.txt')
    
    # Count paths from "you" to "out"
    num_paths = count_paths(graph, "you", "out")
    
    print(f"Number of paths from 'you' to 'out': {num_paths}")

if __name__ == "__main__":
    main()
