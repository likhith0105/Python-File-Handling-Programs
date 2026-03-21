k = "name"
v = "Harry"
count = 0

with open("file.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    if line.strip() == k + "=" + v:
        count = count + 1

print("Occurrences of '" + k + "=" + v + "':", count)