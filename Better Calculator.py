from tkinter import *


root = Tk()
root.title("Simple Calculator")

textBox = Entry(root, width=35, borderwidth=20, bg="black", font="Montserrat 15 bold", fg="white")
textBox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    if textBox.get() == "Undefined":
        textBox.delete(0, END)
    current = textBox.get()
    textBox.delete(0, END)
    fin_num = str(current) + str(number)
    textBox.insert(0, fin_num)


def button_clear():
    textBox.delete(0, END)


def equal_button():
    second_number = textBox.get()
    textBox.delete(0, END)
    try:
        if math == "addition":
            textBox.insert(0, f_num + int(second_number))
            file_text = (str(f_num) + " + " + str(second_number) + " = " + str(f_num + int(second_number)) + "\n")
            with open('CalcHistory.txt', 'a') as hist:
                hist.write(file_text)
                hist.close()
        elif math == "subtraction":
            textBox.insert(0, f_num - int(second_number))
            file_text = (str(f_num) + " - " + str(second_number) + " = " + str(f_num - int(second_number)) + "\n")
            with open('CalcHistory.txt', 'a') as hist:
                hist.write(file_text)
                hist.close()
        elif math == "multiplication":
            textBox.insert(0, f_num * int(second_number))
            file_text = (str(f_num) + " * " + str(second_number) + " = " + str(f_num * int(second_number)) + "\n")
            with open('CalcHistory.txt', 'a') as hist:
                hist.write(file_text)
                hist.close()
        elif math == "division":
            if second_number == 0:
                textBox.insert(0, "Undefined")
            textBox.insert(0, f_num / int(second_number))
            file_text = (str(f_num) + " / " + str(second_number) + " = " + str(f_num / int(second_number)) + "\n")
            with open('CalcHistory.txt', 'a') as hist:
                hist.write(file_text)
                hist.close()
    except ZeroDivisionError:
        textBox.insert(0, "Undefined")


def button_add():
    first_number = textBox.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    textBox.delete(0, END)


def button_subtract():
    first_number = textBox.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    textBox.delete(0, END)


def button_multiply():
    first_number = textBox.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    textBox.delete(0, END)


def button_divide():
    first_number = textBox.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    textBox.delete(0, END)


button_1 = Button(root, text="1", padx=60, pady=20, command=lambda: button_click(1), bg="light blue",
                  font="Montserrat 15 bold")
button_2 = Button(root, text="2", padx=60, pady=20, command=lambda: button_click(2), bg="light blue",
                  font="Montserrat 15 bold")
button_3 = Button(root, text="3", padx=60, pady=20, command=lambda: button_click(3), bg="light blue",
                  font="Montserrat 15 bold")
button_4 = Button(root, text="4", padx=60, pady=20, command=lambda: button_click(4), bg="light blue",
                  font="Montserrat 15 bold")
button_5 = Button(root, text="5", padx=60, pady=20, command=lambda: button_click(5), bg="light blue",
                  font="Montserrat 15 bold")
button_6 = Button(root, text="6", padx=60, pady=20, command=lambda: button_click(6), bg="light blue",
                  font="Montserrat 15 bold")
button_7 = Button(root, text="7", padx=60, pady=20, command=lambda: button_click(7), bg="light blue",
                  font="Montserrat 15 bold")
button_8 = Button(root, text="8", padx=60, pady=20, command=lambda: button_click(8), bg="light blue",
                  font="Montserrat 15 bold")
button_9 = Button(root, text="9", padx=60, pady=20, command=lambda: button_click(9), bg="light blue",
                  font="Montserrat 15 bold")
button_0 = Button(root, text="0", padx=60, pady=20, command=lambda: button_click(0), bg="light blue",
                  font="Montserrat 15 bold")
button_clear = Button(root, text="Clear", padx=116, pady=20, command=button_clear, bg="light blue",
                      font="Montserrat 15 bold")
button_add = Button(root, text="+", padx=60, pady=20, command=button_add, bg="light blue", font="Montserrat 15 bold")
button_equal = Button(root, text="=", padx=134, pady=20, command=equal_button, bg="light blue",
                      font="Montserrat 15 bold")
button_sub = Button(root, text="-", padx=63, pady=20, command=button_subtract, bg="light blue",
                    font="Montserrat 15 bold")
button_mult = Button(root, text="x", padx=59, pady=20, command=button_multiply, bg="light blue",
                     font="Montserrat 15 bold")
button_div = Button(root, text="/", padx=63, pady=20, command=button_divide, bg="light blue", font="Montserrat 15 bold")


button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0, columnspan=1)
button_5.grid(row=2, column=1, columnspan=1)
button_6.grid(row=2, column=2, columnspan=1)

button_7.grid(row=3, column=0, columnspan=1)
button_8.grid(row=3, column=1, columnspan=1)
button_9.grid(row=3, column=2, columnspan=1)

button_0.grid(row=4, column=0, columnspan=1)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0, columnspan=1)
button_equal.grid(row=5, column=1, columnspan=2)

button_sub.grid(row=6, column=0, columnspan=1)
button_mult.grid(row=6, column=1, columnspan=1)
button_div.grid(row=6, column=2, columnspan=1)


root.mainloop()
