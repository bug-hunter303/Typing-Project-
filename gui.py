# import tkinter as tk 
import logic1
import customtkinter as ctk

a = logic1.sentence_select()


root = ctk.CTk()
root.title('Typing Meter')
root.geometry("500x500")

ctk.set_appearance_mode("dark")



display = ctk.CTkLabel(master=root,text="The sentence is :",font=('Times New Roman',20))
#display.place(relx=0.5, rely=0.1, anchor='center')
display.pack(pady=10)
display = ctk.CTkLabel(master=root,text=a,font=('Arial',20))
display.pack()


root.mainloop()



