import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import page_customer
import page_manager
import page_staff

# Our main page
class main(tk.Frame):
	def __init__(self,master):

		tk.Frame.__init__(self, master)

		#import backgournd image
		global img,render 
		img= Image.open('maichicken.png')
		render=ImageTk.PhotoImage(img)
		label= tk.Label(master, image = render)
		label.pack()

		btn1 = tk.Button(master, text="Client Entrance",height=3,width=23,command=lambda: self.select_frame(master,page_customer.page_customer))
		btn1.pack(side=LEFT,fill=X)

		btn2 = tk.Button(master, text="Staff Entrance",height=3,width=23,command=lambda: self.select_frame(master,page_staff.page_staff))
		btn2.pack(side=LEFT,fill=X)

		btn3 = tk.Button(master, text="Shop Owner Entrance",height=3,width=23,command=lambda: self.select_frame(master,page_manager.manager_login))
		btn3.pack(side=LEFT,fill=X)

		btn4 = tk.Button(master, text="Quit",height=3,width=23,command=master.quit)
		btn4.pack(side=LEFT,fill=X)

	# select a new frame
	def select_frame(self,master,new_frame):
		root =tk.Tk()
		f = new_frame(root)
		self.master.destroy()



#execution of the frames
if __name__ == "__main__":
	root=tk.Tk()
	app=main(root)
	app.pack()
	app.mainloop()