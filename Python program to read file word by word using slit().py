with open("Myfile.txt", "r") as f:
    for line in f:           
        for w in line.split():   
            print(w)