import tkinter as tk
from tkinter import *
from tkinter import messagebox
import customer_ordering as co
import main_control



# Customer Page
class page_customer(tk.Frame):
	def __init__(self,master):
		
		tk.Frame.__init__(self, master)
		master.title("Customer Login")
		#labels in the frame
		label_1 = Label(master,text = 'Customer Name')
		label_2 = Label(master,text = 'Phone Number')
		label_3 = Label(master,text = 'Address')
		label_1.grid(row=0,column=0)
		label_2.grid(row=1,column=0)
		label_3.grid(row=2,column=0)

		#entries in the frame 
		entry_1 = Entry(master)
		entry_2 = Entry(master)
		entry_3 = Entry(master)
		entry_1.grid(row=0,column=1)
		entry_2.grid(row=1,column=1)
		entry_3.grid(row=2,column=1)

		#buttons in the frame
		btn1 = Button(master, text="Login",height=1,width=15,command=lambda: self.login(entry_1.get(),entry_2.get(),entry_3.get()))
		btn1.grid(row=3,column=0)

		btn2 = Button(master, text="Return",height=1,width=15,command = lambda: self.select_frame(master,main_control.main))
		btn2.grid(row=3,column=1)
	# select a new frame
	def select_frame(self,master,new_frame):
		root =tk.Tk()
		f = new_frame(root)
		self.master.destroy()

	def login(self,name,phone,address):
		res=co.customer_login(name,phone,address)
		if res==True:
			self.select_frame(self.master,page_ordering)
		else:
			messagebox.showerror('Error','Fail to login as a customer.')

class page_ordering(tk.Frame):
	def __init__(self,master):
		
		tk.Frame.__init__(self, master)
		master.title("Ordering Food")

		scrollbar=Scrollbar(master)

		mylist = Listbox(master, yscrollcommand = scrollbar.set, width=70, height=15)
		food_menu=co.get_menu()

		for food in food_menu:
			mylist.insert(END,'FoodName: '+food[0]+'  ' + 'Quantity: '+food[1]+' '+ 'Price: '+str(food[2])+'  '+'FoodID: '+str(food[3])+'  ')

		mylist.pack( side = LEFT, fill = BOTH )
		scrollbar.pack( side = LEFT, fill = Y )
		scrollbar.config( command = mylist.yview )

		label_1 = Label(master, text="FoodID:",height=1,width=15)
		label_1.pack (side=TOP)
		entry_1 = Entry(master)
		entry_1.pack(side=TOP)

		btn1 = Button(master, text="Add Food to Order",height=1,width=15)
		btn1.pack()

		btn2 = Button(master, text="View Current Order",height=1,width=15)
		btn2.pack()

		btn3 = Button(master, text="Remove Food",height=1,width=15)
		btn3.pack()

		btn4 = Button(master, text="Sumbit Order",height=1,width=15)
		btn4.pack()

		btn4 = Button(master, text="Return",height=1,width=15)
		btn4.pack()

	def select_frame(self,master,new_frame):
		root =tk.Tk()
		f = new_frame(root)
		self.master.destroy()





	