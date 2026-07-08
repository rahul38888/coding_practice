

def count_islands(grid: list[list[int]]):

    visited = set()

    def dfs(i: int, j: int):
        if ((i < 0) or (j < 0) or (i >= len(grid)) or (j >= len(grid[0]))
                or (i, j) in visited):
            return

        if grid[i][j] == 0:
            return

        visited.add((i,j))
        dfs(i - 1, j)
        dfs(i + 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in visited and grid[i][j] == 1:
                count += 1
                dfs(i, j)

    return count


def build_grid():
    return [
            [1, 1, 0, 0, 1],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 0, 0, 1, 1]
            ]


if __name__ == '__main__':
    grd = build_grid()
    print(f"Number of islands: {count_islands(grd)}")
