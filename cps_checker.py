from tkinter import *
import time
cps = 0

def tichotataspi():
    global cps
    cps += 1
    print(cps)
    
def switch():
    if button["state"] == "normal":
        button["state"] = "disable"
        b1["text"] = "enable"
    else:
        button["state"] = "normal"
        b1["text"] = "disable"

bgcolor = "#232925"
fgcolor = "#27f26e"
root = Tk()
root.geometry("700x500")

root.title("Cps_checker")

root.configure(bg=bgcolor)



text = Label(text="Cps checker\n\n", bg=bgcolor, fg=fgcolor, font=("System", 32))
text.pack()

b1 = Button(text="5s", command=switch)




button = Button(text="Click me!", font=("System", 18), width=50, height=10, bg="#10692f",
                 activeforeground="#000000",activebackground="#15ad4a", fg="#ffffff",
                   command=tichotataspi, cursor="cross", relief=RAISED, state="normal") 
button.pack(padx=10, pady=20)
root.mainloop()

