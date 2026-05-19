import tkinter as tk

#add task function
def add_task():
    task = entry.get()        # отримати текст з поля вводу
    if task:
        listbox.insert(tk.END, task)  # додати в кінець списку
        entry.delete(0, tk.END)       # очистити поле вводу
        save_tasks()
#remove task function
def remove_task():
    selected = listbox.curselection()  # індекс виділеного елементу
    if selected:
        listbox.delete(selected)       # видалити виділений елемент
        save_tasks()
#save our very first and only one window into variable
window = tk.Tk()
#add title at the top of our window
window.title("To Do List")
#size of our window - 400 px width and 500 px height
window.geometry("400x500")
#add title INTO the window
title_label = tk.Label(window, text="To Do List", font=("Arial", 16, "bold"))
title_label.pack(pady=10)
#add list with our tasks
listbox = tk.Listbox(window, width=40, height=10)
listbox.pack(pady=10)
#entry field
entry = tk.Entry(window, width=40)
entry.pack(pady=5)
#add buttons - add task and remove task
add_button = tk.Button(window, text="Додати", command=add_task)
add_button.pack(pady=5)
remove_button = tk.Button(window, text="Видалити", command=remove_task)
remove_button.pack(pady=5)

#save function
def save_tasks():
    tasks = listbox.get(0, tk.END)  # отримати всі елементи з Listbox
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task}\n")
#load function
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass
load_tasks()
window.mainloop()