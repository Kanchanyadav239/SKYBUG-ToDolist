class Task:
    def __init__(self, title, description, status='Incomplete'):
        self.title = title
        self.description = description
        self.status = status
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task.title} - {task.status}")

    def update_task_status(self, task_index, new_status):
        self.tasks[task_index - 1].status = new_status
def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. Display Tasks")
        print("3. Update Task Status")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            new_task = Task(title, description)
            todo_list.add_task(new_task)
            print("Task added successfully!")

        elif choice == '2':
            print("\n=== To-Do List ===")
            todo_list.display_tasks()

        elif choice == '3':
            todo_list.display_tasks()
            task_index = int(input("Enter the task number to update status: "))
            new_status = input("Enter the new status (e.g., 'Complete' or 'Incomplete'): ")
            todo_list.update_task_status(task_index, new_status)
            print("Task status updated successfully!")

        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        # Widgets
        self.task_entry = tk.Entry(root, width=30)
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.display_button = tk.Button(root, text="Display Tasks", command=self.display_tasks)
        self.quit_button = tk.Button(root, text="Exit", command=root.destroy)

        # Grid layout
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)
        self.display_button.grid(row=1, column=0, columnspan=2, pady=10)
        self.quit_button.grid(row=2, column=0, columnspan=2, pady=10)

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append(task_text)
            messagebox.showinfo("Success", "Task added successfully!")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def display_tasks(self):
        if not self.tasks:
            messagebox.showinfo("Info", "No tasks to display.")
        else:
            task_list = "\n".join(self.tasks)
            messagebox.showinfo("To-Do List", task_list)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
