import json

path = "/Users/lucas/Desktop/Projects/first-python/test.json"

with open(path, "r") as f:
    data = json.load(f)

data.append("Lucas")

with open("test.json", "w") as f:
    json.dump(data, f, indent=4)
