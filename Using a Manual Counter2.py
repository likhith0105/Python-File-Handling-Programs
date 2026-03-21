k = "name"
v = "Harry"
count = 0

with open("file.txt", "r") as f:
    for line in f:
        if line.strip() == k + "=" + v:
            count = count + 1

print("Occurrences of '" + k + "=" + v + "':", count)