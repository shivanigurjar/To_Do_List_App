import tkinter as tk
from tkinter import messagebox, Button, Entry, Frame, LEFT, BOTH, END, Scrollbar, RIGHT, Listbox, ANCHOR

# Dummy user data
users = {"user1": "root123", "user2": "root789"}

def authenticate(username, password):
    """Authenticate user"""
    return users.get(username) == password

def login():
    """Handle login"""
    username = username_entry.get()
    password = password_entry.get()
    if authenticate(username, password):
        messagebox.showinfo("Login", "Login successful")
        show_todo_list(username)
    else:
        messagebox.showerror("Login Error", "Invalid username or password")

def show_todo_list(username):
    """Display To-Do list"""
    def newTask():
        task = my_entry.get()
        if task != "":
            Lb.insert(END, task)
            my_entry.delete(0, "end")
        else:
            messagebox.showwarning("warning", "Please enter some task.")

    def deleteTask():
        Lb.delete(ANCHOR)
        
    todo_window = tk.Toplevel(root)
    todo_window.title(f"To-Do List - {username}")
    
    frame = Frame(todo_window)
    frame.pack(pady=10)

    Lb = Listbox(
        frame,
        height=8,
        width=25,
        selectbackground="#a6a6a6",
        fg='#464646',
        font=('Times', 18),
        bd=0,
        highlightthickness=0,
        activestyle='none',
    )
    addTask_btn = Button(
        frame,
        text='Add Task',
        font=('times 14'),
        bg='#c5f776',
        padx=20,
        pady=10,
        command=newTask
    )
    addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

    delTask_btn = Button(
        frame,
        text='Delete Task',
        font=('times 14'),
        bg='#ff8b61',
        padx=20,
        pady=10,
        command=deleteTask
    )
    delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

    task_list = [
        'Eat apple',
        'drink water',
        'go gym',
        'write to software',
        'write to documentation',
        'take a nap',
        'learn something',
        'paint canvas',
    ]
    for item in task_list:
        Lb.insert(END, item)

    sb = Scrollbar(frame)
    sb.pack(side=RIGHT, fill=BOTH)

    Lb.config(yscrollcommand=sb.set)
    sb.config(command=Lb.yview)

    my_entry = Entry(
        todo_window,
        font=('times', 24)
    )
    my_entry.pack(pady=20)

    Lb.pack(side=LEFT, fill=BOTH)

    def newTask():
        task = my_entry.get()
        if task != "":
            Lb.insert(END, task)
            my_entry.delete(0, "end")
        else:
            messagebox.showwarning("warning", "Please enter some task.")

    def deleteTask():
        Lb.delete(ANCHOR)

# Main window
root = tk.Tk()
root.geometry('500x450+500+200')
root.title('PythonGuides')
root.config(bg='#223441')
root.resizable(width=False, height=False)

# Login GUI
login_frame = tk.Frame(root)
login_frame.pack(pady=20)

tk.Label(login_frame, text="Username:").grid(row=0, column=0)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1)

tk.Label(login_frame, text="Password:").grid(row=1, column=0)
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1)

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.grid(row=2, columnspan=2)

root.mainloop()
