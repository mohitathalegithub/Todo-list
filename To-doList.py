from tkinter import *

class ToDoList:
    def __init__(self, root):
        self.tasks = []
        self.root = root
        self.listbox = Listbox(self.root)
        self.entry = Entry(self.root)
        self.addButton = Button(self.root, text="Add Task", command=self.add_task)
        self.delButton = Button(self.root, text="Delete Task", command=self.delete_task)
        self.doneButton = Button(self.root, text="Completed", command=self.mark_as_done)
        self.completedListbox = Listbox(self.root)

        # GUI Layout
        self.entry.pack()
        self.addButton.pack()
        self.listbox.pack()
        self.delButton.pack()
        self.doneButton.pack()
        self.completedListbox.pack()

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.listbox.insert(END, task)
            self.entry.delete(0, END)

    def delete_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            self.listbox.delete(task_index)
        except IndexError:
            pass

    def mark_as_done(self):
        try:
            task_index = self.listbox.curselection()[0]
            completed_task = self.listbox.get(task_index)
            self.listbox.delete(task_index)
            self.completedListbox.insert(END, completed_task)
        except IndexError:
            pass

root = Tk()
root.title("Python To-Do List")
root.geometry("800x800") 
to_do_list = ToDoList(root)
root.mainloop()
