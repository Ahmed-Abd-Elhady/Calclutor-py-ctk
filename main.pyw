import customtkinter as ctk
import random



#root applaction window
app = ctk.CTk()
app.geometry("300x370")
app.title("Calculator")
app.resizable(False, False)
#consttttt
Apllaction_them = "dark"


#____Functions_____
def insert_one(button_name):
    index = 0
    lens_of_entry = len(entry.get())
    try:
        for x in range(lens_of_entry):
            index = int(x) +1
        if button_name.cget("text") == 'DC':
            entry.delete(index-1,index)
            return
    except Exception as e:
        print(f"Error : {e}")
    entry.insert(index,f"{button_name.cget("text")}")
    if button_name.cget("text") == 'AC':
        entry.delete(0, 'end')

def equal_sum ():
    sum = eval(entry.get())
    entry.delete(0, 'end')
    entry.insert(0,sum)
ctk.set_appearance_mode(Apllaction_them)
ctk.set_default_color_theme("blue")


def Create_button(button_name,text,x,y):
    for_name = random.sample(range(0, 20 + 1),2)
    button_name + f"{for_name}"
    button_name = ctk.CTkButton(app, text=f"{text}", width=50, height=50, font=("Arial", 30) ,command=lambda:insert_one(button_name))
    button_name.place(x=x, y=y)
entry = ctk.CTkEntry(app, width=280, height=50, font=("Arial", 30))
entry.place(x=12 , y=12)

#entry.insert(0," ")
#____Number 1 ______
Create_button("c","1",20,120)

#____Number 2 ______
Create_button("c","2",80,120)

#____Number 3 ______
Create_button("c","3",140,120)

#____Number 4 ______
Create_button("c","4",20,180)

#____Number 5 ______
Create_button("c","5",80,180)

#____Number 6 ______
Create_button("c","6",140,180)

#____Number 7 ______
Create_button("c","7",20,240)

#____Number 8 ______
Create_button("c","8",80,240)

#____Number 9 ______
Create_button("c","9",140,240)

#____Number + ______
Create_button("c","+",200,120)

#____Number - ______
Create_button("c","-",200,180)

#____Number / ______
Create_button("c","/",200,240)

#____Number *______
Create_button("c","*",20,300)

#____Number *______
Create_button("c","0",80,300)

#____Number .______
Create_button("c",".",140,300)

#____Number AC ______
btn_number_AC = ctk.CTkButton(app, text="AC", width=50, height=30, font=("Arial", 30) ,command=lambda:insert_one(btn_number_AC))
btn_number_AC.place(x=20, y=70)
#____Number DC ______
btn_number_DC = ctk.CTkButton(app, text="DC", width=50, height=30, font=("Arial", 30) ,command=lambda:insert_one(btn_number_DC))
btn_number_DC.place(x=80, y=70)

#____Number =______
equal = ctk.CTkButton(app, text="=", width=50, height=50, font=("Arial", 30) ,command=equal_sum)
equal.place(x=200, y=300)
app.mainloop()
