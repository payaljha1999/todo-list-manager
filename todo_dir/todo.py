import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = load_tasks()
    tasks.append({'description': description, 'done': False})
    save_tasks(tasks)
    print("✅ Task added.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['description']} [{status}]")

def mark_done(index):
    tasks = load_tasks()
    try:
        tasks[index - 1]['done'] = True
        save_tasks(tasks)
        print("✅ Task marked as done.")
    except IndexError:
        print("⚠️ Invalid task number.")

def delete_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ Deleted: {removed['description']}")
    except IndexError:
        print("⚠️ Invalid task number.")

def menu():
    while True:
        print("\n📋 To-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            desc = input("Enter task description: ")
            add_task(desc)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            num = int(input("Enter task number to mark as done: "))
            mark_done(num)
        elif choice == '4':
            num = int(input("Enter task number to delete: "))
            delete_task(num)
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
