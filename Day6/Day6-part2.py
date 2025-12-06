from pathlib import Path


def split_cols(lines: list[str]) -> list[list[str]]:
    width = max(len(line.rstrip("\n")) for line in lines)
    grid = [line.rstrip("\n").ljust(width) for line in lines]
    blocks: list[tuple[int, int]] = []
    inside = False
    start = 0
    for x in range(width):
        col = [row[x] for row in grid]
        space_col = all(ch == " " for ch in col)
        if not space_col and not inside:
            inside = True
            start = x
        elif space_col and inside:
            inside = False
            blocks.append((start, x))
    if inside:
        blocks.append((start, width))

    res: list[list[str]] = []
    for a, b in blocks:
        slice_rows = [row[a:b] for row in grid]
        last = slice_rows[-1]
        op = "*" if "*" in last else "+"
        digits_rows = slice_rows[:-1]
        h = len(digits_rows)
        w = b - a
        nums: list[str] = []
        for x in range(w - 1, -1, -1):
            col_chars = [digits_rows[r][x] for r in range(h)]
            digs = "".join(ch for ch in col_chars if ch != " ")
            if digs:
                nums.append(digs)
        res.append([op] + nums)
    return res


def calc(vals: list[str]) -> int:
    op = vals[0]
    nums = [int(x) for x in vals[1:]]
    if op == "+":
        return sum(nums)
    ans = 1
    for n in nums:
        ans *= n
    return ans


def solve(text: str) -> int:
    lines = text.splitlines()
    if not lines:
        return 0
    probs = split_cols(lines)
    return sum(calc(p) for p in probs)


def main() -> None:
    path = Path(__file__).with_name("input.txt")
    data = path.read_text(encoding="utf-8")
    print(solve(data))


if __name__ == "__main__":
    main()
