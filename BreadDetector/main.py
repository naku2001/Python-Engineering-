from bread import (load_grid, display_grid, perform_first_pass)

def main():
    
    grid = None
    while grid is None:
        filename = input("Enter the bread image filename (e.g., bread.txt): ")
        grid = load_grid(filename)
        if grid is None:
            print("File not found. Please try again.")

    display_grid(grid, "Initial Image (1s and 0s)")

    labeled_grid, rels = perform_first_pass(grid)
    display_grid(labeled_grid, "After First Pass (Initial Labels)")


if __name__ == "__main__":
    main()    