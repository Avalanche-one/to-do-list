#Menu function
def show_menu():
    title = "To Do List"
    menu_options = {1: "Show Tasks", 2: "Add Task", 3: "Remove Task", 4: "Quit"}
    print("=" * 20)
    print(title)
    print("=" * 20)
    for key, value in menu_options.items():
        print(f"{key}: {value}")
#Show Tasks Function
def show_tasks(tasks):
    if tasks:
        for key, task in enumerate(tasks, start=1):
            print(f"{key}: {task}")
    else:
        print("No tasks")
#Add Task Function
def add_task(tasks):
    new_task = input("Enter new task: ")
    tasks.append(new_task)
    print("Your new task has been added!")
#Remove Task Function
def remove_task(tasks):
    show_tasks(tasks)
    print("=" * 20)
    if tasks:
        try:
            removing_task_number = int(input("Enter task number to remove: ")) - 1
            if removing_task_number < 0:
                raise ValueError
            else:
                tasks.pop(removing_task_number)
                print("Your task has been removed!")
        except (ValueError, IndexError):
            print("You must enter a valid number")
    else:
        print("No tasks to remove")
#Tasks List
tasks_list = []
#Main cycle
while True:
    show_menu()
    try:
        choice = int(input("Enter your choice: "))
        if choice not in [1, 2, 3, 4]:
            print("Please enter a number between 1 and 4")
        elif choice == 1:
            show_tasks(tasks_list)
        elif choice == 2:
            add_task(tasks_list)
        elif choice == 3:
            remove_task(tasks_list)
        elif choice == 4:
            break
    except ValueError:
        print("You must enter a valid number")