#This is the customer end to make an order
#Code Author: Zhuoli Xiao

#Import libraries
import order
import customer
import psycopg2 as pg2
import page_customer as pc

#Global Variables
orderList = [] #list to store your current orders

def customer_login(name,phone,address):
	global current_customer
	current_customer=customer.customer(name,phone,address)
	return store_customer(current_customer)

def store_customer(customer):
	try:
		conn = pg2.connect("dbname='foodordering' user='guest' host='localhost' password= '111' ")
	except:
		print('Fail to connect to database')

	cur = conn.cursor()
	
	try:
		cur.execute("""INSERT INTO customers(customername,customerphone,customeraddress) VALUES('{}','{}','{}')""".format(customer.name,customer.phone,customer.address))
		conn.commit()
	
	except:
		print ('customer exists already')

	else:
		return True
		conn.close()

	conn.close()


def get_menu():

	try:
		conn = pg2.connect("dbname='foodordering' user='guest' host='localhost' password= '111' ")
	except:
		print('Fail to connect to database')

	cur = conn.cursor()

	try:
		cur.execute("SELECT foodname,quantity,price,foodid FROM food")
		conn.commit()
	
	except:
		print ('Fail to access food menu')

	food_menu=cur.fetchall()
	conn.close()

	return food_menu

# Make an order
def add_order(order):
	orderList.append(order)

# Remove an order, defined by a foodID from your current orders
def remove_order(foodID):
	for item in orderList:
		if item.foodID == foodID:
			orderList.remove(item)
			break

#get the total price of food
def get_total():
	total = 0
	for item in orderList:
		total += item.foodPrice
	return total

# print current orders to customers
def curOrders():
	print('Dear Customer, you have {} orders'.format(len(orderList)))
	for item in orderList:
		print(item.foodName)

def comfirm_order():
	pass

# customer makes a payment
def pay():
	total = get_total()
	print ('Dear customer, your total is {}. Thanks!'.format(total))


	