import tkinter as tk
from tkinter import *
from tkinter import messagebox
import page_manager as pm
import psycopg2 as pg2


def log_in(name,pw):
	global password
	password=pw
	try:
		conn = pg2.connect("dbname='foodordering' user='{}' host='localhost' password= '{}' ".format(name,pw))
	except:
		messagebox.showerror("Error","Login fail: wrong account or password")
	else:
		pm.login_succeed()	
		conn.close()
	

def update_password(npw):
	try:
		conn = pg2.connect("dbname='foodordering' user='manager' host='localhost' password= '{}' ".format(password))
	except:
		print('Fail to connect to database')
	cur = conn.cursor()

	try:
		cur.execute("ALTER USER manager WITH PASSWORD '{}'".format(npw))
		conn.commit()
	except:
		messagebox.showerror("Error","Fail to update password")
	else:
		messagebox.showinfo("Succeed","Succeed to update password")
	conn.close()


#add a user to system
def add_staff(staff_name,staff_password):
	try:
		conn = pg2.connect("dbname='foodordering' user='manager' host='localhost' password= '{}' ".format(password))
	except:
		print('Fail to connect to database')

	cur = conn.cursor()

	try:
		cur.execute("""CREATE USER {} WITH PASSWORD '{}';""".format(staff_name,staff_password))
		cur.execute("""Grant Select, Delete, Insert On TABLE processingfood TO {}""".format(staff_name))
		cur.execute("""Grant Select On TABLE food TO {}""".format(staff_name))
		conn.commit()
	except:
		print('Fail to create a User or User already exists')

	conn.close()

# remove a staff from database
def delete_staff(staff_name):
	try:
		conn = pg2.connect("dbname='foodordering' user='manager' host='localhost' password= '{}' ".format(password))
	except:
		print('Fail to connect to database')

	cur = conn.cursor()

	try:
		cur.execute("""REVOKE ALL privileges ON Table processingfood FROM {}""".format(staff_name))
		cur.execute("""REVOKE ALL privileges ON Table food FROM {}""".format(staff_name))
		cur.execute("""Drop User IF EXISTS {};""".format(staff_name))
		conn.commit()
	except:
		print('User {} does not exist'.format(staff_name))
	else:
		messagebox.showinfo('Info','Successfully remove User {}'.format(staff_name)) 
	conn.close()

# add a food to store menu
def add_food(food_name,food_quantity,food_pic,food_price):
	try:
		conn = pg2.connect("dbname='foodordering' user='manager' host='localhost' password= '{}' ".format(password))
	except:
		print('Fail to connect to database')

	cur = conn.cursor()
	
	try:
		cur.execute("""INSERT INTO food(foodname,quantity,piclink,price) VALUES('{}','{}','{}',{})""".format(food_name,food_quantity,food_pic,food_price))
		conn.commit()
	except:
		print("Fail to insert food to menu.")
	else:
		messagebox.showinfo('Info','Successfully insert food {}'.format(food_name)) 
	conn.close()

# list all foods in menu
def list_foods():
	
	try:
		conn = pg2.connect("dbname='foodordering' user='manager' host='localhost' password= '{}' ".format(password))
	except:
		print('Fail to connect to database')

	cur = conn.cursor()

	cur.execute("""Select foodid,foodname,quantity,price FROM food;""")
	conn.commit()

	foods = cur.fetchall()
	pm.foods=foods

	conn.close()

# remove all foods in given name
def remove_food(food_id):
	try:
		conn = pg2.connect("dbname='foodordering' user='manager' host='localhost' password= '{}' ".format(password))
	except:
		print('Fail to connect to database')


	cur = conn.cursor()
	cur.execute("DELETE FROM food WHERE foodid={}".format(food_id))
	conn.commit()

	conn.close()


# list all the users in the db
def list_staffs():
	try:
		conn = pg2.connect("dbname='foodordering' user='manager' host='localhost' password= '{}' ".format(password))
	except:
		print('Fail to connect to database')

	cur = conn.cursor()

	cur.execute("""Select * FROM pg_user;""")
	conn.commit()
	

	rows = cur.fetchall()
	pm.rows=rows
	pm.create_list_staffs()

	conn.close()

	
