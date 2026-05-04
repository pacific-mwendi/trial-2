import json

# New data to write
new_data = [
    {"name": "pacific", "age": "19", "country": "kenya"}
]

# Open file in write mode
with open("data1.json", "w") as docs:
    json.dump(new_data, docs, indent=4)  # indent=4 for readable formatting
