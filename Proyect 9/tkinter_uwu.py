import tkinter

window = tkinter.Tk()
window.title("Hello world")
window.minsize(width=600, height=400)

label = tkinter.Label(text="Hello", font=("Arial", 15, "bold"))
# label.pack()
label.grid(column=0, row=0)
# To change the content of the label
label["text"] = "new text"
label.config(text="Old text")


# Button
# def greet():
#     print("Hello")
#
#
# button = tkinter.Button(text="Click me", command=greet)
# button.pack()
def clicked():
    label["text"] = "I got clicked"


button = tkinter.Button(text="Click me", command=clicked)
# button.pack()
button.grid(column=2, row=2)

# Entry
entry = tkinter.Entry(width=10)
# entry.pack()
entry.grid(column=4, row=4)


# Challenge
def print_in():
    label.config(text=entry.get())


button2 = tkinter.Button(text="Print", command=print_in)
# button2.pack()
button2.grid(column=3, row=1)

tkinter.mainloop()
