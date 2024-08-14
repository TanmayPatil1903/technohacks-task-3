import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x300")

        # List to store tasks
        self.tasks = []

        # Task input
        self.task_label = tk.Label(root, text="Task")
        self.task_label.grid(row=0, column=0, padx=10, pady=10)

        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=1, padx=10, pady=10)

        self.description_label = tk.Label(root, text="Description")
        self.description_label.grid(row=1, column=0, padx=10, pady=10)

        self.description_entry = tk.Entry(root, width=30)
        self.description_entry.grid(row=1, column=1, padx=10, pady=10)

        # Buttons
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=2, column=0, padx=10, pady=10)

        self.show_button = tk.Button(root, text="Show Tasks", command=self.show_tasks)
        self.show_button.grid(row=2, column=1, padx=10, pady=10)

        self.clear_button = tk.Button(root, text="Clear All", command=self.clear_tasks)
        self.clear_button.grid(row=2, column=2, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        description = self.description_entry.get()
        if task:
            self.tasks.append({'task': task, 'description': description})
            self.task_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Task added successfully!")
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def show_tasks(self):
        self.task_window = tk.Toplevel(self.root)
        self.task_window.title("Task List")

        for i, task in enumerate(self.tasks):
            tk.Label(self.task_window, text=task['task']).grid(row=i, column=0, padx=10, pady=5)
            tk.Label(self.task_window, text=task['description']).grid(row=i, column=1, padx=10, pady=5)
            tk.Button(self.task_window, text="Edit", command=lambda i=i: self.edit_task(i)).grid(row=i, column=2, padx=10, pady=5)
            tk.Button(self.task_window, text="Delete", command=lambda i=i: self.delete_task(i)).grid(row=i, column=3, padx=10, pady=5)

    def edit_task(self, index):
        task_to_edit = self.tasks[index]

        self.edit_window = tk.Toplevel(self.root)
        self.edit_window.title("Edit Task")

        tk.Label(self.edit_window, text="Task").grid(row=0, column=0, padx=10, pady=10)
        task_entry = tk.Entry(self.edit_window, width=30)
        task_entry.grid(row=0, column=1, padx=10, pady=10)
        task_entry.insert(0, task_to_edit['task'])

        tk.Label(self.edit_window, text="Description").grid(row=1, column=0, padx=10, pady=10)
        description_entry = tk.Entry(self.edit_window, width=30)
        description_entry.grid(row=1, column=1, padx=10, pady=10)
        description_entry.insert(0, task_to_edit['description'])

        tk.Button(self.edit_window, text="Save", command=lambda: self.save_task(index, task_entry.get(), description_entry.get())).grid(row=2, column=1, padx=10, pady=10)

    def save_task(self, index, task, description):
        if task:
            self.tasks[index] = {'task': task, 'description': description}
            self.edit_window.destroy()
            self.task_window.destroy()
            self.show_tasks()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self, index):
        del self.tasks[index]
        self.task_window.destroy()
        self.show_tasks()

    def clear_tasks(self):
        self.tasks.clear()
        messagebox.showinfo("Success", "All tasks cleared!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
