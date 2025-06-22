def todo_list_app():
    tasks = []

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the new task: ")
            tasks.append(task)
            print("Task added successfully.")

        elif choice == '2':
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\nYour Tasks:")
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")

        elif choice == '3':
            if not tasks:
                print("No tasks to edit.")
            else:
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")
                try:
                    task_no = int(input("Enter the task number to edit: "))
                    if 1 <= task_no <= len(tasks):
                        new_task = input("Enter the new task content: ")
                        tasks[task_no - 1] = new_task
                        print("Task updated.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == '4':
            if not tasks:
                print("No tasks to delete.")
            else:
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")
                try:
                    task_no = int(input("Enter the task number to delete: "))
                    if 1 <= task_no <= len(tasks):
                        removed = tasks.pop(task_no - 1)
                        print(f"Task '{removed}' deleted.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == '5':
            print("Have a productive day!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

todo_list_app()
