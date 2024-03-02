from tkinter import *

cps = 0
score = 0
st = 0
timer_running = False 
cps_result = 0.0  
click_started = False  # Flaga informująca, czy kliknięcia się rozpoczęły
button_enabled = False  # Flaga informująca, czy przycisk powinien być włączony

def tichotataspi():
    global cps, timer_running, st, click_started, button_enabled
     
    cps += 1
    print(cps)
    
    if not click_started:  # Jeśli kliknięcia jeszcze się nie rozpoczęły, uruchamiamy timer
        click_started = True
        start_timer(st)
        
    button_enabled = True  # Ustawiamy flagę, że przycisk powinien być włączony

def start_timer(duration):
    global st, timer_running
     
    st = duration
    button.config(state="normal")
    timer_running = True  # Ustawiamy flagę, że timer jest włączony
    root.after(duration * 1000, check_clicks)

def check_clicks():
    global timer_running, button_enabled

    if cps > 0 or button_enabled:
        stop_timer()
    else:
        button.config(state="disabled")
        timer_running = False

def stop_timer():
    global cps, cps_result, button_enabled
    
    button.config(state="disabled")
    cps_result = cps / st  # Zapisujemy wynik CPS
    score1.config(text="Score: " + str(cps_result) + "  CPS")  # Aktualizujemy etykietę z wynikiem
    cps = 0
    button_enabled = False

bgcolor = "#232925"
fgcolor = "#27f26e"
root = Tk()
root.geometry("700x650")
root.title("Cps_checker")
root.configure(bg=bgcolor)

text = Label(text="Cps checker\n", bg=bgcolor, fg=fgcolor, font=("System", 32))
text.pack(pady=20)

score1 = Label(text="Score: " + str(score) + "  CPS", bg=bgcolor, fg=fgcolor, font=("System", 8))
text.pack(pady=20)
score1.pack()

t1 = Button(text="5 second", bg=fgcolor, width=18, height=5, fg="black", font=("System", 8), 
            command=lambda: start_timer(5)) 
t2 = Button(text="10 second", bg=fgcolor, width=18, height=5, fg="black", font=("System", 8),
            command=lambda: start_timer(10))
t3 = Button(text="15 second", bg=fgcolor, width=18, height=5, fg="black", font=("System", 8),
            command=lambda: start_timer(15))

button = Button(text="Click me!", font=("System", 18), width=50, height=10, bg="#10692f",
                activeforeground="#000000",activebackground="#15ad4a", fg="#ffffff",
                command=tichotataspi, cursor="cross", state="disable") 
button.pack(padx=10, pady=20)
t1.pack(side= LEFT,expand=True, padx=20, pady=5)
t2.pack(side= LEFT,expand=True, padx=20, pady=5)
t3.pack(side= LEFT,expand=True, padx=20, pady=5)

root.resizable(False,False)
root.mainloop()
