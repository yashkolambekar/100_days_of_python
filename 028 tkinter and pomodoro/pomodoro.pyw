import tkinter
import time as timee
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- OTHER MECHANICS ------------------------------- # 

# w b w b w b w lb w  b  w  b w  b  w  lb
# 1 2 3 4 5 6 7 8  9 10 11 12 13 14 15 16

session_number = 1
is_running = True

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global is_running
    is_running = False
    top_label["text"] = "Work"
    canvas.itemconfig(timer_text, text="25:00")





# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global is_running
    is_running = True
    global session_number
    if session_number % 8 == 0:
        countdown_start(900)
        top_label["text"] = "Long Break"
    elif session_number % 2 == 1:
        countdown_start(1500)
        top_label["text"] = "Work"
    elif session_number % 2 == 0:
        top_label["text"] = "Break"
        countdown_start(300)
    session_number += 1

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return (hour, minutes, seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown_start(count):
    global is_running
    if is_running:
        if count >= 0:
            window.after(1000, countdown_start, count - 1)
            hms = convert(count)
            hms_string = f"{str(hms[1]).zfill(2)}:{str(hms[2]).zfill(2)}"
            canvas.itemconfig(timer_text, text=hms_string)
    else:
        global session_number
        session_number = 1


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk();
window.title("Pomodoro");
window.config(padx=100, pady=50,bg=YELLOW)
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image_file = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image_file)
timer_text = canvas.create_text(100, 135, text="OO:OO", font=("Poppins", 30, "bold"), fill="white")
canvas.grid(column=1, row=1)
top_label = tkinter.Label(text="Timer", font=("Poppins", 36, "bold"), bg=YELLOW, fg=RED, pady=10)
top_label.grid(column=1, row=0)
checkmarks = tkinter.Label(text="", font=("Poppins", 5), bg=YELLOW, fg=RED, pady=20, justify="center")
checkmarks.grid(column=1, row=2)
start_btn = tkinter.Button(text="Start", font=("Poppins", 15, "bold"), padx=20, bg=PINK, fg=YELLOW, border=0, command=start_timer)
start_btn.grid(column=0, row=3)
reset_btn = tkinter.Button(text="Reset", font=("Poppins", 15, "bold"), padx=20, bg=PINK, fg=YELLOW, border=0, command=reset)
reset_btn.grid(column=2, row=3)
window.resizable(False, False)


window.mainloop()