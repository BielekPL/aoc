import os
from time import sleep
from aocd import get_data

# Ensure 'inputs/' folder exists
os.makedirs("2024/inputs", exist_ok=True)

# Fetch and save the data
for i in range(25):
    data = get_data(day=i+1, year=2024)
    with open(f"2024/inputs/day{i+1}.txt", "w") as f:
        f.write(data)
    sleep(1)
