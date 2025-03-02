from tkinter import *
from tkinter.messagebox import *
import sqlite3
from datetime import date

tdate=date.today()

con=sqlite3.connect('bus_booking.db')
cur=con.cursor()

root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry("%dx%d+0+0" %(w,h))
root.title("BookMyBus: Seat Booking")

bus=PhotoImage(file="./resource/Bus_for_project.png")
Label(root,image=bus).grid(row=0,column=0,columnspan=12,padx=(w-256)/2)

Title=Label(root,font=('aria',30,'bold'),text="Online Bus Booking System",fg="Red",bd=10,bg="light sky blue")
Title.grid(row=1,column=0,columnspan=12)

details=Label(root,font=('aria',20,'bold'),text="Enter Journey Details",fg="SpringGreen4",bg="PaleGreen")
details.grid(row=2,column=0,columnspan=12,pady=(50,50))

def home_screen():
    root.destroy()
    import home

to=Label(root,font=('aria',15,'bold'),text="To")
to.grid(row=3,column=1,sticky=E)
T1=Entry(root)
T1.grid(row=3,column=2,sticky=W)

fr=Label(root,font=('aria',15,'bold'),text="From")
fr.grid(row=3,column=3,sticky=E)
T2=Entry(root)
T2.grid(row=3,column=4,sticky=W)

dt=Label(root,font=('aria',15,'bold'),text="Journey Date")
dt.grid(row=3,column=5,sticky=E)
T3=Entry(root)
T3.grid(row=3,column=6,sticky=W)

def proceed_book(bid, station, travel_date):
    def confirmed():
        phn_no=mobile.get()
        root.destroy()
        conf=Tk()
        h,w=conf.winfo_screenheight(),conf.winfo_screenwidth()
        conf.geometry("%dx%d+0+0" %(w,h))
        conf.title("Online Bus Booking System: Seat Booking")

        bus=PhotoImage(file="./resource/Bus_for_project.png")
        Label(conf,image=bus).grid(row=0,column=0,columnspan=12,padx=(w-256)/2)

        Title=Label(conf,font=('aria',30,'bold'),text="Online Bus Booking System",fg="Red",bd=10,bg="light sky blue")
        Title.grid(row=1,column=0,columnspan=12)

        try:
            data=cur.execute("SELECT * FROM BOOKING_HISTORY WHERE REF_NO={}".format(phn_no))
            userdata=data.fetchall()
        except:
            showerror("Invalid Input", message="Unacceptable Input.")
        print("out of if")
        if len(userdata)!=0:
            print("inside if", len(userdata))
            for i in range(len(userdata)):
                data=cur.execute("SELECT * FROM BUS WHERE BUSID={}".format(userdata[i][3]))
                busdata=data.fetchall()
                data=cur.execute("SELECT ONAME FROM OPERATOR WHERE OPID={}".format(busdata[0][4]))
                odata=data.fetchall()
                ticket=Frame(conf, borderwidth=5, relief="ridge")
                ticket.grid(row=2, column=0,columnspan=12)
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
                Label(conf, text="Pess Any Key To Continue.", font=("Arial, Bold", 15)).grid(row=3, column=0, columnspan=12)
                showinfo("Success", message="Seat Booked")
                def dummy(temp=0):
                    conf.destroy()
                    import home
                conf.bind("<KeyPress>", dummy)
        conf.mainloop()
    
    def add_details():
        try:
            cur.execute("insert into BOOKING_HISTORY values({}, '{}', '{}', {}, {}, '{}', '{}', {}, '{}')".format(mobile.get(), name.get(), gender_var.get(), bid, seats.get(), tdate, travel_date, age.get(), station))
            cur.execute("update RUNS SET SEAT_AVAIL=SEAT_AVAIL-{} where BUSID={} and DATE='{}'".format(seats.get(), bid, travel_date))
            con.commit()
            confirmed()
        except:
            showerror("Failure", message="Invalid Input")

    def display_fare():
        cur.execute("select SEAT_AVAIL from RUNS where BUSID={} and DATE='{}'".format( bid, travel_date))
        r=cur.fetchall()
        if(int(seats.get())>r[0][0] or int(age.get())>100 or len(mobile.get())!=10):
            if(int(seats.get())>r[0][0]):
                showerror('Error','Seats Not Available')
            if(int(age.get())>100):
                showerror('Error','Age should not be more than 100')
            if(len(mobile.get())!=10):
                showerror('Error','Invalid Mobile Number')
        else:
            f=cur.execute("Select FARE from BUS where BUSID={}".format(bid))
            f=f.fetchall()
            flag=askyesno("Fare Confirm", message="Total Amount to be paid is Rs {}".format(f[0][0]*int(seats.get())))
            if flag:
                add_details()
    
    Label(root,text='Fill Passenger Details to Book the Bus Ticket',font=('aria',15,'bold'),fg='Red',bg='Sky Blue').grid(row=9,columnspan=11,pady=5)
    Label(root,text='Name',font=('aria',15,'bold')).grid(row=11,column=0,sticky=E)
    name=Entry(root)
    name.grid(row=11,column=1,sticky=W)
    Label(root,text='Gender',font=('aria',15,'bold')).grid(row=11,column=2,sticky=E)
    gender_var=StringVar()
    gender_var.set('Male')
    OptionMenu(root,gender_var,'Male','Female').grid(row=11,column=3,sticky=W)
    Label(root,text='No. of Seats',font=('aria',15,'bold')).grid(row=11,column=4,sticky=E)
    seats=Entry(root)
    seats.grid(row=11,column=5,sticky=W)
    Label(root,text='Mobile  No.',font=('aria',15,'bold')).grid(row=11,column=6,sticky=E)
    mobile=Entry(root)
    mobile.grid(row=11,column=7,sticky=W)
    Label(root,text='Age',font=('aria',15,'bold')).grid(row=11,column=8,sticky=E)
    age=Entry(root)
    age.grid(row=11,column=9,sticky=W)
    Button(root,text='Book Seat',font=('aria',15,'bold'),bg='Pale Green',command=display_fare).grid(row=11,column=10,sticky=E)

