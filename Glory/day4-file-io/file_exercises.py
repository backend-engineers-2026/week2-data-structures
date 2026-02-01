# reading the entire file
with open("lorem.txt", "r") as file:
    content = file.read()
    print(content)

# reading line by line
with open("lorem.txt", "r") as file:
    for line in file:
        print(line.strip())

# writing to a file with "w" mode
with open("output.txt", "w") as f:
    f.write("Hello, Python!\n")
    f.write("This is a new line.")

# append to a file with "a" mode
with open("output.txt", "a") as f:
    f.write("\nThis line is appended.")

# write multiple lines with .writelines()
lines_to_write = [
    "First line\n", 
    "Second line\n",
    "Third line"
]  

with open("multiline.txt", "w") as f:
    f.writelines(lines_to_write)