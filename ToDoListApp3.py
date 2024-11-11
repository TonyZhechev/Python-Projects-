
tasks = []


def show_menu():
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")



def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f'Task "{task}" added!')



def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. {task['task']} [{status}]")



def complete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as complete: ")) - 1
        if tasks[task_num]["completed"]:
            print("Task is already completed.")
        else:
            tasks[task_num]["completed"] = True
            print(f'Task "{tasks[task_num]["task"]}" marked as complete!')
    except (IndexError, ValueError):
        print("Invalid task number.")


def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        task = tasks.pop(task_num)
        print(f'Task "{task["task"]}" deleted!')
    except (IndexError, ValueError):
        print("Invalid task number.")



while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
