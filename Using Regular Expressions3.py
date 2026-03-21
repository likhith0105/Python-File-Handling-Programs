import re

k = "name"
v = "Harry"

with open("file.txt", "r") as f:
    data = f.read()

pattern = r"\b" + re.escape(k) + "=" + re.escape(v) + r"\b"
matches = re.findall(pattern, data)

print("Occurrences of '" + k + "=" + v + "':", len(matches))