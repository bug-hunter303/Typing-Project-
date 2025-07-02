import customtkinter as ctk

root = ctk.CTk()
root.geometry("500x500")

display = ctk.CTkLabel(master=root,text="The sentence is :")
display.place()

root.mainloop()