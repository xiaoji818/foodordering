# control the behaviours of customers
from tkinter import *
from PIL import ImageTk,Image

import customer_ordering 
from order import order

#global variables
cn = 'aa'
pn = 'aa'
ad = 'aa'
enter = False
 
# record user info from input
def record_info(c,p,a):
	 global cn,pn,ad
	 cn = c
	 pn = p
	 ad = a

def set_info():
	print(cn)

# create the UI frame to gather infomation
def create_frame():
	page= Tk()
	page.title('Customer Info')
	#labels in the frame
	label_1 = Label(page,text = 'Customer Name')
	label_2 = Label(page,text = 'Phone Number')
	label_3 = Label(page,text = 'Address')
	#entries in the frame 
	entry_1 = Entry(page)
	entry_2 = Entry(page)
	entry_3 = Entry(page)
	record_info(entry_1.get(),entry_2.get(),entry_3.get())

	#buttons in the frame
	btn1 = Button(page, text="Comfirm",height=1,width=15)

	btn2 = Button(page, text="Return",height=1,width=15,command = page.destroy)

	#put the widgets in positions
	label_1.grid(row=0)
	label_2.grid(row=1)
	label_3.grid(row=2)

	entry_1.grid(row=0,column=1)
	entry_2.grid(row=1,column=1)
	entry_3.grid(row=2,column=1)

	btn1.grid(row=3,column=0)
	btn2.grid(row=3,column=1)

	page.mainloop()

def customer_main():
	create_frame()