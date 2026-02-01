# - Count total lines
total_lines = 0
with open("logs.txt", "r") as file:
    for line in file:
        total_lines += 1
print(f"Total lines: {total_lines}")

# - Find lines with "ERROR"
error_lines = []
with open("logs.txt", "r") as file:
    for line in file:
        if "ERROR" in line:
            error_lines.append(line)

print("\n", error_lines)

# - Extract timestamps
timestamps = []
with open("logs.txt", "r") as file:
    for line in file:
        parts = line.split()
        timestamp = parts[0] + " " + parts[1]
        timestamps.append(timestamp)

print("\nLog timestamps:")
for ts in timestamps:
    print(ts)

# - Write errors to separate file
with open("error.txt", "w") as error_file:
    for line in error_lines:
        error_file.write(line)