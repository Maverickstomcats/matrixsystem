import pymysql
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import tkinter as tk


#connection later
def connection():
    conn=pymysql.connect(
    host='localhost',user='root',password='',db='student_db'
    )
    return conn

def refreshTable():
    for data in mt_tree.get_children():
     mt_tree.delete(data)

    for array in read():
       mt_tree.insert(parent='',index='end',iid=array,text="",values=(array),tag="orow")

root = Tk()
root.title("Student Management System")
root.geometry("1080x720")
mt_tree = ttk.Treeview(root)


def read():
   conn=connection()
   cursor=conn.cursor()
   cursor.execute("SELECT * FROM students")
   result=cursor.fetchall()
   conn.commit()
   conn.close()
   return results


def add():
   studid=str(studidentry.get())
   fname=str(fnameEntry.get())
   lname=str(lnameEntry.get())
   address=(addressEntry())
   phone=str(phoneEntry.get())
   


label=Label(root,text="Student Management System (CRUD MATRIX)", font=('Helvectica',30))
label.grid(row=0,column=0,columnspan=8,rowspan=2,padx=50,pady=50)

studidlabel=Label(root,text="Stud ID",font=('Arial',15))
fnamelabel=Label(root,text="First Name",font=('Arial',15))
lnamelabel=Label(root,text="Last Name",font=('Arial',15))
addresslabel=Label(root,text="Address",font=('Arial',15))
phonelabel=Label(root,text="Phone",font=('Arial',15))


studidlabel.grid(row=3,column=0,columnspan=1,padx=50,pady=5)
fnamelabel.grid(row=4,column=0,columnspan=1,padx=50,pady=5)
lnamelabel.grid(row=5,column=0,columnspan=1,padx=50,pady=5)
addresslabel.grid(row=6,column=0,columnspan=1,padx=50,pady=5)
phonelabel.grid(row=7,column=0,columnspan=1,padx=50,pady=5)


studidEntry=Entry(root,width=55,bd=5,font=('Arial',15))
fnameEntry=Entry(root,width=55,bd=5,font=('Arial',15))
lnameEntry=Entry(root,width=55,bd=5,font=('Arial',15))
addressEntry=Entry(root,width=55,bd=5,font=('Arial',15))
PhoneEntry=Entry(root,width=55,bd=5,font=('Arial',15))


studidEntry.grid(row=3,column=1,columnspan=4,padx=50,pady=5)
fnameEntry.grid(row=4,column=1,columnspan=4,padx=50,pady=5)
lnameEntry.grid(row=5,column=1,columnspan=4,padx=50,pady=5)
addressEntry.grid(row=6,column=1,columnspan=4,padx=50,pady=5)
PhoneEntry.grid(row=7,column=1,columnspan=4,padx=50,pady=5)


addBtn=Button(
    root,text="add",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="#84F894"
)
updateBtn=Button(
    root,text="update",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="#84E8F8"
)
deleteBtn=Button(
    root,text="Delete",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="#FF9999"
)
searchBtn=Button(
    root,text="Search",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="#F4FE82"
)
resetBtn=Button(
    root,text="Reset",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="#F398FF"
)
selectBtn=Button(
    root,text="Select",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="#EEEEEE"
)

addBtn.grid(row=3,column=5,columnspan=1,rowspan=2)
updateBtn.grid(row=5,column=5,columnspan=1,rowspan=2)
deleteBtn.grid(row=7,column=5,columnspan=1,rowspan=2)
searchBtn.grid(row=9,column=5,columnspan=1,rowspan=2)
resetBtn.grid(row=11,column=5,columnspan=1,rowspan=2)
selectBtn.grid(row=13,column=5,columnspan=1,rowspan=2)


style=ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold,15'))
mt_tree['columns']=("Stud ID","First Name","Lastname","Address","Phone")

mt_tree.column("#0",width=0,stretch=NO)
mt_tree.column("Stud ID",anchor=W,width=170)
mt_tree.column("First Name",anchor=W,width=170)
mt_tree.column("Lastname",anchor=W,width=170)
mt_tree.column("Address",anchor=W,width=170)
mt_tree.column("Phone",anchor=W,width=170)

mt_tree.heading("Stud ID",text="Student ID", anchor=W)
mt_tree.heading("First Name",text="First Name", anchor=W)
mt_tree.heading("Lastname",text="LastName", anchor=W)
mt_tree.heading("Address",text="Address", anchor=W)
mt_tree.heading("Phone",text="Phone", anchor=W)




root.mainloop()