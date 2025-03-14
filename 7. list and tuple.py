def display_menu():
    print("\nTask Manager Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Update Task")
    print("5. Sort Tasks by Priority")
    print("6. Exit")

def view_tasks(task_list):
    if not task_list:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task[0]} (Priority: {task[1]})")

def add_task(task_list):
    task_name = input("Enter the task name: ")
    task_priority = int(input("Enter the task priority (1-5, where 1 is highest): "))
    task_list.append((task_name, task_priority))
    print(f"Task '{task_name}' added with priority {task_priority}.")

def remove_task(task_list):
    view_tasks(task_list)
    if task_list:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(task_list):
            removed_task = task_list.pop(task_number - 1)
            print(f"Task '{removed_task[0]}' removed.")
        else:
            print("Invalid task number.")

def update_task(task_list):
    view_tasks(task_list)
    if task_list:
        task_number = int(input("Enter the task number to update: "))
        if 1 <= task_number <= len(task_list):
            new_task_name = input("Enter the new task name: ")
            new_task_priority = int(input("Enter the new task priority (1-5): "))
            task_list[task_number - 1] = (new_task_name, new_task_priority)
            print(f"Task updated to '{new_task_name}' with priority {new_task_priority}.")
        else:
            print("Invalid task number.")

def sort_tasks(task_list):
    if not task_list:
        print("No tasks available to sort.")
    else:
        # Sort tasks by priority (lower number = higher priority)
        task_list.sort(key=lambda x: x[1])
        print("Tasks sorted by priority.")

def main():
    task_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            view_tasks(task_list)
        elif choice == '2':
            add_task(task_list)
        elif choice == '3':
            remove_task(task_list)
        elif choice == '4':
            update_task(task_list)
        elif choice == '5':
            sort_tasks(task_list)
        elif choice == '6':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
