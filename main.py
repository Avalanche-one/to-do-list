#Menu function
def show_menu():
    title = "To Do List"
    menu_options = {1: "Show Tasks", 2: "Add Task", 3: "Remove Task", 4: "Quit"}
    print("=" * 20)
    print(title)
    print("=" * 20)
    for key, value in menu_options.items():
        print(f"{key}: {value}")
#Tasks list
tasks_list = []
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
        removing_task_number = int(input("Enter task number to remove: ")) - 1
        tasks.pop(removing_task_number)
        print("Your task has been removed!")
    else:
        print("No tasks to remove")
#Main cycle
while True:
    show_menu()
    choice = int(input("Enter your choice: "))
    print(f"You've chosen {choice}")
    if choice == 4:
        break