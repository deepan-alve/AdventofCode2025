from pathlib import Path


def parse_input(text: str) -> list[tuple[int, int]]:
    tiles = []
    for line in text.strip().splitlines():
        x, y = line.split(',')
        tiles.append((int(x), int(y)))
    return tiles


def get_loop_edges(red_tiles: list[tuple[int, int]]) -> set[tuple[int, int]]:
    edges = set()
    for i in range(len(red_tiles)):
        x1, y1 = red_tiles[i]
        x2, y2 = red_tiles[(i + 1) % len(red_tiles)]
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                edges.add((x1, y))
        else:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                edges.add((x, y1))
    return edges


def is_point_inside_polygon(x: int, y: int, polygon: list[tuple[int, int]]) -> bool:
    """Check if a point is inside a polygon using ray casting algorithm."""
    n = len(polygon)
    inside = False
    
    p1x, p1y = polygon[0]
    for i in range(1, n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    
    return inside


def get_all_green_tiles(red_tiles: list[tuple[int, int]], edges: set[tuple[int, int]]) -> set[tuple[int, int]]:
    """Get all green tiles (edges + interior)."""
    # Find bounding box
    min_x = min(x for x, y in red_tiles)
    max_x = max(x for x, y in red_tiles)
    min_y = min(y for x, y in red_tiles)
    max_y = max(y for x, y in red_tiles)
    
    green_tiles = set(edges)
    
    # Add all interior points
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (x, y) not in edges and is_point_inside_polygon(x, y, red_tiles):
                green_tiles.add((x, y))
    
    return green_tiles


def solve(text: str) -> int:
    red_tiles = parse_input(text)
    edges = get_loop_edges(red_tiles)
    
    # Pre-compute all green tiles (edges + interior)
    green_tiles = get_all_green_tiles(red_tiles, edges)
    
    max_area = 0
    
    for i in range(len(red_tiles)):
        x1, y1 = red_tiles[i]
        for j in range(i + 1, len(red_tiles)):
            x2, y2 = red_tiles[j]
            
            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)
            
            area = (max_x - min_x + 1) * (max_y - min_y + 1)
            if area <= max_area:
                continue
            
            # Check if all tiles in rectangle are green
            valid = all((x, y) in green_tiles
                       for x in range(min_x, max_x + 1)
                       for y in range(min_y, max_y + 1))
            
            if valid:
                max_area = area
    
    return max_area


def main() -> None:
    path = Path(__file__).with_name("input.txt")
    data = path.read_text(encoding="utf-8")
    print(solve(data))


if __name__ == "__main__":
    main()
