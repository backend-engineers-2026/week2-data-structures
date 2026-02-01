TODO_FILE = "todo.txt"


# Helper: read all tasks from file
def read_tasks():
    tasks = []

    try:
        with open(TODO_FILE, "r") as file:
            for line in file:
                task_name, status = line.strip().split("|")
                tasks.append({"task": task_name, "status": status})
    except FileNotFoundError:
        pass  # file doesn't exist yet → no tasks

    return tasks


# Helper: write all tasks to file
def write_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task['task']}|{task['status']}\n")


# Add task
def add_task(task_name):
    with open(TODO_FILE, "a") as file:
        file.write(f"{task_name}|pending\n")

    print(f"Task added: {task_name}")


# Mark task as complete
def mark_complete(task_name):
    tasks = read_tasks()
    found = False

    for task in tasks:
        if task["task"] == task_name:
            task["status"] = "completed"
            found = True

    if not found:
        print("Task not found")
        return

    write_tasks(tasks)
    print(f"Task marked complete: {task_name}")


# List all tasks
def list_tasks():
    tasks = read_tasks()

    if not tasks:
        print("No tasks found")
        return

    for task in tasks:
        print(f"{task['task']} [{task['status']}]")


# Filter by status
def filter_tasks(status):
    tasks = read_tasks()
    filtered = [t for t in tasks if t["status"] == status]

    if not filtered:
        print(f"No {status} tasks found")
        return

    for task in filtered:
        print(f"{task['task']} [{task['status']}]")
