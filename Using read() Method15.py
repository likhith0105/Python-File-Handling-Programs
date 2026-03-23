try:
    with open("file.txt", "r") as f:
        lines = f.readlines()

    for l in lines:
        l = l.strip()
        if not l:
            continue

        d = {}
        for i in l.strip("{}").split(", "):
            k, v = i.split(":", 1)
            d[k.strip("'\" ").strip()] = v.strip("'\" ").strip()

        print(d)

except Exception as e:
    print("Error:", e)