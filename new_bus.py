from tkinter import *
from tkinter.messagebox import *
import sqlite3
con=sqlite3.Connection("bus_booking.db")
cur=con.cursor()

root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry("%dx%d+0+0" %(w,h))
root.title("BookMyBus: New Bus")

bus=PhotoImage(file="./resource/Bus_for_project.png")
Label(root,image=bus).grid(row=0,column=0,columnspan=15,padx=(w-256)/2)

Title=Label(root,font=('aria',30,'bold'),text="Online Bus Booking System",fg="Red",bd=10,bg="light sky blue")
Title.grid(row=1,column=0,columnspan=15)

details=Label(root,font=('aria',20,'bold'),text="Add Bus Details",fg="SpringGreen4",bg="PaleGreen")
details.grid(row=2,column=0,columnspan=15,pady=(50,50))

Label(root,font=('aria',15,'bold'),text="Bus ID").grid(row=3,column=1,sticky=E)
T1=Entry(root)
T1.grid(row=3,column=2,sticky=W)

Label(root,font=('aria',15,'bold'),text="Bus Type").grid(row=3,column=3,sticky=E)
a=StringVar()
a.set('Bus Type')
OptionMenu(root,a,'AC 2X2','AC 3X2','Non AC 2X2','Non AC 3X2','AC-Sleeper 2X1','Non-AC Sleeper 2X1').grid(row=3,column=4,sticky=W)

Label(root,font=('aria',15,'bold'),text="Capacity").grid(row=3,column=5,sticky=E)
T2=Entry(root)
T2.grid(row=3,column=6,sticky=W)

Label(root,font=('aria',15,'bold'),text="Fare(in Rs)").grid(row=3,column=7,sticky=E)
T3=Entry(root)
T3.grid(row=3,column=8,sticky=W)

Label(root,font=('aria',15,'bold'),text="Operator ID").grid(row=3,column=9,sticky=E)
T4=Entry(root)
T4.grid(row=3,column=10,sticky=W)

Label(root,font=('aria',15,'bold'),text="Route ID").grid(row=3,column=11,sticky=E)
T5=Entry(root)
T5.grid(row=3,column=12,sticky=W)

def add_bd():
    try:
        ibid=T1.get()
        it=a.get()
        icap=T2.get()
        ifare=T3.get()
        iopid=T4.get()
        irid=T5.get()
        if str(ibid)=="":
            cur.execute("insert into BUS(TYPE, CAPACITY, FARE, OPID, ROUTEID) values('{}',{},{},{},{})".format(it, icap, ifare, iopid, irid))
        else:
            cur.execute("insert into BUS values({}, '{}',{},{},{},{})".format(ibid ,it, icap, ifare, iopid, irid))
        Label(new_frame, text="{}".format((ibid)+" "+str(it)+" "+str(icap)+" "+str(ifare)+" "+str(iopid)+" "+str(irid))).grid(row=1,column=0, columnspan=11)
        showinfo("Bus Details Entry", message="Bus Record Added")
        con.commit() 
    except:
        showerror("DB insertion Error", message="Bus Record Already Exists")
        
def edit_bop():
    try:
        ibid=T1.get()
        it=a.get()
        icap=T2.get()
        ifare=T3.get()
        iopid=T4.get()
        irid=T5.get()
        cur.execute("update bus SET TYPE='{}', CAPACITY={}, FARE={}, OPID={}, ROUTEID={} where BUSID={}".format(it, icap, ifare, iopid, irid, ibid))
        Label(new_frame, text="{}".format(str(ibid)+" "+str(it)+" "+str(icap)+" "+str(ifare)+" "+str(iopid)+" "+str(irid))).grid(row=1,column=0, columnspan=11)
        showinfo("Bus Entry Updated", message="Bus Record updated Successfully")
        con.commit() 
    except:
        showerror("Record Not Found", message="Bus Record does not Exists")
        
new_frame=Frame(root)
new_frame.grid(row=5,column=2,pady=10,columnspan=7)

Button(root,font=('aria',10,'bold'),text="Add Bus",bg="PaleGreen",bd=5,command=add_bd).grid(row=4,column=6,pady=10)
Button(root,font=('aria',10,'bold'),text="Edit Bus",bg="PaleGreen",bd=5,command=edit_bop).grid(row=4,column=7,pady=10)

def home_screen():
    root.destroy()
    import home
    
home=PhotoImage(file="./resource/home.png")
Button(root,image=home,bg="PaleGreen",bd=5,command=home_screen).grid(row=4,column=8,pady=10)
root.mainloop()
