import os
import json

# File to store tasks
TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from the file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter the task description: ")
    tasks.append({"description": task, "completed": False})
    print("Task added successfully!")

def view_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print("No tasks found!")
        return

    print("\nPending Tasks:")
    for idx, task in enumerate(tasks):
        if not task['completed']:
            print(f"{idx + 1}. {task['description']}")

    print("\nCompleted Tasks:")
    for idx, task in enumerate(tasks):
        if task['completed']:
            print(f"{idx + 1}. {task['description']} (Completed)")

def mark_task_completed(tasks):
    """Mark a task as completed."""
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the task number to mark as completed: "))
        if 0 < task_number <= len(tasks):
            tasks[task_number - 1]['completed'] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def remove_task(tasks):
    """Remove a task from the list."""
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the task number to remove: "))
        if 0 < task_number <= len(tasks):
            tasks.pop(task_number - 1)
            print("Task removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove a Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
