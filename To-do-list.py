def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- To-Do List Application ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")
    print("----------------------------")

def add_task(tasks):
    """Prompts the user for a new task and adds it to the list."""
    task = input("Enter the task description: ").strip()
    if task:
        tasks.append({"description": task, "completed": False})
        print(f"Task '{task}' added successfully!")
    else:
        print("Task description cannot be empty.")

def view_tasks(tasks):
    """Displays all tasks with their status (complete/incomplete)."""
    if not tasks:
        print("\nNo tasks in your list yet.")
        return

    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks):
        status = "✓" if task["completed"] else " "
        print(f"{i + 1}. [{status}] {task['description']}")
    print("--------------------")

def mark_task_complete(tasks):
    """Allows the user to mark a task as complete."""
    view_tasks(tasks) # Show tasks so user can choose
    if not tasks:
        return

    try:
        task_number = int(input("Enter the number of the task to mark as complete: ")) - 1
        if 0 <= task_number < len(tasks):
            if not tasks[task_number]["completed"]:
                tasks[task_number]["completed"] = True
                print(f"Task '{tasks[task_number]['description']}' marked as complete!")
            else:
                print("This task is already marked as complete.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    """Allows the user to delete a task from the list."""
    view_tasks(tasks) # Show tasks so user can choose
    if not tasks:
        return

    try:
        task_number = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= task_number < len(tasks):
            removed_task = tasks.pop(task_number)
            print(f"Task '{removed_task['description']}' deleted successfully!")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """The main function to run the To-Do List application."""
    tasks = [] # List to store tasks. Each task is a dictionary.

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()