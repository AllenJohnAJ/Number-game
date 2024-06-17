from tkinter import *
import sys
import random as r

win = Tk() 
win.geometry("312x324") 
win.resizable(0, 0) 
win.title("High Low : Allen John")


def exitx():
    sys.exit()


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

#hint1
def hint():
    rt=((no-25)//10)*10
    lt=((no+25)//10)*10
    if rt<0:
        result="BETWEEN 0 AND",lt
    elif lt>100:
        result="BETWEEN",rt,"AND 100"
    else:
        result="BETWEEN",rt,"AND",lt

    input_text.set(result)
    expression = ""


    

#hint2

def xyz():
    global expression
    if no%2==0:
        result="EVEN"
    else:
        result="ODD"
    input_text.set(result)
    expression = ""


# 'bt_clear' function :This is used to clear 
# the input field

def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
 
# 'bt_equal':This method calculates the expression 
# present in input field
 
def bt_equal():
    global expression
    if int(expression)>no:
        result="HIGH"
    elif int(expression)<no:
        result="LOW"
    else:
        result="YOU WON"
    input_text.set(result)
    expression = ""
 
expression = ""
no=r.randint(1,100)
 
# 'StringVar()' :It is used to get the instance of input field
 
input_text = StringVar()
 
# Let us creating a frame for the input field
 
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
 
input_frame.pack(side=TOP)
 
#Let us create a input field inside the 'Frame'
 
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field
 
#Let us creating another 'Frame' for the button below the 'input_frame'
 
btns_frame = Frame(win, width=312, height=272.5, bg="grey")
 
btns_frame.pack()
 
# first row
 
clear = Button(btns_frame, text = "clear", fg = "black", width = 43, height = 3, bd = 0, bg = "#E6E6FA", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 4, padx = 0, pady = 0)
 

 
# second row
 
seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#F5F5DC", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#F5F5DC", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#F5F5DC", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
zero = Button(btns_frame, text = "0", fg = "black", width = 10, height = 3, bd = 0, bg = "#F5F5DC", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 1, column = 3, padx = 1, pady = 1)
 
# third row
 
four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#F5F5DC", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#F5F5DC", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#F5F5DC", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
enter = Button(btns_frame, text = "enter", fg = "black", width = 10, height = 3, bd = 0, bg = "#E6E6FA", cursor = "hand2", command = lambda: bt_equal()).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# fourth row
 
one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#F5F5DC", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#F5F5DC", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#F5F5DC", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
exit1 = Button(btns_frame, text = "exit", fg = "black", width = 10, height = 3, bd = 0, bg = "#E6E6FA", cursor = "hand2", command = win.destroy).grid(row = 3, column = 3, padx = 1, pady = 1)
 
# fourth row
 
hint1 = Button(btns_frame, text = "hint1", fg = "black", width = 21, height = 3, bd = 0, bg = "#E6E6FA", cursor = "hand2", command = lambda: hint()).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
hint2= Button(btns_frame, text = "hint2", fg = "black", width = 21, height = 3, bd = 0, bg = "#E6E6FA", cursor = "hand2", command = lambda: xyz()).grid(row = 4, column = 2, columnspan = 2, padx = 1, pady = 1)

win.mainloop()
