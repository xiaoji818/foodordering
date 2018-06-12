# object of customer
class customer(object):
	def __init__(self,name,phone,address):
		self.name=name
		self.phone=phone
		self.address=address

	def __str__(self):
		string = ''
		string += 'Name: {}\n'.format(self.name)
		string += 'Phone: {}\n'.format(self.phone)
		string += 'Address: {}\n'.format(self.address)
		return string
		
