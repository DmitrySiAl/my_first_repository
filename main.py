from pathlib import Path
import json
from pydantic import BaseModel

FILE_NAME = "tasks.json"

class Task(BaseModel):
    title: str
    done: bool = False

class TodoManager:
    def __init__(self, file_name: str = FILE_NAME):
        self.file_name = file_name
        self.__tasks: list[dict] = self.__load_file()
    def __load_file(self) -> list[dict]:
        path = Path(self.file_name)
        if path.is_file():
            return json.loads(path.read_text(encoding="utf-8"))
        return []
    def __save_file(self):
        path = Path(self.file_name)
        path.write_text(json.dumps(self.__tasks, indent=4, ensure_ascii=False))
    def add_task(self, title: str):
        new_task = Task(title=title)
        new_task = new_task.model_dump()
        self.__tasks.append(new_task)
        self.__save_file()
    def remove_task(self, index: int) -> bool:
        task_index = index - 1
        if 0 <= task_index < len(self.__tasks):
            self.__tasks.pop(task_index)
            self.__save_file()
            return True
        return False
    def mark_done(self, index: int) -> bool:
        task_index = index - 1
        if 0 <= task_index < len(self.__tasks):
            self.__tasks[task_index]["done"] = True
            self.__save_file()
            return True
        return False
    @property
    def tasks(self) -> list[dict]:
        return self.__tasks

def main():
    manager = TodoManager()
    while True:

        print("--- Menu ---")
        print("1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("4. Mark task as done")
        print("5. Exit\n")

        try:
            choice = int(input("Enter your choice: \n"))
        except ValueError:
            print("Invalid choice. Please try again.\n")
            continue

        if choice == 1:
            manager.add_task(input("Enter title: "))
            print("Task added\n")

        elif choice == 2:
            if not manager.tasks:
                print("No tasks added\n")
                continue
            for index, item in enumerate(manager.tasks, 1):
                status = "done" if item["done"] else "not done"
                print(f"{index}. {item['title']} [({status})]")
            try:
                if manager.remove_task(int(input("Enter index: \n"))):
                    print("Task removed\n")
                else:
                    print("Task not found\n")
            except ValueError:
                print("Invalid choice. Please try again.\n")

        elif choice == 3:
            if not manager.tasks:
                print("No tasks removed\n")
                continue
            for index, item in enumerate(manager.tasks, 1):
                status = "done" if item["done"] else "not done"
                print(f"{index}. {item['title']} [({status})]")
            print()

        elif choice == 4:
            if not manager.tasks:
                print("No tasks removed\n")
                continue
            for index, item in enumerate(manager.tasks, 1):
                status = "done" if item["done"] else "not done"
                print(f"{index}. {item['title']} [({status})]")
            try:
                if manager.mark_done(int(input("Enter index: \n"))):
                    print("Task done\n")
                else:
                    print("Task not found\n")
            except ValueError:
                print("Invalid choice. Please try again.\n")

        elif choice == 5:
            print("Exit\n")
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()