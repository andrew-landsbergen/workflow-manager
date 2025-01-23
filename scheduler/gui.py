import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from task import Task

class SchedulerGUI:
    def __init__(self, scheduler):
        self.scheduler = scheduler

        self.window = tk.Tk()
        self.window.title("Task Scheduler")

        # Task listbox
        self.task_listbox = tk.Listbox(self.window, height=10, width=50)
        self.task_listbox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Buttons for task manipulation
        self.add_button = tk.Button(self.window, text="Add Task", command=self.add_task)
        self.add_button.grid(row=1, column=0, padx=10, pady=10)

        self.remove_button = tk.Button(self.window, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=1, column=1, padx=10, pady=10)

        self.start_button = tk.Button(self.window, text="Start Scheduler", command=self.start_scheduler)
        self.start_button.grid(row=1, column=2, padx=10, pady=10)

        # Start the GUI
        self.refresh_task_list()
        self.window.mainloop()

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.scheduler.get_tasks():
            self.task_listbox.insert(tk.END, f"{task.name} - Priority: {task.priority}")

    def add_task(self):
        name = simpledialog.askstring("Task Name", "Enter task name:")
        priority = simpledialog.askinteger("Priority", "Enter task priority (1 to 3):")

        if name and priority:
            new_task = Task(name=name, priority=priority)
            self.scheduler.add_task(new_task)
            self.refresh_task_list()

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.scheduler.get_tasks()[selected_task_index[0]]
            self.scheduler.remove_task(task)
            self.refresh_task_list()

    def start_scheduler(self):
        self.scheduler.run()