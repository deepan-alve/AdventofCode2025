from pathlib import Path


def parse_input(text: str) -> list[tuple[int, int]]:
    tiles = []
    for line in text.strip().splitlines():
        x, y = line.split(',')
        tiles.append((int(x), int(y)))
    return tiles


def solve(text: str) -> int:
    tiles = parse_input(text)
    max_area = 0
    
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]
            
            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            area = width * height
            
            if area > max_area:
                max_area = area
    
    return max_area


def main() -> None:
    path = Path(__file__).with_name("input.txt")
    data = path.read_text(encoding="utf-8")
    print(solve(data))


if __name__ == "__main__":
    main()
