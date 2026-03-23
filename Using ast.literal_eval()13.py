

import ast

try:
    with open('data.txt', 'r') as file:
        for line in file:
            if line.strip():  
                dictionary = ast.literal_eval(line.strip())
                print(dictionary)
except Exception as e:
    print("Something unexpected occurred:", e)