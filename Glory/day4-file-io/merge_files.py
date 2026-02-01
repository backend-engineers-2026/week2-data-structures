files = ["lorem.txt", "python.txt", "example.txt"]
with open("merged.txt", 'w') as output:
    for filename in files: # loop through each file
        output.write(f"==== {filename} ====\n")

        with open(filename, "r") as file:
            for line in file:
                output.write(line)
        
        output.write("\n") # blank line between files