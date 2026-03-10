import os

def load_grid(filename):
    if not os.path.exists(filename):
        return None
    grid = []
    with open(filename, 'r') as f:
        for line in f:
            grid.append([int(x) for x in line.split()])
    return grid

def display_grid(grid, title):
    print(f"\n{title}")
    for row in grid:
        print(" ".join(f"{str(cell):>2}" for cell in row))

def perform_first_pass(grid):
    
    rows = len(grid)
    cols = len(grid[0])
    labels = [[0 for _ in range(cols)] for _ in range(rows)]
    relationships = {}
    next_label = 1

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                top = labels[r-1][c] if r > 0 else 0
                left = labels[r][c-1] if c > 0 else 0

                #Case 1
                if top == 0 and left == 0:
                    labels[r][c] = next_label
                    next_label += 1
                
                #Case 2
                elif top == 0 or left == 0 or top == left:
                    labels[r][c] = max(top, left)
                
                #Case 3
                else:
                    smaller = min(top, left)
                    larger = max(top, left)
                    labels[r][c] = smaller
                    relationships[larger] = smaller

    return labels, relationships    

def perform_sec_pass(grid):
    pass

def perform_third_pass(grid):
    pass
