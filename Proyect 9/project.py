import tkinter

window = tkinter.Tk()
window.title("Inches to centimeters")
window.minsize(width=300, height=300)


def conversion():
    print(variable.get())
    option = variable.get()
    if option == 1:
        inch_to_cm()
    elif option == 2:
        cm_to_inch()


variable = tkinter.IntVar()
option1 = tkinter.Radiobutton(text="Inches", variable=variable, value=1)
option1.place(x=20, y=83)
option2 = tkinter.Radiobutton(text="Cm", variable=variable, value=2)
option2.place(x=20, y=120)

label = tkinter.Label(text="Welcome to the inches/centimeters converter uwu")
label.pack(pady=10)


def inch_to_cm():
    inch = float(entry1.get())
    inch_result.config(text="The result is: {} cm".format(inch * 2.54))


def cm_to_inch():
    cm = float(entry1.get())
    cm_result.config(text="The result is: {} inches".format(cm / 2.54))


entry1 = tkinter.Entry(width=30)
entry1.insert(index=tkinter.END, string="Write the inches here: ")
entry1.pack()

button = tkinter.Button(text="Convert", command=conversion)
button.pack()

inch_result = tkinter.Label(text="0")
inch_result.pack(pady=10)

# entry2 = tkinter.Entry(width=30)
# entry2.insert(index=tkinter.END, string="Write the cm here: ")
# entry2.pack()
cm_result = tkinter.Label(text="0")
cm_result.pack(pady=10)
# button2 = tkinter.Button(text="Convert", command=cm_to_inch)
# button2.pack()
window.mainloop()
