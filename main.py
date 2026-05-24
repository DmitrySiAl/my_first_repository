from pathlib import Path
import json
from wsgiref.util import shift_path_info

FILE_NAME = ("tasks.json")

def load_tasks():
    if Path(FILE_NAME).exists():
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    tasks = load_tasks()
    task = input("Enter task: ")
    task = {'task': task, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added")

def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks added")
        return
    for index, item in enumerate(tasks, 1):
        status = "done" if item["done"] else "not done"
        print(f"{index}. {item['task']} - {status}")

def remove_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to remove")
        return
    show_tasks()
    try:
        task_number = int(input("Enter task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task['task']}' removed")
        else:
            print("Invalid task number")
    except ValueError:
        print("Invalid task number")

def done_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found")
        return
    show_tasks()
    try:
        choice = int(input("Enter choice: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["done"] = True
            save_tasks(tasks)
            print("Task done")
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid choice")

while True:
    print("Menu")
    print("1. Add task")
    print("2. Remove task")
    print("3. Show tasks")
    print("4. Mark task as done")
    print("5. Exit")
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid choice")
        continue
    if choice == 1:
        add_task()
    elif choice == 2:
        remove_task()
    elif choice == 3:
        show_tasks()
    elif choice == 4:
        done_tasks()
    elif choice == 5:
        print("Goodbye")
        break
    else:
        print("Invalid choice")