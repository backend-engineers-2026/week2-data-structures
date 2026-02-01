# Todo list with file persistence
#tasks = []

def load_tasks():
    tasks = []

    try:
        with open("todo.txt", "a+") as file:
            file.seek(0)
            for line in file:
                task, status = line.strip().split("|")
                tasks.append({"task": task, "status": status})
    except FileNotFoundError:
        pass

    return tasks

# - Add task (saves to todo.txt)
def save_tasks(tasks):
    with open("todo.txt", "a") as file:
        for task in tasks:
            line = f"{task['task']} | {task['status']}\n"
            file.write(line)

def add_task(tasks):
    name = input("Task name: ")
    tasks.append({"task": name, "status": "pending"})
    save_tasks(tasks)

# - Mark complete (updates file)
def mark_completed(tasks):
    num = int(input("Task number: ")) - 1

    if num >= 0 and num < len(tasks):
        tasks[num]["status"] = "completed"
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

# - List all tasks
def view_tasks(tasks):
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        icon = "☑️ " if task["status"] == "completed" else "⬜"
        print(f"{icon} {i}. {task['task']}")
# - Filter by status (pending/completed)

tasks = load_tasks()

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Mark completed")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        mark_completed(tasks)
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
