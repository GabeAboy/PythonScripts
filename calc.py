import Tkinter as tk
from Tkinter import Grid
class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.calcscreen = ''
 
        self.calculator = tk.Button(bd=5,text=self.calcscreen,width=20)
        self.calculator.grid(row=0,column=2)
 
        self.label = tk.Label(text="Calculator by PixelHD").grid(row=1,column=1)
 
        self.num1 = tk.Button(bd=5,text="1",command=self.add1)
        self.num1.grid(row=2,column=0)
        self.num2 = tk.Button(bd=5,text="2",command=self.add2).grid(row=2,column=1)
        self.num3 = tk.Button(bd=5,text="3",command=self.add3).grid(row=2,column=2)
        self.num4 = tk.Button(bd=5,text="4",command=self.add4).grid(row=3,column=0)
        self.num5 = tk.Button(bd=5,text="5",command=self.add5).grid(row=3,column=1)
        self.num6 = tk.Button(bd=5,text="6",command=self.add6).grid(row=3,column=2)
        self.num7 = tk.Button(bd=5,text="7",command=self.add7).grid(row=4,column=0)
        self.num8 = tk.Button(bd=5,text="8",command=self.add8).grid(row=4,column=1)
        self.num9 = tk.Button(bd=5,text="9",command=self.add9).grid(row=4,column=2)
        self.num0 = tk.Button(bd=5,text="0",command=self.add0).grid(row=5,column=1)
        self.plus = tk.Button(bd=5,text="+",command=self.add).grid(row=2,column=3)
        self.minus = tk.Button(bd=5,text="-",command=self.subtract).grid(row=3,column=3)
        self.equal = tk.Button(bd=5,text="=",command=self.finishcalc).grid(row=4,column=3)
        self.divide = tk.Button(bd=5,text="/",command=self.division).grid(row=4,column=0)
        self.multiply = tk.Button(bd=5,text="*",command=self.multiplication).grid(row=4,column=2)
 
        self.clear = tk.Button(bd=5,text="AC",command=self.clearcalc).grid(row=5,column=3)
 
        self.root.mainloop()
    def add1(self):
        self.calcscreen += "1"
        self.calculator.configure(text=self.calcscreen)
    def add2(self):
        self.calcscreen += "2"
        self.calculator.configure(text=self.calcscreen)
    def add3(self):
        self.calcscreen += "3"
        self.calculator.configure(text=self.calcscreen)
    def add4(self):
        self.calcscreen += "4"
        self.calculator.configure(text=self.calcscreen)
    def add5(self):
        self.calcscreen += "5"
        self.calculator.configure(text=self.calcscreen)
    def add6(self):
        self.calcscreen += "6"
        self.calculator.configure(text=self.calcscreen)
    def add7(self):
        self.calcscreen += "7"
        self.calculator.configure(text=self.calcscreen)
    def add8(self):
        self.calcscreen += "8"
        self.calculator.configure(text=self.calcscreen)
    def add9(self):
        self.calcscreen += "9"
        self.calculator.configure(text=self.calcscreen)
    def add0(self):
        self.calcscreen += "0"
        self.calculator.configure(text=self.calcscreen)
    def clearcalc(self):
        self.calcscreen = ""
        self.calculator.configure(text=self.calcscreen)
    def  add(self):
        self.calcscreen += " + "
        self.calculator.configure(text=self.calcscreen)
    def subtract(self):
        self.calcscreen += " - "
        self.calculator.configure(text=self.calcscreen)
    def finishcalc(self):
        if self.calcscreen == "":
            self.calcscreen = "0 + 0"
        self.result = eval(self.calcscreen)
        self.calculator.configure(text=self.result)
        self.calcscreen = ""
    def multiplication(self):
        self.calcscreen += " * "
        self.calculator.configure(text=self.calcscreen)
    def division(self):
        self.calcscreen += " / "
        self.calculator.configure(text=self.calcscreen)
       
 
app = Calculator()
