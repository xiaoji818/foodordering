import psycopg2 as pg2
import tkinter as tk
from tkinter import messagebox


def change_password():
	pass

def serve_orders():
	pass

def view_order_list():
	pass

def finish_list():
	pass

# check the validity of staff
def check_staff(staff_name,password):
	try:
		conn = pg2.connect("dbname='foodordering' user='guest' host='localhost' password= '111' ")
	except:
		print('Fail to connect to database')

	cur = conn.cursor()
	
	try:
		cur.execute("""SELECT password FROM staffs WHERE s_name = staff_name""".format(staff_name))
		conn.commit()

	except:
		messagebox.showerror("Error", "Staff Account does not exist")

	else:
		rows = cur.fetchall()
		for row in rows:
			if row == password:
				page_staff.page_manage_orders()
		messagebox.showerror("Error", "Invalid Staff Account or Password")

	cur.close()
	conn.close()


