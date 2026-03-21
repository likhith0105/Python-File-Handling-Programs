from collections import Counter

k = "name"
v = "Harry"

with open("file.txt", "r") as f:
    lines = [line.strip() for line in f if line.strip()]

counts = Counter(lines)
target = k + "=" + v
print("Occurrences of '" + target + "':", counts.get(target, 0))