#make a to do list application
import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x600")  # Set the initial window size
        self.root.resizable(True, True)  # Make the window resizable
        self.tasks = []

        # Create a frame for the task list
        self.task_list_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.task_list_frame.pack(fill="both", expand=True)

        # Create a scrollbar for the task list
        self.scrollbar = tk.Scrollbar(self.task_list_frame)
        self.scrollbar.pack(side="right", fill="y")

        # Create a listbox for the tasks
        self.task_list = tk.Listbox(self.task_list_frame, bg="#f0f0f0", fg="#333333", font=("Helvetica", 12), yscrollcommand=self.scrollbar.set)
        self.task_list.pack(side="left", fill="both", expand=True)

        # Configure the scrollbar
        self.scrollbar.config(command=self.task_list.yview)

        # Create a frame for the entry field and buttons
        self.entry_frame = tk.Frame(self.root, bg="#333333")
        self.entry_frame.pack(fill="x")
        self.entry_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Create an entry field for new tasks
        self.new_task_entry = tk.Entry(self.entry_frame, font=("Helvetica", 15), width=30)
        self.new_task_entry.pack(side="top", fill="x", padx=10, pady=10)

        # Create buttons
        self.add_task_button = tk.Button(self.entry_frame, text="Add Task", command=self.add_task, bg="#4CAF50", fg="#ffffff", font=("Helvetica", 12))
        self.add_task_button.pack(side="top", fill="x", padx=10, pady=10 )

        self.delete_task_button = tk.Button(self.entry_frame, text="Delete Task", command=self.delete_task, bg="#e74c3c", fg="#ffffff", font=("Helvetica", 12))
        self.delete_task_button.pack(side="top", fill="x", padx=10, pady=10)

        self.update_task_button = tk.Button(self.entry_frame, text="Update Task", command=self.update_task, bg="#3498db", fg="#ffffff", font=("Helvetica", 12))
        self.update_task_button.pack(side="top", fill="x", padx=10, pady=10)

        self.clear_all_button = tk.Button(self.entry_frame, text="Clear All", command=self.clear_all, bg="#2ecc71", fg="#ffffff", font=("Helvetica", 12))
        self.clear_all_button.pack(side="top", fill="x", padx=10, pady=10)

    def add_task(self):
        task = self.new_task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert("end", task)
            self.new_task_entry.delete(0, "end")

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
            self.tasks.pop(task_index)
        except IndexError:
            messagebox.showwarning("Error", "Select a task to delete")

    def update_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            task = self.tasks[task_index]
            new_task = self.new_task_entry.get()
            if new_task:
                self.tasks[task_index] = new_task
                self.task_list.delete(task_index)
                self.task_list.insert(task_index, new_task)
                self.new_task_entry.delete(0, "end")
        except IndexError:
            messagebox.showwarning("Error", "Select a task to update")

    def clear_all(self):
        self.tasks = []
        self.task_list.delete(0, "end")

if __name__ == "__main__":
    root = tk.Tk()
    todo_list = ToDoList(root)
    root.mainloop()