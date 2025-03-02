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
Label(root,image=bus).grid(row=0,column=0,columnspan=15,padx=(w-256)/2)

Title=Label(root,font=('aria',30,'bold'),text="Online Bus Booking System",fg="Red",bd=10,bg="light sky blue")
Title.grid(row=1,column=0,columnspan=15)

Detail=Label(root,text='Add Bus Operator Detail',font='Arial 20 bold',fg='green')
Detail.grid(row=3,column=0,columnspan=15,padx=w//3,pady=50)

def add_bop():
    try:
        iopid=op_id.get()
        iname=name.get()
        iaddress=add.get()
        iphn=ph_no.get()
        imail=email.get()
        cur.execute("insert into OPERATOR values({},'{}','{}','{}',{})".format(iopid,iname,iaddress,imail,iphn))
        Label(new_frame, text="{}".format(str(iopid)+" "+str(iname)+" "+str(iaddress)+" "+str(imail)+" "+str(iphn)),font='Arial 14').grid(row=1,column=0, columnspan=11)
        showinfo("Operator Entry", message="Operator Record Added")
        con.commit()
    except:
        showerror("DB insertion Error", message="Operator Record Already Exists")

#edit Bus Operator function
def edit_bop():
    try:
        iopid=op_id.get()
        iname=name.get()
        iaddress=add.get()
        iphn=ph_no.get()
        imail=email.get()
        cur.execute("update OPERATOR set ONAME='{1}',ADDRESS='{2}',EMAIL='{3}',PHONE={4} where OPID={0}".format(iopid,iname,iaddress,imail,iphn))       
        Label(new_frame, text="{}".format(str(iopid)+" "+str(iname)+" "+str(iaddress)+" "+str(imail)+" "+str(iphn)),font='Arial 14').grid(row=1,column=0, columnspan=11)
        showinfo("Operator Entry Updated", message="Operator Record updated Successfully")
        con.commit()
    except:
        showerror("Record Not Found", message="Operator Record does not Exists")

Button(root,text="ADD",font='Arial 14 bold',fg='black',bg='Green2',command=add_bop).grid(row=7,column=10)
Button(root,text="EDIT",font='Arial 14 bold',fg='black',bg='Orange',command=edit_bop).grid(row=7,column=11)

def home_screen():
    root.destroy()
    import home

Label(root,text='Operator Id',font='Arial 12 bold').grid(row=7,column=0,sticky=E)
op_id=Entry(root)
op_id.grid(row=7,column=1,sticky=W)

Label(root,text='Name',font='Arial 12 bold').grid(row=7,column=2,sticky=E)
name=Entry(root)
name.grid(row=7,column=3,sticky=W)

Label(root,text='Address',font='Arial 12 bold').grid(row=7,column=4,sticky=E)
add=Entry(root)
add.grid(row=7,column=5,sticky=W)

Label(root,text='Phone No.',font='Arial 12 bold').grid(row=7,column=6,sticky=E)
ph_no=Entry(root)
ph_no.grid(row=7,column=7,sticky=W)

Label(root,text='Email',font='Arial 12 bold').grid(row=7,column=8,sticky=E)
email=Entry(root)
email.grid(row=7,column=9,sticky=W)

new_frame=Frame(root)
new_frame.grid(row=8,column=1,pady=10,columnspan=7)

img1=PhotoImage(file='./resource/home.png')
Button(root,image=img1,bg='Green2',command=home_screen).grid(row=8,column=10,pady=10)
root.mainloop()
