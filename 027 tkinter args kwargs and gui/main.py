# import tkinter

# window = tkinter.Tk()
# window.title("My first GUI Program")
# window.minsize(width=500, height=300)

# my_label = tkinter.Label(text="I am a Label", padx=10, font=("Poppins", 18))
# my_label.pack(side="left")

# window.mainloop()


########################################################### UNLIMITED ARGS

# def add(*args):
#     output = 0
#     for n in args:
#         output += n
#     print(output)

# add(120, 10, 50, 20)


########################################################### UNLIMITED KEYWORD ARGUMENTS

# def calculate(**kwargs):
#     if "add" in kwargs:
#         print(f"add {kwargs['add']}")

# calculate(add=3, multiply=3)


########################################################### TKINTER

# import tkinter

# window = tkinter.Tk()
# window.minsize(width=500, height=500)

# first_label = tkinter.Label(text="This is a label", font=("Poppins", 16))
# first_label.grid(column=0, row=0)

# counter = 0
# def button_clicked():
#     global counter
#     counter += 1
#     first_label["text"] = input.get()

# input = tkinter.Entry(width=50)
# input.grid(column=0, row=1)

# button = tkinter.Button(text="Click me", padx=10, pady=5, command=button_clicked)
# button.grid(column=1, row=1)

# window.mainloop() 


########################################################### MILES TO KILOMETER

import tkinter

window = tkinter.Tk()

def convert():
    km_input["text"] = round(int(miles_input.get()) * 1.6, 2)

miles_input = tkinter.Entry()
miles_input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

before_km = tkinter.Label(text="is equal to")
before_km.grid(column=0, row=1)

km_input = tkinter.Label(text="")
km_input.grid(column=1, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

calc_button = tkinter.Button(text="Calculate", command=convert)
calc_button.grid(column=1, row=2)

window

window.mainloop()