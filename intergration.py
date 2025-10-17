import tkinter as tk
import sqlite3

root = tk.Tk()
root.title("Three Layer Architecture")
root.geometry("300x350")

label_id = tk.Label(root, text="Studemt_ID:")
label_id.pack(pady=[15.5])
entry_id = tk.Entry(root,width=25)
entry_id.pack()

label_name = tk.Label(root, text="Student_Name:")
label_name.pack(pady=[10.5])
entry_name = tk.Entry(root,width=25)
entry_name.pack()

def print_Student():
    student_id = entry_id.get()
    student_name = entry_name.get()
    
    print ('Student ID:{student_id}')
    print ('Student Name:{student_name}')
    print ('-'*30)

button_print = tk.Button(root, text="Print", command=print_Student)
button_print.pack(pady=[15])

root.mainloop()