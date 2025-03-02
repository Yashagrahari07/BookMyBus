from tkinter import *

root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry("%dx%d+0+0" %(w,h))
root.title("BookMyBus: Home")

bus=PhotoImage(file="./resource/Bus_for_project.png")
Label(root,image=bus).grid(row=0,column=0,columnspan=5,padx=(w-256)/2)

Title=Label(root,font=('aria',30,'bold'),text="Online Bus Booking System",fg="Red",bd=10,bg="light sky blue")
Title.grid(row=1,column=0,columnspan=5)

def seat_book():
    root.destroy()
    import seat_booking

B1=Button(bg="SpringGreen2",text="Seat Booking",font=('aria',20,'bold'),command=seat_book)
B1.grid(row=2,column=0,pady=(100,0),padx=(220,0))

def check_seat():
    root.destroy()
    import Check_Booking

B2=Button(bg="SpringGreen2",text="Check Booked Seat",font=('aria',20,'bold'),command=check_seat)
B2.grid(row=2,column=1,pady=(100,0))

def add_bus():
    root.destroy()
    import bus_details

B3=Button(bg="SpringGreen2",text="Add Bus Details",font=('aria',20,'bold'),command=add_bus)
B3.grid(row=2,column=2,pady=(100,0))

Rem=Label(root,font=('aria',15,'bold'),text="For Admins Only",fg="Red",bd=10)
Rem.grid(row=3,column=2,pady=20)

root.mainloop()
