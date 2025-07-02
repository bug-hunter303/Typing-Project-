import tkinter as tk
import test1

def send_input():
    user_input = box_input.get("1.0", tk.END).strip()
    result = test1.process_text(user_input)
    print("Returned:", result)

root = tk.Tk()
root.geometry("500x500")

box_input = tk.Text(root, height=5, width=40)
box_input.pack()

send_btn = tk.Button(root, text="Send to test1", command=send_input)
send_btn.pack()

root.mainloop()
