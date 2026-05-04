# Step 1: Read old names (if the file exists)
try:
    with open("names.txt", "r") as f:
        old_names = f.read().splitlines()  # Creates a list of old names
except FileNotFoundError:
    old_names = []  # If file doesn't exist yet, old_names is empty

# Step 2: New names to write
new_names = ["ethan", "lewis", "lawrence", "abdallah"]

# Step 3: Overwrite the file with new names
with open("names.txt", "w") as f:
    for name in new_names:
        f.write(name + "\n")

# Step 4: Print old and new names
print("Old names:", old_names)
print("New names:", new_names)