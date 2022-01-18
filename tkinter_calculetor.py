from tkinter import *
#creating window
window = Tk()
window.title("Calculator")
window.geometry("600x400")

# creating lable
l1=Label(window,text="First num")
l2=Label(window,text="Secound num")
l3=Label(window,text="Result")

#creating entry field
e1=Entry()
e2=Entry()
e3=Entry()

#arranging
l1.place(x=100,y=50)
l2.place(x=100,y=100)
e1.place(x=200,y=50)
e2.place(x=200,y=100)

#addition function
def add():
  num1=int(e1.get())
  num2=int(e2.get())
  result = num1+num2

  e3.insert(END,str(result))


#substraction function
def sub():
  num1=int(e1.get())
  num2=int(e2.get())
  result = num1-num2

  e3.insert(END,str(result))

#clear function
def clear():
  e1.delete(0,END)
  e2.delete(0,END)
  e3.delete(0,END)

#creating buttons
b1=Button(window,text="+",command = add)
b2=Button(window,text="-",command = sub)
b3=Button(window,text="c",command = clear)

#aranging
b1.place(x=100,y=150)
b2.place(x=200,y=150)
b3.place(x=200,y=250)

l3.place(x=100,y=200)
e3.place(x=200,y=200)

window.mainloop()