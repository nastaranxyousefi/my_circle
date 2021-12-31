from tkinter import *


def circum():
    PI = 3.14
    result = 2 * PI * float(radius_value.get())
    label1.config(text=f"The Circumference of circle is {result:.3f}.", font=("Helvetica",20 ), fg="red3")


def area():
    PI = 3.14
    result = PI * (float(radius_value.get())) ** 2
    label2.config(text=f"The area of circle is {result:.3f}.", font=("Helvetica",20 ), fg="red3")


root = Tk()
root.title("My circle")
root.minsize(600, 600)
root.maxsize(600, 600)
root.geometry("600x600")
root.resizable(width=False, height=False)
bg = PhotoImage(file = 'math.gif')
my_label = Label(root, image = bg)
my_label.place(x=0, y=0 ,relwidth=1, relheight=1)

Label(root, text="calculate circle",bg="gray7",fg="white", font=("Courier",30 )).pack(pady=30)


Label(root, text="Enter the radius of circle: ",bg="gray7",fg="white", font=("Helvetica",16 )).pack(pady=20)
radius_value = Entry(root, fg="black",bg="lightsteelblue1",font=("Helvetica",16 ), width=12)
radius_value.pack()



button1 = Button(root, text="Calculate circumference", font=("Helvetica",16 ), height=2, width=16, fg='gray5', command=circum)
button1.pack(pady=40)


button2 = Button(root, text="Calculate area",font=("Helvetica",16 ),height=2, width=16, fg='gray5', command=area)
button2.pack()

label1 = Label(root, text="", bg="gray7")
label1.pack(pady=30)

label2 = Label(root, text="", bg="gray7")
label2.pack(pady=10)




root.mainloop()