def show_bus():
    sb=Frame(root)
    sb.grid(row=4, column=0,columnspan=10,pady=20)
    Label(sb,text='Select Bus',font=('aria',15,'bold'),fg='Forest Green').grid(row=2,column=0, pady=40)
    Label(sb,text='Operator',font=('aria',15,'bold'),fg='Forest Green').grid(row=2,column=1, padx=20)
    Label(sb,text='Bus Type',font=('aria',15,'bold'),fg='Forest Green').grid(row=2,column=2, padx=20)
    Label(sb,text='Available/Capacity',font=('aria',15,'bold'),fg='Forest Green').grid(row=2,column=3, padx=20)
    Label(sb,text='Fare',font=('aria',15,'bold'),fg='Forest Green').grid(row=2,column=4, padx=20)

    def transfer():
        if b.get()==0:
            showerror("Select Bus", message="No Bus Selected")
        else:
            proceed_book(b.get(),t1, t3)
            
    t1=T1.get()
    t2=T2.get()
    t3=T3.get()
    data=cur.execute("""
                     select ONAME, TYPE, SEAT_AVAIL, FARE, BUS.BUSID
                     from OPERATOR, BUS, ROUTE AS start, ROUTE AS end, RUNS 
                     WHERE start.SNAME='{}'
                     AND end.SNAME='{}'
                     AND start.SID<end.SID
                     AND start.ROUTEID=end.ROUTEID
                     AND RUNS.DATE='{}'
                     AND BUS.BUSID=RUNS.BUSID
                     AND BUS.OPID=OPERATOR.OPID
                     AND SEAT_AVAIL>0
                     """.format(t1, t2, t3))
    data=data.fetchall()
    b=IntVar()
    i=0
    for i in range(len(data)):
        boption=Radiobutton(sb,text="{}".format("Bus"+str(i+1)), variable=b, value=data[i][4], bg="lightblue" , font=("Arial Bold", 15)).grid(row=i+3,column=0, pady=10)
        Label(sb,text="{}".format(data[i][0]), fg="blue", font=("Arial Bold", 15)).grid(row=i+3,column=1)
        Label(sb,text="{}".format(data[i][1]), fg="blue", font=("Arial Bold", 15)).grid(row=i+3,column=2)
        Label(sb,text="{}".format(data[i][2]), fg="blue", font=("Arial Bold", 15)).grid(row=i+3,column=3)
        Label(sb,text="{}".format(data[i][3]), fg="blue", font=("Arial Bold", 15)).grid(row=i+3,column=4)
    book=Button(sb, text="Proceed to Book",font=('aria',15,'bold'),bg='Pale Green', command=transfer).grid(row=7,column=6,pady=10)


Button(root,font=('aria',10,'bold'),text="Show Bus",bg="PaleGreen",bd=5,command=show_bus).grid(row=3,column=7)

home=PhotoImage(file="./resource/home.png")
Button(root,image=home,bg="PaleGreen",bd=5,command=home_screen).grid(row=3,column=8)
root.mainloop()
