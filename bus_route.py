from tkinter import *
from tkinter.messagebox import *
import sqlite3
con=sqlite3.Connection("bus_booking.db")
cur=con.cursor()

root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry("%dx%d+0+0" %(w,h))
root.title("BookMyBus: Bus Route")

bus=PhotoImage(file="./resource/Bus_for_project.png")
Label(root,image=bus).grid(row=0,column=0,columnspan=10,padx=(w-256)/2)

Title=Label(root,font=('aria',30,'bold'),text="Online Bus Booking System",fg="Red",bd=10,bg="light sky blue")
Title.grid(row=1,column=0,columnspan=10)

details=Label(root,font=('aria',20,'bold'),text="Add Bus Route Details",fg="SpringGreen4",bg="PaleGreen")
details.grid(row=2,column=0,columnspan=10,pady=(50,50))

to=Label(root,font=('aria',15,'bold'),text="Route ID")
to.grid(row=3,column=1,sticky=E)
T1=Entry(root)
T1.grid(row=3,column=2,sticky=W)

fr=Label(root,font=('aria',15,'bold'),text="Station Name")
fr.grid(row=3,column=3,sticky=E)
T2=Entry(root)
T2.grid(row=3,column=4,sticky=W)

dt=Label(root,font=('aria',15,'bold'),text="Station ID")
dt.grid(row=3,column=5,sticky=E)
T3=Entry(root)
T3.grid(row=3,column=6,sticky=W)

def add_rd():
    try:
        irid=T1.get()
        isid=T2.get()
        isname=T3.get()
        cur.execute("insert into ROUTE values({},{},'{}')".format(irid, isid, isname))
        Label(new_frame, text="".format(str(irid)+" "+str(isid)+" "+str(isname))).grid(row=1,column=0, columnspan=11)
        showinfo("Bus Route Details Entry", message="Bus Route Record Added")
        con.commit()
    except:
        showerror("DB insertion Error", message="Bus Route Record Already Exists")

def del_rd():
        irid=T1.get()
        isid=T2.get()
        isname=T3.get()
        try:
            cur.execute("delete from ROUTE where ROUTEID={} and SID=P{} and SNAME='{}'".format(irid, isid, isname))
        except:
            cur.execute("delete from ROUTE where ROUTEID={}".format(irid))
        showinfo("Bus Route Entry deleted", message="Bus Route Record updated Successfully")
        con.commit()

new_frame=Frame(root)
new_frame.grid(row=4,column=2,pady=10,columnspan=7)

Button(root,font=('aria',10,'bold'),text="Add Route",bg="PaleGreen",bd=5,command=add_rd).grid(row=3,column=7)
Button(root,font=('aria',10,'bold'),text="Delete Route",bg="PaleGreen",bd=5,command=del_rd).grid(row=3,column=8)

def home_screen():
    root.destroy()
    import home
    
home=PhotoImage(file="./resource/home.png")
Button(root,image=home,bg="PaleGreen",bd=5,command=home_screen).grid(row=3,column=9)
root.mainloop()
con.commit()
con.close()
