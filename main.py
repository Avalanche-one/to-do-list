#menu function
def show_menu():
    title = "To Do List"
    menu_options = {1: "Show List", 2: "Add Item", 3: "Remove Item", 4: "Quit"}
    print("=" * 20)
    print(title)
    print("=" * 20)
    for key, value in menu_options.items():
        print(f"{key}: {value}")
#main cycle
while True:
    show_menu()
    choice = int(input("Enter your choice: "))
    print(f"You've chosen {choice}")
    if choice == 4:
        break