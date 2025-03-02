from tkinter import *
from tkinter.messagebox import *
import sqlite3

con=sqlite3.Connection("bus_booking.db")
cur=con.cursor()

root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry("%dx%d+0+0" %(w,h))
root.title("BookMyBus: Seat Booking")

bus=PhotoImage(file="./resource/Bus_for_project.png")
Label(root,image=bus).grid(row=0,column=0,columnspan=10,padx=(w-256)/2)

Title=Label(root,font=('aria',30,'bold'),text="Online Bus Booking System",fg="Red",bd=10,bg="light sky blue")
Title.grid(row=1,column=0,columnspan=10)

Detail=Label(root,text='Add Bus Running Details',font='Arial 20 bold',fg='green')
Detail.grid(row=3,column=0,columnspan=10,padx=w//3,pady=50)

Label(root,text='Bus ID',font='Arial 14 bold').grid(row=7,column=0,sticky=E)
bid=Entry(root)
bid.grid(row=7,column=1,sticky=W)

Label(root,text='Running Date',font='Arial 14 bold').grid(row=7,column=2,sticky=E)
d=Entry(root)
d.grid(row=7,column=3,sticky=W)

Label(root,text='Seat Available',font='Arial 14 bold').grid(row=7,column=4,sticky=E)
s=Entry(root)
s.grid(row=7,column=5,sticky=W)

def add_run():
    try:
        ibid=bid.get()
        irdate=d.get()
        iseat=s.get()
        cur.execute("insert into RUNS values({}, '{}', {})".format(ibid, irdate, iseat))
        Label(new_frame,text="".format(ibid+" "+irdate+" "+iseat)).grid(row=1,column=0, columnspan=11)
        showinfo("Bus Running Details Entry", message="Bus Running Record Added")
        con.commit()
    except:
        showerror("DB insertion Error", message="Bus Record Already Exists")

#edit Bus Details funtion
def edit_run():
    try:
        ibid=bid.get()
        irdate=d.get()
        iseat=s.get()
        cur.execute("update RUNS SEAT_AVAIL={2} where BUSID={0} AND DATE={1}".format(ibid, irdate, iseat))
        Label(new_frame, text="".format(ibid+" "+irdate+" "+iseat)).grid(row=1,column=0, columnspan=11)
        showinfo("Bus Running Entry Updated", message="Bus Running Record updated Successfully")
        con.commit()
    except:
        showerror("Record Not Found", message="Bus Running Record does not Exists")

new_frame=Frame(root)
new_frame.grid(row=8,column=2,columnspan=3)

Button(root,text="Add Run",font='Arial 14 bold',fg='black',bg='Green2',command=add_run).grid(row=7,column=6)
Button(root,text="Edit Run",font='Arial 14 bold',fg='black',bg='Orange',command=edit_run).grid(row=7,column=7)

def home_screen():
    root.destroy()
    import home
    
img1=PhotoImage(file='./resource/home.png')
Button(root,image=img1,bg='Green2',command=home_screen).grid(row=8,column=6,pady=10)
root.mainloop()
