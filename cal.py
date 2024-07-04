import tkinter
from tkinter import *
window=Tk()
window.geometry("570x600+100+200")
window.title("simple caculater")
window.resizable(False,False)
window.configure(bg="#8D6F64")
input = " "
def show(value):
    global input
    input += value
    result.config(text=input)
def clear():
    global input
    input = " "
    result.config(text=input)
def calculate():
    global input
    res=""
    if input !="":
        try:
            res=eval(input)
        except:
             res="error"
             input=""
    result.config(text=res)        
result=Label(window,font=("Arial",30),width=25,height=2,text="")
result.pack()



Button(window,text="c",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="indigo",bg="#060270", command=lambda: clear()).place(x=10,y=100)
Button(window,text="/",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2A2B36", command=lambda: show("/")).place(x=150,y=100)
Button(window,text="%",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2A2B36", command=lambda: show("%")).place(x=290,y=100)
Button(window,text="",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2A2B36", command=lambda: show("")).place(x=430,y=100)

Button(window,text="7",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2A2B36", command=lambda: show("7")).place(x=10,y=200)
Button(window,text="8",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2A2B36", command=lambda: show("8")).place(x=150,y=200)
Button(window,text="9",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2A2B36", command=lambda: show("9")).place(x=290,y=200)
Button(window,text="-",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2A2B36", command=lambda: show("-")).place(x=430,y=200)

Button(window,text="4",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2A2B36", command=lambda: show("4")).place(x=10,y=300)
Button(window,text="5",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2A2B36", command=lambda: show("5")).place(x=150,y=300)
Button(window,text="6",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2A2B36", command=lambda: show("6")).place(x=290,y=300)
Button(window,text="+",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2A2B36", command=lambda: show("+")).place(x=430,y=300)

Button(window,text="1",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2A2B36", command=lambda: show("1")).place(x=10,y=400)
Button(window,text="2",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2A2B36", command=lambda: show("2")).place(x=150,y=400)
Button(window,text="3",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2A2B36", command=lambda: show("3")).place(x=290,y=400)
Button(window,text="0",width=11,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2A2B36", command=lambda: show("0")).place(x=10,y=500)

Button(window,text=".",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#2A2B36", command=lambda: show(".")).place(x=290,y=500)
Button(window,text="=",width=5,height=3,font=("arial",30,"bold"),bd=1,fg="white",bg="#2A2B36", command=lambda: calculate()).place(x=430,y=400)






window.mainloop()