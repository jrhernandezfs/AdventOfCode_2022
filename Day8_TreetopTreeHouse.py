def is_visible(grid, row, col):
    tree_height = grid[row][col]
    # Check in each direction (up, down, left, right)
    for d_row, d_col in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        r, c = row + d_row, col + d_col
        while 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            if grid[r][c] >= tree_height:
                break
            r += d_row
            c += d_col
        else:
            # If we did not break, the tree is visible in this direction
            return True
    return False


def count_visible_trees(input_file):
    with open(input_file, 'r') as file:
        grid = [list(map(int, line.strip())) for line in file.readlines()]

    visible_trees = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # Edge trees are always visible
            if row in [0, len(grid) - 1] or col in [0, len(grid[0]) - 1] or is_visible(grid, row, col):
                visible_trees += 1
    return visible_trees


def scenic_score(grid, row, col):
    tree_height = grid[row][col]
    score = 1
    # Calculate viewing distance in each direction
    for d_row, d_col in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        view_count = 0
        r, c = row + d_row, col + d_col
        while 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] < tree_height:
            view_count += 1
            r += d_row
            c += d_col
        # Add one for the tree itself
        score *= view_count + 1
    return score


def highest_scenic_score(grid):
    max_score = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            score = scenic_score(grid, row, col)
            max_score = max(max_score, score)
    return max_score


# Replace 'AC8_Input.txt' with your actual input file name
visible_tree_count = count_visible_trees("AC8_Input.txt")
highest_scenic = highest_scenic_score("AC8_input")
print("Number of visible trees:", visible_tree_count)
print("Highest scenic score: ", highest_scenic)

