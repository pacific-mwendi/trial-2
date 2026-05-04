import csv

data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "London"]
]

with open('output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)