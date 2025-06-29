import tkinter as tk

root = tk.Tk() 



name_label = tk.Label(root,text="Enter Name")
name_label.pack()

name_textbox = tk.Entry(root)
name_textbox.pack() # organises in the geometric place

email_label = tk.Label(root,text="Enter Email")
email_label.pack()
email_text = tk.Entry(root)
email_text.pack()

root.mainloop()
