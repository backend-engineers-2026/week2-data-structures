total_lines = 0
error_lines = []
timestamps = []

from pathlib import Path

base_dir = Path(__file__).parent
log_path = base_dir / "logs.txt"
error_output = base_dir / "errors.txt"

with open(log_path, "r") as file:
    for line in file:
        total_lines += 1

        if "ERROR" in line:
            error_lines.append(line)

        timestamp = line.split(" ", 2)[0] + " " + line.split(" ", 2)[1]
        timestamps.append(timestamp)

# Write errors to a subdirectory named 'errors'
errors_dir = base_dir / "errors"
errors_dir.mkdir(parents=True, exist_ok=True)
error_file_path = errors_dir / "errors.txt"
with open(error_file_path, "w") as error_file:
    error_file.writelines(error_lines)

print("Total lines:", total_lines)
print("Timestamps:", timestamps)
