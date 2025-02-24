import tkinter as tk
from tkinter import messagebox, simpledialog
import json
from tkcalendar import Calendar

class TaskManager:
    def __init__(self, root):  # Fixed __init__ method
        self.root = root
        self.root.title("Task Manager")
        
        self.tasks = []
        
        self.listbox = tk.Listbox(root, width=50, height=15)
        self.listbox.pack(pady=10)
        self.listbox.bind("<B1-Motion>", self.drag_task)
        self.listbox.bind("<ButtonRelease-1>", self.drop_task)
        
        button_frame = tk.Frame(root)
        button_frame.pack()
        
        self.add_btn = tk.Button(button_frame, text="Add Task", command=self.add_task)
        self.add_btn.grid(row=0, column=0, padx=5)
        
        self.edit_btn = tk.Button(button_frame, text="Edit Task", command=self.edit_task)
        self.edit_btn.grid(row=0, column=1, padx=5)
        
        self.delete_btn = tk.Button(button_frame, text="Delete Task", command=self.delete_task)
        self.delete_btn.grid(row=0, column=2, padx=5)
        
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)
        
        file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save", command=self.save_tasks)
        file_menu.add_command(label="Load", command=self.load_tasks)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        
        self.dragged_item = None
    
    def add_task(self):
        title = simpledialog.askstring("Add Task", "Enter task title:")
        deadline = self.get_deadline()
        if title and deadline:
            self.tasks.append((title, deadline))
            self.listbox.insert(tk.END, f"{title} - {deadline}")
    
    def edit_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            title, deadline = self.tasks[index]
            new_title = simpledialog.askstring("Edit Task", "Edit title:", initialvalue=title)
            new_deadline = self.get_deadline(initial_deadline=deadline)
            if new_title and new_deadline:
                self.tasks[index] = (new_title, new_deadline)
                self.listbox.delete(index)
                self.listbox.insert(index, f"{new_title} - {new_deadline}")
        else:
            messagebox.showwarning("Edit Task", "Please select a task to edit.")
    
    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks.pop(index)
            self.listbox.delete(index)
        else:
            messagebox.showwarning("Delete Task", "Please select a task to delete.")
    
    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)
        messagebox.showinfo("Save", "Tasks saved successfully!")
    
    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
                self.listbox.delete(0, tk.END)
                for title, deadline in self.tasks:
                    self.listbox.insert(tk.END, f"{title} - {deadline}")
            messagebox.showinfo("Load", "Tasks loaded successfully!")
        except FileNotFoundError:
            messagebox.showwarning("Load", "No saved tasks found.")
    
    def get_deadline(self, initial_deadline=None):
        top = tk.Toplevel(self.root)
        top.title("Select Deadline")
        cal = Calendar(top, selectmode='day')
        cal.pack(pady=20)
        
        def confirm():
            top.selected_date = cal.get_date()
            top.destroy()
        
        tk.Button(top, text="Select", command=confirm).pack()
        top.wait_window()
        return getattr(top, 'selected_date', initial_deadline)
    
    def drag_task(self, event):
        index = self.listbox.nearest(event.y)
        if index != self.dragged_item:
            self.dragged_item = index
    
    def drop_task(self, event):
        if self.dragged_item is not None:
            new_index = self.listbox.nearest(event.y)
            if new_index != self.dragged_item:
                self.tasks.insert(new_index, self.tasks.pop(self.dragged_item))
                self.update_listbox()
            self.dragged_item = None
    
    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for title, deadline in self.tasks:
            self.listbox.insert(tk.END, f"{title} - {deadline}")

if __name__ == "__main__":  # Fixed __name__ check
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
