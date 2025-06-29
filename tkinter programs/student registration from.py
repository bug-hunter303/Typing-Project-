import tkinter as tk 
from tkinter import messagebox

root = tk.Tk()

def submit_click():
    name , mobile , email = name_textbox.get() , mobile_textbox.get() , email_textbox.get()
    
    if name and email and mobile:
        messagebox.showinfo("Status","Data Submitted")
    else:
        messagebox.showwarning("Empty Field Exists","Fill the fields")



root.geometry("300x400")
root.title("Student Registration Form")
 # root.configure(bg = " ")


name_textbox = tk.Label(root,text="Enter Name")
name_textbox.pack(anchor=tk.W , padx=10)
name_textbox = tk.Entry(root)
name_textbox.pack(anchor=tk.W , padx=10)

email_textbox = tk.Label(root,text="Enter Email")
email_textbox.pack(anchor=tk.W , padx=10)
email_textbox = tk.Entry(root)
email_textbox.pack(anchor=tk.W , padx=10)

mobile_textbox = tk.Label(root,text="Phone")
mobile_textbox.pack(anchor=tk.W , padx=10)
mobile_textbox = tk.Entry(root)
mobile_textbox.pack(anchor=tk.W , padx=10)

submit_button = tk.Button(root , text='Submit' , command= submit_click) # no submit_click() cause only after the user clicks the submit the function runs 
submit_button.pack(anchor=tk.W , padx=10 , pady=10)




root.mainloop()