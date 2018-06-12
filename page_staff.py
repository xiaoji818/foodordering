import tkinter as tk
from tkinter import *
import staff_actions as st
import main_control
# Customer Page
class page_staff(tk.Frame):
	def __init__(self,master):
		
		tk.Frame.__init__(self, master)
		#labels in the frame
		label_1 = Label(master,text = 'Staff_Account')
		label_2 = Label(master,text = 'Password')
		label_1.grid(row=0,column=0)
		label_2.grid(row=1,column=0)

		#entries in the frame 
		entry_1 = Entry(master)
		entry_2 = Entry(master)
		entry_1.grid(row=0,column=1)
		entry_2.grid(row=1,column=1)
		

		#buttons in the frame
		btn1 = Button(master, text="Comfirm",height=1,width=15,command=lambda: st.check_staff(entry_1.get(),entry_2.get()))
		btn1.grid(row=3,column=0)

		btn2 = Button(master, text="Return",height=1,width=15,command = lambda: self.select_frame(master,main_control.main))
		btn2.grid(row=3,column=1)
	# select a new frame

	def select_frame(self,master,new_frame):
		root =tk.Tk()
		f = new_frame(root)
		f.pack()
		self.master.destroy()

class manage_orders(tk.Frame):
	def __init__(self,master):
		tk.Frame.__init__(self, master)
		


def page_manage_orders():
	root=tk.Tk()
	app=manage_orders(root)
	app.pack()
	app.mainloop()
	