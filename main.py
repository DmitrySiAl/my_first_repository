from pathlib import Path
import json

FILE_NAME = "tasks.json"

def main():
    while True:
        def load_tasks():
            if Path(FILE_NAME).exists():
                with open(FILE_NAME, "r", encoding="utf-8") as file:
                    return json.load(file)
            return []

        def save_tasks(tasks):
            with open(FILE_NAME, "w", encoding="utf-8") as file:
                json.dump(tasks, file, indent=4, ensure_ascii=False)

        def add_task():
            tasks = load_tasks()
            task = input("Enter task: \n")
            task = {'task': task, "done": False}
            tasks.append(task)
            save_tasks(tasks)
            print("Task added\n")

        def show_tasks():
            tasks = load_tasks()
            if not tasks:
                print("No tasks added\n")
                return
            for index, item in enumerate(tasks, 1):
                status = "done" if item["done"] else "not done"
                print(f"{index}. {item['task']} [{status}]")

        def remove_task():
            tasks = load_tasks()
            if not tasks:
                print("No tasks to remove\n")
                return
            show_tasks()
            try:
                task_number = int(input("Enter task number to remove: \n"))
                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    save_tasks(tasks)
                    print(f"Task '{removed_task['task']}' removed\n")
                else:
                    print("Invalid task number\n")
            except ValueError:
                print("Invalid task number\n")

        def done_tasks():
            tasks = load_tasks()
            if not tasks:
                print("No tasks found\n")
                return
            show_tasks()
            try:
                choice = int(input("Enter choice: \n"))
                if 1 <= choice <= len(tasks):
                    tasks[choice - 1]["done"] = True
                    save_tasks(tasks)
                    print("Task done\n")
                else:
                    print("Invalid choice\n")
            except ValueError:
                print("Invalid choice\n")

        while True:
            print("Menu")
            print("1. Add task")
            print("2. Remove task")
            print("3. Show tasks")
            print("4. Mark task as done")
            print("5. Exit\n")
            try:
                choice = int(input("Enter choice: \n"))
            except ValueError:
                print("Invalid choice\n")
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
                print("Invalid choice\n")
if __name__ == "__main__":
    main()