# Author: Perfect Makuwerere
# Date: 02/24/2026
# Description: Cosmic Ray Muon Detector Analysis

import random


GRID_SIZE = 8
muon_map = []
for i in range(GRID_SIZE):
    row = []
    for j in range(GRID_SIZE):
        row.append(0)
    muon_map.append(row)

for r in range(GRID_SIZE):
    for c in range(GRID_SIZE):
        muon_map[r][c] = random.randint(0, 500)

high_val = -1
low_val = 501
high_x, high_y = 0, 0
low_x, low_y = 0, 0


for r in range(GRID_SIZE):
    for c in range(GRID_SIZE):
        current_rate = muon_map[r][c]
        if current_rate > high_val:
            high_val = current_rate
            high_y = r + 1  
            high_x = c + 1
            
        if current_rate < low_val:
            low_val = current_rate
            low_y = r + 1 
            low_x = c + 1

print("Cosmic Ray Muon Detector Analysis")
print(f"Highest Capture Rate: {high_val} at coordinates (X: {high_x}, Y: {high_y})")
print(f"Lowest Capture Rate:  {low_val} at coordinates (X: {low_x}, Y: {low_y})")


print("\nDetection Map Grid")
for row in muon_map:
    for val in row:
        print(f"{val:<4}", end=" ")
    print()