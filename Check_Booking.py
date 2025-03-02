from tkinter import *
from tkinter.messagebox import *
import sqlite3
conn=sqlite3.Connection("bus_booking.db")
cur=conn.cursor()
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry("%dx%d+0+0" %(w,h))
root.title("BookMyBus: Check Booking")

bus=PhotoImage(file="./resource/Bus_for_project.png")
Label(root,image=bus).grid(row=0,column=0,columnspan=10,padx=(w-256)/2)

Title=Label(root,font=('aria',30,'bold'),text="Online Bus Booking System",fg="Red",bd=10,bg="light sky blue")
Title.grid(row=1,column=0,columnspan=10)

details=Label(root,font=('aria',20,'bold'),text="Check Your Booking",fg="SpringGreen4",bg="PaleGreen")
details.grid(row=2,column=0,columnspan=10,pady=(50,50))

Mob=Label(root,font=('aria',15,'bold'),text="Enter Your Mobile No:")
Mob.grid(row=3,column=3)
T1=Entry(root)
T1.grid(row=3,column=4)

def chk_tkt():
    phn_no=T1.get()
    if(len(phn_no)!=10):
                showerror('Error','Invalid Mobile Number')
    else:
        try:
            data=cur.execute("SELECT * FROM BOOKING_HISTORY WHERE REF_NO={}".format(phn_no))
            userdata=data.fetchall()
        except:
            showerror("Invalid Input", message="Unacceptable Input.")
        if len(userdata)!=0:
            for i in range(len(userdata)):
                data=cur.execute("SELECT * FROM BUS WHERE BUSID={}".format(userdata[i][3]))
                busdata=data.fetchall()
                data=cur.execute("SELECT ONAME FROM OPERATOR WHERE OPID={}".format(busdata[0][4]))
                odata=data.fetchall()
                ticket=Frame(root, borderwidth=5, relief="ridge")
                Label(ticket, text="Passengers: {}".format(userdata[i][1]), font=("Arial Bold", 15)).grid(row=0,column=0)
                Label(ticket, text="No of Seats: {}".format(userdata[i][4]), font=("Arial Bold", 15)).grid(row=1,column=0)
                Label(ticket, text="Age: {}".format(userdata[i][7]), font=("Arial Bold", 15)).grid(row=2,column=0)
                Label(ticket, text="Phone: {}".format(userdata[i][0]), font=("Arial Bold", 15)).grid(row=3,column=0)
                Label(ticket, text="Travel On: {}".format(userdata[i][6]), font=("Arial Bold", 15)).grid(row=4,column=0)
                Label(ticket, text="Gender: {}".format(userdata[i][2]), font=("Arial Bold", 15)).grid(row=5,column=0)
                Label(ticket, text="Fare Rs: {} *".format(busdata[0][3]*userdata[i][4]), font=("Arial Bold", 15)).grid(row=1,column=1)
                Label(ticket, text="Bus Details: {}".format(odata[0][0]), font=("Arial Bold", 15)).grid(row=2,column=1)
                Label(ticket, text="Booked On: {}".format(userdata[i][5]), font=("Arial Bold", 15)).grid(row=3,column=1)
                Label(ticket, text="Boarding Point: {}".format(userdata[i][8]), font=("Arial Bold", 15)).grid(row=4,column=1)
                Label(ticket, text="*Total amount Rs {}/- to be paid at the time of Boarding the Bus".format(busdata[0][3]*userdata[i][4]), font=10).grid(row=6,column=0, columnspan=2)
                ticket.grid(row=5,column=0,columnspan=10, pady=10)
        else:
            flag=askyesno("No Booking Record", message="Do you want to book seat now?")
            if flag:
                root.destroy()
                import seat_booking
                
def home_screen():
    root.destroy()
    import home

Button(root,font=('aria',12,'bold'),text="Check Booking",bd=2,command=chk_tkt).grid(row=3,column=5)
home=PhotoImage(file="./resource/home.png")
Button(root,image=home,bg="PaleGreen",bd=5,command=home_screen).grid(row=3,column=6)

root.mainloop()
