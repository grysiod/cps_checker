from tkinter import *
import threading

cps = 0
score = 0
st = 0
timer_running = False 
cps_result = 0.0  
click_started = False  
button_enabled = False  

def tichotataspi(): 
    global cps, timer_running, st, click_started, button_enabled
    cps += 1
    print(cps)
    
    if not click_started:  
        click_started = True
        start_timer(st)
        
    button_enabled = True  

def start_timer(duration): 
    global st, timer_running
    st = duration
    button.config(state="normal")
    timer_running = True  

def check_clicks(): 
    global timer_running, button_enabled
    print("czek")
    if cps > 0 or button_enabled:
        stop_timer()
    else:
        button.config(state="disabled")
        timer_running = False

def stop_timer(): 
    global cps, cps_result, button_enabled
    
    button.config(state="disabled")
    cps_result = cps / st  
    score1.config(text="Score: " + str(cps_result) + "  CPS")  
    cps = 0
    button_enabled = False
    

def all():
    global st, cps
    while True:
        if cps > 1:
            print("jocie")
            root.after(st * 1000, check_clicks)
            break
        

t10 = threading.Thread(target=all)

bgcolor = "#232925"
fgcolor = "#27f26e"
root = Tk()
root.geometry("700x650")
root.title("Cps_checker")
root.configure(bg=bgcolor)

text = Label(text="Cps checker\n", bg=bgcolor, fg=fgcolor, font=("System", 32))
text.pack(pady=20)

score1 = Label(text="Score: " + str(score) + "  CPS", bg=bgcolor, fg=fgcolor, font=("System", 8))
score1.pack(pady=20)

t1 = Button(text="5 second", bg=fgcolor, width=18, height=5, fg="black", font=("System", 8), 
            command=lambda: start_timer(5)) 
t2 = Button(text="10 second", bg=fgcolor, width=18, height=5, fg="black", font=("System", 8),
            command=lambda: start_timer(10))
t3 = Button(text="15 second", bg=fgcolor, width=18, height=5, fg="black", font=("System", 8),
            command=lambda: start_timer(15))

button = Button(text="Click me!", font=("System", 18), width=50, height=10, bg="#10692f",
                activeforeground="#000000",activebackground="#15ad4a", fg="#ffffff",
                command=tichotataspi, cursor="cross", state="disabled") 
button.pack(padx=10, pady=20)
t1.pack(side= LEFT,expand=True, padx=20, pady=5)
t2.pack(side= LEFT,expand=True, padx=20, pady=5)
t3.pack(side= LEFT,expand=True, padx=20, pady=5)

root.resizable(False,False)
t10.start()  # Uruchomienie wątku przed główną pętlą tkinter
root.mainloop()
