# example 1
myfile = "students.csv"

with open(myfile) as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]}:{row[1]}")