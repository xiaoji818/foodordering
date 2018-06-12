import tkinter as tk
from tkinter import *
from tkinter import messagebox
import manager_actions as ma
import main_control


#Global variables
rows=[]
foods=[]

# input manager name and password to login
class manager_login(tk.Frame):
	def __init__(self,master):

		tk.Frame.__init__(self, master)

		label_1 = Label(master,text = 'Manager Name')
		label_2 = Label(master,text = 'Password')
		label_1.grid(row=0,column=0)
		label_2.grid(row=1,column=0)

		entry_1 = Entry(master)
		entry_2 = Entry(master)
		
		entry_1.grid(row=0,column=1)
		entry_2.grid(row=1,column=1)

		btn1 = Button(master, text="Comfirm",height=1,width=15,command=lambda: ma.log_in(entry_1.get(),entry_2.get()))
		btn1.grid(row=3,column=0)

		btn2 = Button(master, text="Return",height=1,width=15,command = lambda: self.select_frame(master,main_control.main))
		btn2.grid(row=3,column=1)

	def select_frame(self,master,new_frame):
		root =tk.Tk()
		f = new_frame(root)
		self.master.destroy()

# UI to add a new staff to database
class add_staff(tk.Frame):
	def __init__(self,master):

		tk.Frame.__init__(self, master)
		master.title("Add a Staff")

		label_1 = Label(master,text = 'staff_name')
		label_2 = Label(master,text = 'staff_password')
		label_1.grid(row=0,column=0)
		label_2.grid(row=1,column=0)

		entry_1 = Entry(master)
		entry_2 = Entry(master)
		
		entry_1.grid(row=0,column=1)
		entry_2.grid(row=1,column=1)

		btn1 = Button(master, text="Add Staff to DB",height=1,width=15,command=lambda: ma.add_staff(entry_1.get(),entry_2.get()))
		btn1.grid(row=2,column=0)

		btn2 = Button(master, text="Return",height=1,width=15,command = lambda: self.select_frame(master,page_manager))
		btn2.grid(row=2,column=1)

	def select_frame(self,master,new_frame):
		root =tk.Tk()
		f = new_frame(root)
		self.master.destroy()

# delte a user from database 
class delete_staff(tk.Frame):
	def __init__(self,master):
		
		tk.Frame.__init__(self, master)

		master.title("Delete a Staff")

		label_1 = Label(master,text = 'staff_name')
		label_1.grid(row=0,column=0)
		entry_1 = Entry(master)
		entry_1.grid(row=0,column=1)

		btn1 = Button(master, text="Comfirm",height=1,width=15,command=lambda: ma.delete_staff(entry_1.get()))
		btn1.grid(row=1,column=0)

		btn2 = Button(master, text="Return",height=1,width=15,command = lambda: self.select_frame(master,page_manager))
		btn2.grid(row=1,column=1)

	def select_frame(self,master,new_frame):
		root =tk.Tk()
		f = new_frame(root)
		self.master.destroy()

# add a food  to menu in database 
class add_food(tk.Frame):
	def __init__(self,master):
		tk.Frame.__init__(self, master)
		
		label_1 = Label(master,text = 'food_name')
		label_1.grid(row=0,column=0)
		label_2 = Label(master,text = 'Quantity per Order')
		label_2.grid(row=1,column=0)
		label_3 = Label(master,text = 'Food Picture Link')
		label_3.grid(row=2,column=0)
		label_3 = Label(master,text = 'Price per Order')
		label_3.grid(row=3,column=0)

		entry_1 = Entry(master)
		entry_1.grid(row=0,column=1)
		entry_2 = Entry(master)
		entry_2.grid(row=1,column=1)
		entry_3 = Entry(master)
		entry_3.grid(row=2,column=1)
		entry_4 = Entry(master)
		entry_4.grid(row=3,column=1)

		btn1 = Button(master, text="Add",height=1,width=15,command=lambda: ma.add_food(entry_1.get(),entry_2.get(),entry_3.get(),entry_4.get()))
		btn1.grid(row=4,column=0)

		btn2 = Button(master, text="Return",height=1,width=15,command = lambda: self.select_frame(master,page_manager))
		btn2.grid(row=4,column=1)
	

	def select_frame(self,master,new_frame):
		root =tk.Tk()
		f = new_frame(root)
		self.master.destroy()


# Remove food from menu in database
class remove_food(tk.Frame):
	def __init__(self,master):
		tk.Frame.__init__(self, master)
		master.title('Remove Food')
		ma.list_foods()

		T = Text(master, height=15, width=30)
		T.grid(row=0)
		
		T.insert(END,"ID  Name Quantity Price"+'\n')
		for food in foods:
			T.insert(END,str(food[0])+'     '+food[1]+'        '+food[1]+'      '+str(food[2])+'\n')

		label_1 = Label(master,text = 'food_name')
		label_1.grid(row=1,column=0)

		entry_1 = Entry(master)
		entry_1.grid(row=1,column=1)

		btn1 = Button(master, text="Remove Food",height=1,width=15,command=ma.remove_food(entry_1.get()))
		btn1.grid(row=2,column=0)

		btn2 = Button(master, text="Return",height=1,width=15,command = lambda: self.select_frame(master,page_manager))
		btn2.grid(row=2,column=1)

	def select_frame(self,master,new_frame):
		root =tk.Tk()
		f = new_frame(root)
		self.master.destroy()


# list all the staffs in db
def create_list_staffs():
	root=tk.Tk()
	f =list_staffs(root) 

##UI to list all the staffs in database
class list_staffs(tk.Frame):
	def __init__(self,master):
		tk.Frame.__init__(self, master) 

		T = Text(master, height=15, width=30)
		T.pack()
		
		for row in rows:
			T.insert(END,row[0]+'\n')
			
		
	# select a new frame
	def select_frame(self,master,new_frame):
		root =tk.Tk()
		f = new_frame(root)
		self.master.destroy()


# list all the actions can be done by manager 
class page_manager(tk.Frame):
	def __init__(self,master):

		tk.Frame.__init__(self, master) 

		btn1 = tk.Button(master, text="Add a Staff",height=3,width=23,command=lambda: self.select_frame(master,add_staff))
		btn1.pack(fill=X)

		btn2 = tk.Button(master, text="Delete Staff",height=3,width=23,command=lambda: self.select_frame(master,delete_staff))
		btn2.pack(fill=X)

		btn5 = tk.Button(master, text="List Staffs",height=3,width=23,command=ma.list_staffs)
		btn5.pack(fill=X)

		btn3 = tk.Button(master, text="Add Food to Menu",height=3,width=23,command=lambda: self.select_frame(master,add_food))
		btn3.pack(fill=X)

		btn6 = tk.Button(master, text="Remove Food",height=3,width=23,command=lambda: self.select_frame(master,remove_food))
		btn6.pack(fill=X)

		btn7 = tk.Button(master, text="Change Manager Name and Password",height=3,width=23)
		btn7.pack(fill=X)

		btn4 = tk.Button(master, text="Return",height=3,width=23,command=lambda: self.select_frame(master,main_control.main))
		btn4.pack(fill=X)

	# select a new frame
	def select_frame(self,master,new_frame):
		root =tk.Tk()
		f = new_frame(root)
		self.master.destroy()

# wrong name or password
def login_fail():
	messagebox.showerror("Error", "Invalid Manager Account or Password")

# log in successfully and go in main page
def login_succeed():
	root = tk.Tk()
	f = page_manager(root)
	