from tkinter import *

window=Tk()
window.title("calculator")
window.configure(background="#d1f2eb")
first_number = None
total = 0
current_operation = None




Button_default_property={  #defining default property for the buttons
    "height":2,
    "width":3,
    "bg":"pink",
    "font":("Arial", 13,"bold")



}



def button_click(digit):
    current = input_value.get()
    new_value = current + digit
    input_value.set(new_value)



def button_clearall():
    global total, first_number, current_operation

    input_value.set("")
    total=0
    first_number=None
    current_operation = None

def button_adds():
    global total, first_number, current_operation

    try:
        current_number = float(input_value.get())
        if first_number is None:  # If first number is not set
            first_number = current_number
        else:  # Perform ongoing addition
            first_number += current_number  # Accumulate sum
        input_value.set("")  # Clear input field for next number
        current_operation = "+"  # Set operation mode
    except ValueError:
        input_value.set("Error")



def button_subzz():
    global total,first_number,current_operation

    try:
        current_number = float(input_value.get())
        if first_number is None:
            first_number=current_number
        else:
            first_number-=current_number
        input_value.set("")
        current_operation = "-"
    except ValueError:
        input_value.set("Error")


def button_divisionnnn():
    global total,first_number,current_operation
    try:
        current_number = float(input_value.get())
        if first_number is None:
            first_number=current_number
        else:
            first_number/=current_number
        input_value.set("")
        current_operation = "/"
    except ValueError:
        input_value.set("Error")

def button_multipicatiobn():
    global total, first_number, current_operation
    try:
        current_number = float(input_value.get())
        if first_number is None:
            first_number = current_number
        else:
            first_number *= current_number

        input_value.set("")
        current_operation = "*"

    except ValueError:
        input_value.set("Error")



def equals_operation():
    global total, first_number, current_operation

    try:
        if current_operation == "+" and first_number is not None:
            second_number = float(input_value.get())
            total = first_number + second_number
            input_value.set(str(total))
            first_number = None  # Reset first number to allow new calculations
            current_operation = None  # Reset operation

        if current_operation == "-" and first_number is not None:
            second_number = float(input_value.get())
            total=first_number - second_number
            input_value.set(str(total))
            first_number=None
            current_operation = None

        if current_operation == "/" and first_number is not  None:
            second_number = float(input_value.get())
            total=first_number/second_number
            input_value.set(str(total))
            first_number=None
            current_operation=None

        if current_operation == "*" and first_number is not None:
            second_number = float(input_value.get())
            total=first_number*second_number
            input_value.set(str(total))
            first_number=None
            current_operation=None


    except ValueError:
        input_value.set("Error")
    except ZeroDivisionError:
        input_value.set("ZeroDivisionError")














def on_enter(event):#function to give hover colour for buttons
    event.widget.config(bg="lightblue")  # Change background color when mouse enters

def on_leave(event): #function to give hover colour for buttons
    event.widget.config(bg="pink") #change the background colour when the mouse leaves


input_value = StringVar()#initialize the value to store the variables
input_value.set("")#at start begin  the input field as empty


display = Entry(
    window,
    textvariable=input_value,
    font=("Arial", 16),
    justify="right",


)

display.grid(row=0, column=0, columnspan=4, padx=6, pady=6,ipady=10)


button_1 = Button(#defining 1 button
    window,
    **Button_default_property,  # Apply all default properties
    text="1",
    command=lambda : button_click("1")



)

button_2 = Button(#defining 2 button
    window,
    **Button_default_property,
    text="2",
    command=lambda: button_click("2")
)

button_3 = Button(#defining 3 button
    window,
    **Button_default_property,
    text="3",
    command=lambda: button_click("3")

)

button_4 = Button(#defining 4 button
    window,
    **Button_default_property,
    text="4",
    command=lambda: button_click("4")
)
button_5 = Button(#defining 5 button
    window,
    **Button_default_property,
    text="5",
    command=lambda: button_click("5")
)
button_6 = Button(#defining 6 button
    window,
    **Button_default_property,
    text="6",
    command=lambda: button_click("6")
)
button_7 = Button(#defining 7 button
    window,
    **Button_default_property,
    text="7",
    command=lambda: button_click("7")
)
button_8 = Button(#defining 8 button
    window,
    **Button_default_property,
    text="8",
    command=lambda: button_click("8")

)
button_9 = Button(#defining 9 button
    window,
    **Button_default_property,
    text="9",
    command=lambda: button_click("9")
)
button_0 = Button(#defining 0 button
    window,
    **Button_default_property,
    text="0",
    command=lambda: button_click("0")
)

button_plus =Button(
    window,
    **Button_default_property,
    text="+",
    command=lambda :button_adds()

)

button_minus = Button(
    window,
    **Button_default_property,
    text="-",
    command=lambda :button_subzz()

)

button_multiplication = Button(
    window,
    **Button_default_property,
    text="x",
    command=lambda :button_multipicatiobn()
)
button_division = Button(
    window,
    **Button_default_property,
    text="/",
    command=lambda :button_divisionnnn()
)
button_equals = Button(
    window,
    text="=",
    height=2,
    width=3,
    bg="pink",
    font=("Arial",13,"bold"),
    command=lambda :equals_operation()
)
button_clear = Button(
    window,
    **Button_default_property,
    text="clear",
    command=lambda: button_clearall()
)

def Button_padding(btn,row,col):
    btn.grid(row=row, column=col, padx=6, pady=6)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)


Button_padding(button_1,1,0)
Button_padding(button_2 ,1,1)
Button_padding(button_3,1,2)
Button_padding(button_4,2,0)
Button_padding(button_5,2,1)
Button_padding(button_6,2,2)
Button_padding(button_7,3,0)
Button_padding(button_8,3,1)
Button_padding(button_9,3,2)
Button_padding(button_0,4,1)
Button_padding(button_plus,4,0)
Button_padding(button_minus,4,2)
Button_padding(button_multiplication,1,3)
Button_padding(button_division,2,3)
button_equals.grid(row=3, column=3, rowspan=2, sticky="ns", padx=6, pady=6)
button_clear.grid(row=5, column=0, columnspan=4, sticky="we", padx=6, pady=6)







window.mainloop()