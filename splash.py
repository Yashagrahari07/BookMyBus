from tkinter import *


root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry("%dx%d+0+0" %(w,h))
root.title("BookMyBus: Online Bus Booking System")
bus=PhotoImage(file="./resource/Bus_for_project.png")
Label(root,image=bus).grid(row=0,column=0,columnspan=5,padx=(w-256)/2)

Title=Label(root,font=('aria',30,'bold'),text="Online Bus Booking System",fg="Red",bd=10,bg="light sky blue")
Title.grid(row=1,column=0,columnspan=5)

Name=Label(root,font=('aria',20,'bold'),text="Name: Yash Agrahari",fg="blue2",bd=10)
Name.grid(row=2,column=0,columnspan=5,pady=(100,0))

ER=Label(root,font=('aria',20,'bold'),text="Er: 211B353",fg="blue2",bd=10)
ER.grid(row=3,column=0,columnspan=5,pady=(20,0))

Mobile=Label(root,font=('aria',20,'bold'),text="Mobile: 7457929239",fg="blue2",bd=10)
Mobile.grid(row=4,column=0,columnspan=5,pady=(20,0))

Submit=Label(root,font=('aria',25,'bold'),text="Submitted To: Dr. Mahesh Kumar",fg="Red",bd=10,bg="light sky blue")
Submit.grid(row=5,column=0,columnspan=5,pady=(100,0))

Project=Label(root,font=('aria',20,'bold'),text="Project Based Learning",fg="Red",bd=10)
Project.grid(row=6,column=0,columnspan=5,pady=(0,0))

def key_press(a=1):
    root.destroy()
    import home
    
root.bind('<Motion>', key_press)
root.bind('<KeyPress>', key_press)

root.mainloop()

