import os
from aocd import get_data

# Ensure 'inputs/' folder exists
os.makedirs("inputs", exist_ok=True)

# Fetch and save the data
data = get_data(day=1, year=2024)
with open("inputs/day01.txt", "w") as f:
    f.write(data)
