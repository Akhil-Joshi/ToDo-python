from click import confirm

tasks = []

print("Welcome to the To-Do List")

def add_task():
    task_and_status = []
    while True:
        print("\nEnter 'done' to finish. Enter the task you want to do:")
        task = input()
        if task.lower() == 'done':
            break
        status = input("Enter the status: ")
        task_and_status.append((task, status))
    tasks.append(task_and_status)

def check_task_status():
    if not tasks:
        print("No tasks available.")
    else:
        task_to_check = input("\nEnter the task you want to check the status for: ")
        found = False
        for task_list in tasks:
            for task, status in task_list:
                if task == task_to_check:
                    print(f"The status of '{task}' is '{status}'.")
                    found = True
                    break
            if found:
                break
        if not found:
            print(f"The task '{task_to_check}' does not exist.")

def update_status():
    if not tasks:
        print("No tasks available.")
    else:
        task_to_update = input("\nEnter the task you want to update the status for: ")
        found = False
        for task_list in tasks:
            for i, (task, status) in enumerate(task_list):
                if task == task_to_update:
                    new_status = input(f"Enter the new status for '{task}': ")
                    tasks[i] = (task, new_status)
                    print(f"The status of '{task}' has been updated to '{new_status}'.")
                    found = True
                    break
            if found:
                break
        if not found:
            print(f"The task '{task_to_update}' does not exist.")

def delete_task():
    if not tasks:
        print("No tasks available.")
    else:
        task_to_delete = input("\nEnter the task you want to delete: ")
        found = False
        for task_list in tasks:
            for i, (task, status) in enumerate(task_list):
                if task == task_to_delete:
                    tasks.remove(task_list)
                    print(f"The task '{task_to_delete}' has been deleted.")
                    found = True
                    break
            if found:
                break
        if not found:
            print(f"The task '{task_to_delete}' does not exist.")


def display():
    if not tasks:
        print("No tasks available.")
    else:
        print("List of tasks: \n")
        for task_list in tasks:
            for task, status in task_list:
                print(f"{task}: {status}")
            print()  # Print an empty line to separate tasks

def end_task():
    result = confirm("\nAre you sure you want to exit: ")
    if result:
        print("Thanks for using the ToDo app!\n")
        exit()
    else:
        print("Resuming...\n")

print("\n1. Add task.\n2. Check task status.\n3. Update task status.\n4. Delete task.\n5. Display tasks.\nPress 0 to quit.\n")

while True:
    command = input("Enter the command: ")
    if command == '1':
        add_task()
    elif command == '2':
        check_task_status()
    elif command == '3':
        update_status()
    elif command == '4':
        delete_task()
    elif command == '5':
        display()
    elif command == '0':
        end_task()
    else:
        print("Command error!! \nPlease enter the correct command.")
