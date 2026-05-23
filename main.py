from pathlib import Path
import json
x = "tasks.json"
def load_task():
    if Path(x).exists():
        with open(x, "r", encoding="utf-8") as file:
            return json.load(file)
    return []
def save_task(tasks):
    with open(x, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)
def add_task():
    tasks = load_task()
    task = input("Enter task: ")
    task = {'task': task, "ready": "not"}
    tasks.append(task)
    save_task(tasks)
    print("Task added")
def show_tasks():
    tasks = load_task()
    if not tasks:
        print("No tasks added")
        return
    for index, item in enumerate(tasks, 1):
        status = "ready" if item["ready"] == "yes" else "not ready"
        print(f"{index}. {item['task']} - {status}")
def remove_task():
    tasks = load_task()
    show_tasks()
    if not tasks:
        print("No tasks to remove")
        return
    task = input("Enter task to remove: ")
    task_to_delete = None
    for item in tasks:
        if item["task"] == task:
            task_to_delete = item
            break
    if task_to_delete:
        tasks.remove(task_to_delete)
        save_task(tasks)
        print("Task removed")
    else:
        print("Task not found")
def ready_tasks():
    tasks = load_task()
    if not tasks:
        print("No tasks found")
        return
    show_tasks()
    try:
        choice = int(input("Enter choice: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["ready"] = "yes"
            save_task(tasks)
            print("Task ready")
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid choice")
while True:
    print("Menu")
    print("1. Add task")
    print("2. Remove task")
    print("3. Show tasks")
    print("4. Mark task as ready")
    print("5. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        add_task()
    elif choice == 2:
        remove_task()
    elif choice == 3:
        show_tasks()
    elif choice == 4:
        ready_tasks()
    elif choice == 5:
        break
    else:
        print("Invalid choice")