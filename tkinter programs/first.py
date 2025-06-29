import tkinter as tk
from tkinter import messagebox
from openpyxl import load_workbook
import openpyxl

root = tk.Tk()
file_path = r"C:\Users\ankit\Documents\Book1.xlsx"
A = openpyxl.load_workbook(file_path)
B = A["Sheet1"] # B represents the sheet 

def on_click(): 
    name = name_textbox.get()
    email = email_textbox.get()

    if name and email:
        B.append([name,email])
        A.save(file_path)
        messagebox.showinfo("Success","All the data in the field have been submitted")
    else:
        messagebox.showwarning("Invalid","Data Input is missing")


root.title('Student Registration Form')
root.geometry("300x500")

name_textbox = tk.Label(root,text="Enter text")
name_textbox.pack(padx=10,anchor=tk.W)
name_textbox = tk.Entry(root)
name_textbox.pack(padx=10,anchor=tk.W)

email_textbox = tk.Label(root,text="Enter email")
email_textbox.pack(padx=10,anchor=tk.W)
email_textbox = tk.Entry(root)
email_textbox.pack(padx=10,anchor=tk.W)

submit_button = tk.Button(root,text="Submit",command=on_click)
submit_button.pack(anchor=tk.W , padx=10)



root.mainloop()