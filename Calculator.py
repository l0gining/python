from tkinter import *

def entryprint(str):
    entry.insert(END, str)

def enclear():
    entry.delete(0, END)

def calculate():
    x = eval(entry.get())
    calc_string.set(x)

window = Tk()
window.title("Калькулятор")
window.geometry('500x400+500+200')
window.resizable(False, False)

frame = Frame(window, borderwidth=1, relief=GROOVE)
frame.grid()

calc_string = StringVar()
calc_string.set('')

entry = Entry(frame, text='0', font=('Verdana', 13), state=NORMAL, justify=RIGHT)
entry.grid()

labelout = Label(frame, text='0', font=('Verdana', 13), textvariable=calc_string)
labelout.grid()

frame1 = Frame(frame, borderwidth=1, relief=GROOVE)
frame1.grid()

buttons = [['7', '8', '9', '+', 'C',],
           ['4', '5', '6', '-', '%',],
           ['1', '2', '3', '*', '**'],
           ['0', '/', '=']]

c = 0
r = 1
for i in buttons:
    for j in i:
        if j == 'C':
            cmnd = lambda j=j: enclear()
        elif j == '=':
            cmnd = lambda j=j: calculate()
        else:
            cmnd = lambda j=j: entryprint(j)
        x = Button(frame1, text=j, height=3, width=6, command=cmnd)
        x.grid(column=c, row=r)
        c += 1
    c = 0
    r += 1

window.mainloop()
