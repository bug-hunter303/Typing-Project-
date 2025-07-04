import Sentences
import customtkinter as ctk
import time 
import Calculation

start_time = None
first_key = True
original_sentence = Sentences.sentence_select()

def first_keyy(event = None):
    global start_time , first_key
    if first_key:
        start_time = time.time()
        first_key = False


def on_enter(event = None):
    global start_time , first_key

    user_input = user_entry.get()
    end_time = time.time()

    if start_time is not None:
        elapsed_time = round(end_time - start_time , 2)

        stats = Calculation.calculations(original_sentence,user_input,elapsed_time)

        result_label.configure(
            text=f"Accuracy: {stats['accuracy']}%\n"
                 f"WPM: {stats['wpm']}\n"
                 f"Time Taken: {stats['elapsed_time']} seconds"
        )

    # user_entry.delete(0,'end')
    first_key = True
    start_time = None
    


root = ctk.CTk()
root.title('Typing Meter')
root.geometry("500x500")

ctk.set_appearance_mode("dark")

display = ctk.CTkLabel(master=root,text="The sentence is :",font=('Times New Roman',20))
display.pack(pady=10)
display = ctk.CTkLabel(master=root,text=original_sentence,font=('Arial',20))
display.pack()

input = ctk.CTkLabel(master=root,text="Type the text give above :" , font=('Times New Roman',20))
input.pack(pady=10)
user_entry = ctk.CTkEntry(master=root, placeholder_text="Start Typing...",text_color='yellow' , font=('Arial',20),width=450)
user_entry.pack()

user_entry.bind("<Key>",first_keyy)
user_entry.bind("<Return>",on_enter)

result_label = ctk.CTkLabel(root, text="", font=("Arial", 16), wraplength=400)
result_label.pack(pady=20)

root.mainloop()



