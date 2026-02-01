# Read config.txt:
with open("config.txt", "r") as file:
    contents = file.read()
    print(contents)

# Parse into dictionary using split('=')
config = {}
with open("config.txt", "r") as file:
    for line in file:
        line = line.strip() # .strip() removes whitespaces (spaces, tabs, \n) from both ends of a string
        key, value = line.split("=")
        config[key] = value
print("\n", config)