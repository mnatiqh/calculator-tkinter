from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("409x442")

equation = StringVar()

equation.set("")



def updateEquation(event):
    '''
    evnet -> which button was clicked , what was written on the button. was that double click or single , left or right
    '''

    value = event.widget.cget("text")

    if value == "CLR" : 
        equation.set("")

    elif value == "=":
        equation.set(eval(equation.get()))

    elif value == "DEL":
        equation.set(equation.get()[0:-1])
    
    else:   
        equation.set( equation.get() + value )


    pass

entry = Entry(root , textvariable=equation , font=("arial" , 27))
entry.grid(row=2 , column=2 , columnspan=5)

numberButton1 = Button(root , text="1" , font=("arial" , 30) , width=4)
numberButton1.grid(row=6 , column=2)
numberButton1.bind("<Button-1>" , updateEquation)

numberButton2 = Button(root , text="2" , font=("arial" , 30) , width=4)
numberButton2.grid(row=6 , column=3)
numberButton2.bind("<Button-1>" , updateEquation)

numberButton3 = Button(root , text="3" , font=("arial" , 30) , width=4)
numberButton3.grid(row=6 , column=4)
numberButton3.bind("<Button-1>" , updateEquation)

numberButton4 = Button(root , text="4" , font=("arial" , 30) , width=4)
numberButton4.grid(row=5 , column=2)
numberButton4.bind("<Button-1>" , updateEquation)

numberButton5 = Button(root , text="5" , font=("arial" , 30) , width=4)
numberButton5.grid(row=5 , column=3)
numberButton5.bind("<Button-1>" , updateEquation)

numberButton6 = Button(root , text="6" , font=("arial" , 30) , width=4)
numberButton6.grid(row=5 , column=4)
numberButton6.bind("<Button-1>" , updateEquation)

numberButton7 = Button(root , text="7" , font=("arial" , 30) , width=4)
numberButton7.grid(row=4 , column=2)
numberButton7.bind("<Button-1>" , updateEquation)

numberButton8 = Button(root , text="8" , font=("arial" , 30) , width=4)
numberButton8.grid(row=4 , column=3)
numberButton8.bind("<Button-1>" , updateEquation)

numberButton9 = Button(root , text="9" , font=("arial" , 30) , width=4)
numberButton9.grid(row=4 , column=4)
numberButton9.bind("<Button-1>" , updateEquation)

numberButton0 = Button(root , text="0" , font=("arial" , 30) , width=4)
numberButton0.grid(row=7 , column=3)
numberButton0.bind("<Button-1>" , updateEquation)

decimalButton = Button(root , text="." , font=("arial" , 30) , width=4)
decimalButton.grid(row=7 , column=4)
decimalButton.bind("<Button-1>" , updateEquation)

percentageButton = Button(root , text="%" , font=("arial" , 30) , width=4)
percentageButton.grid(row=3 , column=2)
percentageButton.bind("<Button-1>" , updateEquation)

equalButton = Button(root , text="=" , font=("arial" , 30) , width=4)
equalButton.grid(row=7 , column=5)
equalButton.bind("<Button-1>" , updateEquation)


additionButton = Button(root , text="+" , font=("arial" , 30) , width=4)
additionButton.grid(row=6 , column=5)
additionButton.bind("<Button-1>" , updateEquation)

minusButton = Button(root , text="-" , font=("arial" , 30) , width=4)
minusButton.grid(row=5 , column=5)
minusButton.bind("<Button-1>" , updateEquation)

multiplyButton = Button(root , text="*" , font=("arial" , 30) , width=4)
multiplyButton.grid(row=4 , column=5)
multiplyButton.bind("<Button-1>" , updateEquation)

divisionButton = Button(root , text="/" , font=("arial" , 30) , width=4)
divisionButton.grid(row=3 , column=5)
divisionButton.bind("<Button-1>" , updateEquation)

clearButton = Button(root , text="CLR" , font=("arial" , 30) , width=4)
clearButton.grid(row=3 , column=4)
clearButton.bind("<Button-1>" , updateEquation)

deleteButton = Button(root , text="DEL" , font=("arial" , 30) , width=4)
deleteButton.grid(row=3 , column=3)
deleteButton.bind("<Button-1>" , updateEquation)

doubleZeroButton = Button(root , text="00" , font=("arial" , 30) , width=4)
doubleZeroButton.grid(row=7 , column=2)
doubleZeroButton.bind("<Button-1>" , updateEquation)

root.mainloop()