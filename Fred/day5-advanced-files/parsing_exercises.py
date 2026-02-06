# Create tasks.txt
with open("tasks.txt", "w") as f:
    f.write(
        "task_name|status|priority\nBuy groceries|pending|high\nWrite code|complete|medium"
    )

# Parse and display
with open("tasks.txt", "r") as f:
    header = f.readline().strip().split("|")
    print(f"{header[0]:<15} | {header[1]:<10} | {header[2]:<10}")
    print("-" * 40)
    for line in f:
        name, status, priority = line.strip().split("|")
        print(f"{name:<15} | {status:<10} | {priority:<10}")


# Create config.txt
with open("config.txt", "w") as f:
    f.write("DATABASE_HOST=localhost\nDATABASE_PORT=5432\nDATABASE_NAME=myapp")

# Parse into dictionary
config_dict = {}
with open("config.txt", "r") as f:
    for line in f:
        if "=" in line:
            key, value = line.strip().split("=")
            config_dict[key] = value

print(config_dict)
