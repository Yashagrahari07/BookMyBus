from tkinter import *

root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry("%dx%d+0+0" %(w,h))
root.title("BookMyBus: Bus Details")

bus=PhotoImage(file="./resource/Bus_for_project.png")
Label(root,image=bus).grid(row=0,column=0,columnspan=5,padx=(w-256)/2)

Title=Label(root,font=('aria',30,'bold'),text="Online Bus Booking System",fg="Red",bd=10,bg="light sky blue")
Title.grid(row=1,column=0,columnspan=5)

details=Label(root,text='Add New Details to Database',font=('aria',30,'bold'),fg='Green3')
details.grid(row=2,column=0,columnspan=5,pady=20)

def new_op():
    root.destroy()
    import new_operator

B1=Button(bg="SpringGreen2",text="New Operator",font=('aria',20,'bold'),command=new_op)
B1.grid(row=3,column=0,pady=10,padx=(220,0))

def new_bus():
    root.destroy()
    import new_bus

B2=Button(bg='OrangeRed2',text="New Bus",font=('aria',20,'bold'),command=new_bus)
B2.grid(row=3,column=1,pady=10)

def new_route():
    root.destroy()
    import bus_route

B3=Button(bg='Steel Blue',text="New Route",font=('aria',20,'bold'),command=new_route)
B3.grid(row=3,column=2,pady=10)

def new_run():
    root.destroy()
    import new_run

B4=Button(bg='Rosy Brown',text="New Run",font=('aria',20,'bold'),command=new_run)
B4.grid(row=3,column=3,pady=10)


root.mainloop()
